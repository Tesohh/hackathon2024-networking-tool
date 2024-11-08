import requests
from enum import Enum
# def fetch_cves() -> bool:
#     with open("scanner/.cves/cve_metadata.json") as f:
#         meta = json.load(f)
#         last_fetch = datetime.date.fromisoformat(meta["lastFetch"])
#
#         now = datetime.date.today()
#
#         delta = (now - last_fetch)
#         if delta.days < 1:
#             print(f"last update was {delta.days} days ago, no CVE fetching needed")
#             return False
#
#     print(f"Fetching CVEs... (last update was {delta.days} days ago)")
#     res = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0")
#     jres = res.json()
#
#
#
#     return True
#

# class CPEPart(Enum):
#     APPLICATION = 'a'
#     HARDWARE = 'h'
#     OPERATINGSYSTEM = 'o'

# def build_cpe(part: CPEPart, vendor: str, product: str, version: str, update: str = "*", edition: str = "*", language: str = "*") -> str:
#     return f""

def fetch_cves_for_cpe(cpe: str, only_vulnerable = True) -> dict:
    res = requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe}{'&isVulnerable' if only_vulnerable else ''}")
    return res.json()

