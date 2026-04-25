---
mitre_id: "S0190"
mitre_name: "BITSAdmin"
mitre_type: "tool"
mitre_stix_id: "tool--64764dc6-a032-495f-8250-1e4c06bdc163"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-04-16T20:38:52.586Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0190/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "BITSAdmin"
aliases:
  - "S0190"
  - "BITSAdmin"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin)

## Workspace

- [[workspaces/tools/S0190-bitsadmin-note|Open workspace note]]

![[workspaces/tools/S0190-bitsadmin-note]]

## Uses Techniques

- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

