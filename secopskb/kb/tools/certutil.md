---
mitre_id: "S0160"
mitre_name: "certutil"
mitre_type: "tool"
mitre_stix_id: "tool--0a68f1f1-da74-4d28-8d9a-696c082706cc"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2024-11-27T21:56:15.800Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0160/"
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
  - "certutil"
  - "certutil.exe"
aliases:
  - "S0160"
  - "certutil"
  - "certutil.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

[certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil)

## Workspace

- [[workspaces/tools/S0160-certutil-note|Open workspace note]]

![[workspaces/tools/S0160-certutil-note]]

## Uses Techniques

- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
    - [[T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

