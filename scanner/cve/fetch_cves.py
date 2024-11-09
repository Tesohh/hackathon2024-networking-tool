
import aiohttp
import asyncio
import os
import json

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe}&isVulnerable"

async def download_cve(cpe: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(cpe=cpe)) as response:
            response.raise_for_status()
            return await response.json()

async def get_cve(cpe: str, use_cache: bool = True) -> dict:

    if use_cache:
        filename = os.path.join(".cache", "cached_" + cpe.replace("/", "_"))

        if os.path.exists(filename):
            with open(filename) as fp:
                return json.load(fp)

    cve = await download_cve(cpe)

    if use_cache:
        os.makedirs(".cache", exist_ok=True)

        with open(filename, "w") as fp:
            json.dump(cve, fp)

    return cve

async def interactive_cve_fetch(cpe_list: list[str], queue: asyncio.Queue, max_tasks: int) -> dict:

    lock = asyncio.Semaphore(max_tasks)

    cve = {}

    async def _download_cve(cpe):
        async with lock:

            await queue.put({"agent": "cve", "type": "cve download start", "cpe": cpe})

            cve[cpe] = await get_cve(cpe)

            await queue.put({"agent": "cve", "type": "cve download complete", "cpe": cpe})

    await asyncio.gather(*(_download_cve(cpe) for cpe in cpe_list))

    await queue.put({"agent": "cve", "type": "cve download completed"})

    return cve
