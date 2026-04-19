---
id: S0361
name: Expand
created: 2019-02-19 19:17:14.971000+00:00
modified: 2025-04-25 14:45:29.018000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Expand

[Expand](https://attack.mitre.org/software/S0361) is a Windows utility used to expand one or more compressed CAB files.(Citation: Microsoft Expand Utility) It has been used by [BBSRAT](https://attack.mitre.org/software/S0127) to decompress a CAB file into executable content.(Citation: Palo Alto Networks BBSRAT)

## Properties

- id: S0361
- name: Expand
- created: 2019-02-19 19:17:14.971000+00:00
- modified: 2025-04-25 14:45:29.018000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

