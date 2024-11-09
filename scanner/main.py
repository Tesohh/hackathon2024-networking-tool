
import asyncio
import json
import sys

import scan
import cpe_detector as cpe_detector
from cve.cve import CVE # :)
import cve.fetch_cves


def normalize_cpe(cpe: str) -> str:
    return cpe.replace("/", "2.3:", 1)

async def msg_dump_task(queue: asyncio.Queue) -> None:
    while message := await queue.get():
        print(json.dumps(message), flush=True)

def sendmsg(queue: asyncio.Queue, agent: str, **extras) -> None:
    queue.put_nowait({"agent": agent, **extras})

async def main(iface: str):

    queue = asyncio.Queue()

    dump_task = asyncio.create_task(msg_dump_task(queue))

    ## do the network scan
    avail = await scan.interactive_scan(network   = scan.get_network(iface),
                                        timeout   = 3.0,
                                        max_tasks = 1000,
                                        queue     = queue)

    ## find the CPE for each host
    hosts_info = await cpe_detector.interactive_cpe_finder(queue     = queue,
                                                           addresses = avail,
                                                           max_tasks = 30)

    ## download the necessary CVE infos
    cve_map = await cve.fetch_cves.interactive_cve_fetch(cpe_list  = list(dict.fromkeys(normalize_cpe(cpe) for item in hosts_info.values() for cpe in item["cpe"])),
                                                         queue     = queue,
                                                         max_tasks = 5)

    result = []

    ## associate the hosts with the corresponding CVE
    for addr, info in hosts_info.items():

        host_cve = [CVE.from_json(vul["cve"]) for cpe in info["cpe"] for vul in cve_map.get(normalize_cpe(cpe), {}).get("vulnerabilities", [])]
        host_cve = [cve.to_json() for cve in host_cve if not cve.patched]

        result.append({
            "address": addr,
            "mac":     info["mac"],
            "vendor":  info["vendor"],
            "cve":     host_cve
        })

        await queue.put({"agent": "cve-assign", "host": addr, "cve": host_cve})

    await queue.put(None)
    await dump_task

    json.dump({"agent": "final", "data": result}, sys.stdout, indent=None)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
    sys.exit(0)
