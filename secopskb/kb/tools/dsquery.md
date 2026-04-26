---
mitre_id: "S0105"
mitre_name: "dsquery"
mitre_type: "tool"
mitre_stix_id: "tool--38952eac-cb1b-4a71-bad2-ee8223a1c8fe"
mitre_created: "2017-05-31T21:33:04.937Z"
mitre_modified: "2025-04-16T20:38:51.407Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0105/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "dsquery"
  - "dsquery.exe"
aliases:
  - "S0105"
  - "dsquery"
  - "dsquery.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

[dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active Directory for information from a system within a domain. (Citation: TechNet Dsquery) It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

## Workspace

- [[workspaces/tools/S0105-dsquery-note|Open workspace note]]

![[workspaces/tools/S0105-dsquery-note]]

## Uses Techniques

- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

