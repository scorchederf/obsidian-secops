---
mitre_id: "S0465"
mitre_name: "CARROTBALL"
mitre_type: "tool"
mitre_stix_id: "tool--5fc81b43-62b5-41b1-9113-c79ae5f030c4"
mitre_created: "2020-06-02T19:10:29.513Z"
mitre_modified: "2025-04-25T14:45:20.112Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0465/"
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
  - "CARROTBALL"
aliases:
  - "S0465"
  - "CARROTBALL"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

[CARROTBALL](https://attack.mitre.org/software/S0465) is an FTP downloader utility that has been in use since at least 2019. [CARROTBALL](https://attack.mitre.org/software/S0465) has been used as a downloader to install [SYSCON](https://attack.mitre.org/software/S0464).(Citation: Unit 42 CARROTBAT January 2020)

## Workspace

- [[workspaces/tools/S0465-carrotball-note|Open workspace note]]

![[workspaces/tools/S0465-carrotball-note]]

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

