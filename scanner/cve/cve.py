from __future__ import annotations
from dataclasses import dataclass

# what do we need?
# CVE id
# Vulnerability severity
# That's it

@dataclass
class CVE:
    id: str
    severity: str
    
    @classmethod
    def from_json(cls, src: dict) -> CVE:
        severity = "UNKNOWN"
        for k, v in src["metrics"].items():
            if k == "cvssMetricV2":
                severity = v[0]["baseSeverity"]
                break
            else:
                severity = v[0]["cvssData"]["baseSeverity"]
                break

        return CVE(
            id=src["id"],
            severity=severity
        )


