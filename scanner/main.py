
import asyncio
import json
import sys

import scanner
import os_detector
import cve.cve
import cve.fetch_cves



async def main(iface: str):

    s = asyncio.Semaphore(1000)
    res = set()

    await asyncio.gather(*(scanner.do_test(ip_addr, s, 3.0, res) for ip_addr in scanner.network_gen(scanner.get_network(iface))))

    host_info_map = {addr: os_detector.get_cpe(addr) for addr in res}

    cves: list[cve.cve.CVE] = []
    for addr, item in host_info_map.items():
        for cpe in item["cpe"]:
            res = cve.fetch_cves.from_cpe(cpe)
            for vuln in res["vulnerabilities"]:
                cves.append(cve.cve.CVE.from_json(vuln))

    print(cves)
    

    # json.dump(host_info_map, sys.stdout, indent=4)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
    sys.exit(0)
