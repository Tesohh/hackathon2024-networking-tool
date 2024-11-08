
import asyncio
import json
import sys

import scanner
import os_detector



async def main(iface: str):

    s = asyncio.Semaphore(1000)
    res = set()

    await asyncio.gather(*(scanner.do_test(ip_addr, s, 3.0, res) for ip_addr in scanner.network_gen(scanner.get_network(iface))))

    host_info_map = {addr: os_detector.get_cpe(addr) for addr in res}

    json.dump(host_info_map, sys.stdout, indent=4)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
    sys.exit(0)
