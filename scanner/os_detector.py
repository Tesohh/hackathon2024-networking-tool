
from subprocess import Popen, PIPE, DEVNULL
import re


def get_nmap_xml(argv: list[str]) -> str:
    with Popen(argv, stdout=DEVNULL, stderr=PIPE) as proc:
        return proc.stderr.read().decode()



def get_cpe(addr: str) -> dict[str, tuple[str, ...]]:

    vendor_pattern = r'''addr="(.+)" addrtype="mac" vendor="(.+)"'''
    cpe_pattern = r'''<cpe>(cpe:.+)<\/cpe>'''

    xml = get_nmap_xml(["nmap", "-oX", "/dev/stderr", "-O", "-v", addr])

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

