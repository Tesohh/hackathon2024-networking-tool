
from subprocess import Popen, PIPE, DEVNULL
import re


def get_nmap_xml(argv: list[str]) -> str:
    with Popen(argv, stdout=DEVNULL, stderr=PIPE) as proc:
        return proc.stderr.read().decode()

def get_cpe(addr: str) -> dict:

    vendor_pattern = r'''addr=".+" addrtype="mac" vendor="(.+)"'''
    cpe_pattern = r'''<cpe>(cpe:.+)<\/cpe>'''

    xml = get_nmap_xml(["nmap", "-oX", "/dev/stderr", "-O", "-v", addr])

    vendors = dict.fromkeys(re.findall(vendor_pattern, xml))
    cpe = dict.fromkeys(re.findall(cpe_pattern, xml))

    return {
        "vendor": tuple(vendors),
        "cpe":    tuple(cpe)
    }

