
from subprocess import check_output
import socket
import asyncio
import sys



async def test_host(addr: int, timeout: float) -> bool:
    s = socket.socket()
    s.setblocking(False)

    try:
        await asyncio.wait_for(asyncio.get_event_loop().sock_connect(s, (addr, 80)), timeout)
    except asyncio.TimeoutError:
        return False
    except ConnectionRefusedError:
        return True
    except Exception as e:
        print(e)
    else:
        return True
    finally:
        s.close()

def get_network(iface: str) -> str:

    for line in check_output(["ip", "a", "list", iface]).decode().splitlines():
        if not "inet" in line:
            continue
        return line.split()[1]

    raise Exception("unable to get network address")

def network_gen(network: str):
    address, netmask = network.split("/")

    address_int = int.from_bytes(socket.inet_aton(address))
    netmask_int = (~((1 << (32 - int(netmask))) - 1)) & 0xFFFFFFFF

    net_id = address_int & netmask_int

    for i in range(1, 2 ** (32 - int(netmask)) - 1):
        yield socket.inet_ntoa(int.to_bytes(net_id + i, 4))

async def do_test(addr, lock, timeout, results: set[str]):
    async with lock:
        if await test_host(addr, timeout):
            print("HOST", addr, "is up", file=sys.stderr)
            results.add(addr)
