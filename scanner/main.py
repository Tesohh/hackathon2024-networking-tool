
import asyncio
import json
import sys

import scan
import os_detector
import cve.cve
import cve.fetch_cves


async def download_cve(cpe: str, to: dict):
    if cpe in to:
        return
    to[cpe] = None
    to[cpe] = await cve.fetch_cves.from_cpe(cpe)

def normalize_cpe(cpe: str) -> str:
    return cpe.replace("/", "2.3:", 1)

async def main(iface: str):

    s = asyncio.Semaphore(1000)
    res = set()

    await asyncio.gather(*(scan.do_test(ip_addr, s, 3.0, res) for ip_addr in scan.network_gen(scan.get_network(iface))))

    host_info_map = {addr: os_detector.get_cpe(addr) for addr in res}

    cve_infos: dict[str, dict] = {}

    await asyncio.gather(*(download_cve(normalize_cpe(cpe), cve_infos) for item in host_info_map.values() for cpe in item["cpe"]))

    result = []

    for addr, info in host_info_map.items():

        cve_list = set()

        for cpe in info["cpe"]:
            for vul in cve_infos[normalize_cpe(cpe)]["vulnerabilities"]:
                cve_list.add(cve.cve.CVE.from_json(vul["cve"]))

        result.append({
            "address": addr,
            "mac":     info["mac"],
            "vendor":  info["vendor"],
            "cve":     list(cve.to_json() for cve in cve_list)
        })

    json.dump(result, sys.stdout, indent="\t")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
    sys.exit(0)
