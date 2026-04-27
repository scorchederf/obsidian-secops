---
mitre_id: "S0552"
mitre_name: "AdFind"
mitre_type: "tool"
mitre_stix_id: "tool--f59508a6-3615-47c3-b493-6676e1a39a87"
mitre_created: "2020-12-28T18:35:50.244Z"
mitre_modified: "2024-09-25T15:21:53.462Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0552/"
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
  - "AdFind"
aliases:
  - "S0552"
  - "AdFind"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)

## Workspace

- [[workspaces/tools/S0552-adfind-note|Open workspace note]]

![[workspaces/tools/S0552-adfind-note]]

## Uses Techniques

- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

