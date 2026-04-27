---
mitre_id: "S0095"
mitre_name: "ftp"
mitre_type: "tool"
mitre_stix_id: "tool--cf23bf4a-e003-4116-bbae-1ea6c558d565"
mitre_created: "2017-05-31T21:33:00.565Z"
mitre_modified: "2025-06-04T16:11:23.752Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0095/"
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
  - "ftp"
  - "ftp.exe"
aliases:
  - "S0095"
  - "ftp"
  - "ftp.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP)

## Workspace

- [[workspaces/tools/S0095-ftp-note|Open workspace note]]

![[workspaces/tools/S0095-ftp-note]]

## Uses Techniques

- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

