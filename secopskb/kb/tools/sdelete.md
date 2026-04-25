---
mitre_id: "S0195"
mitre_name: "SDelete"
mitre_type: "tool"
mitre_stix_id: "tool--d8d19e33-94fd-4aa3-b94a-08ee801a2153"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-04-25T14:45:30.257Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0195/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "SDelete"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

[SDelete](https://attack.mitre.org/software/S0195) is an application that securely deletes data in a way that makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools. (Citation: Microsoft SDelete July 2016)

## Workspace

- [[notes/tools/S0195-sdelete-note|Open workspace note]]

![[notes/tools/S0195-sdelete-note]]

## Uses Techniques

- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]
- [[T1485-data_destruction|T1485: Data Destruction]]

