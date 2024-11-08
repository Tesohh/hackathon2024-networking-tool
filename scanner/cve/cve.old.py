from dataclasses import dataclass

# @dataclass
# class CVSS:
#     version: str
#     vector_string: str
#     access_vector: str
#     access_complexity: str
#     authentication: str
#     confidentiality_impact: str
#     integrity_impact: str
#     availability_impact: str
#     base_score: float
#
# def cvss_from_json(src: dict, key: str) -> CVSS:
#     cvss = CVSS(
#         version=src["version"],
#         vector_string=src["vectorString"],
#         access_vector=src["accessVector"],
#         access_complexity=src["accessComplexity"],
#         authentication=src["authentication"],
#         confidentiality_impact=src["confidentialityImpact"],
#         integrity_impact=src["integrityImpact"],
#         availability_impact=src["availabilityImpact"],
#         base_score=src["baseScore"]
#     )
#     return cvss

@dataclass 
class CVEMetrics:
    source: str
    type: str
    # scoring: CVSS
    base_severity: str
    exploitablity_score: float
    impact_score: float
    ac_insufficient_info: bool
    obtain_all_privilege: bool
    obtain_user_privilege: bool
    obtain_other_privilege: bool
    user_interaction_required: bool

def cvemetric_from_json(src: dict) -> CVEMetrics:
    cve_metrics = CVEMetrics(
        source=src["source"],
        type=src["type"],
        # scoring=cvss_from_json(src["cvssData"]),
        base_severity=src["baseSeverity"],
        exploitablity_score=src["exploitabilityScore"],
        impact_score=src["impactScore"],
        ac_insufficient_info=src["acInsufInfo"],
        obtain_all_privilege=src["obtainAllPrivilege"],
        obtain_user_privilege=src["obtainUserPrivilege"],
        obtain_other_privilege=src["obtainOtherPrivilege"],
        user_interaction_required=src.get("userInteractionRequired", False),
    )
    return cve_metrics

@dataclass
class CVE:
    id: str    
    cve_metrics: list[CVEMetrics]
    source_identifier: str

def cve_from_json(src: dict) -> CVE:
    metrics = []
    for k, v in src["metrics"].items():
        if k == "cvssMetricV30":
            for i in v:
                metrics.append(cvemetric_from_json(i))
        elif k == "cvssMetricV31":
            for i in v:
                metrics.append(cvemetric_from_json(i))
        elif k == "cvssMetricV2":
            for i in v:
                metrics.append(cvemetric_from_json(i))

    return CVE(
        id=src["id"],
        cve_metrics=metrics,
        source_identifier=src["sourceIdentifier"]
    )

