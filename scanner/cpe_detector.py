
from asyncio.subprocess import create_subprocess_exec, PIPE, DEVNULL
import re
import asyncio


async def get_nmap_xml(argv: list[str]) -> str:
    proc = await create_subprocess_exec(*argv, stdout=DEVNULL, stderr=PIPE)
    await proc.wait()

    assert proc.stderr is not None

    return (await proc.stderr.read()).decode()

async def get_cpe(addr: str) -> dict[str, tuple[str, ...]]:

    vendor_pattern = r'''addr="(.+)" addrtype="mac" vendor="(.+)"'''
    cpe_pattern = r'''<cpe>(cpe:.+)<\/cpe>'''

    xml = await get_nmap_xml(["nmap", "-oX", "/dev/stderr", "-O", "-v", addr])

    mac_and_vendors = dict.fromkeys(re.findall(vendor_pattern, xml))
    cpe = dict.fromkeys(re.findall(cpe_pattern, xml))

    if mac_and_vendors:
        mac, vendors = zip(*mac_and_vendors)
    else:
        mac = vendors = ()

    return {
        "mac":    tuple(mac),
        "vendor": tuple(vendors),
        "cpe":    tuple(cpe)
    }

async def interactive_cpe_finder(queue: asyncio.Queue, addresses: list[str], max_tasks: int) -> dict:

    lock = asyncio.Semaphore(max_tasks)

    result = {}

    async def _find(addr):
        async with lock:
            cpe = await get_cpe(addr)
            await queue.put({"agent": "cpe", "type": "cpe result", "result": cpe})
            result[addr] = cpe

    await asyncio.gather(*(_find(addr) for addr in addresses))

    await queue.put({"agent": "cpe", "type": "cpe find completed"})

    return result
