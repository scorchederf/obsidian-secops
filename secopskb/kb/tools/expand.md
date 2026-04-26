---
mitre_id: "S0361"
mitre_name: "Expand"
mitre_type: "tool"
mitre_stix_id: "tool--ca656c25-44f1-471b-9d9f-e2a3bbb84973"
mitre_created: "2019-02-19T19:17:14.971Z"
mitre_modified: "2025-04-25T14:45:29.018Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0361/"
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
  - "Expand"
aliases:
  - "S0361"
  - "Expand"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

[Expand](https://attack.mitre.org/software/S0361) is a Windows utility used to expand one or more compressed CAB files.(Citation: Microsoft Expand Utility) It has been used by [BBSRAT](https://attack.mitre.org/software/S0127) to decompress a CAB file into executable content.(Citation: Palo Alto Networks BBSRAT)

## Workspace

- [[workspaces/tools/S0361-expand-note|Open workspace note]]

![[workspaces/tools/S0361-expand-note]]

## Uses Techniques

- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

