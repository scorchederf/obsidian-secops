---
mitre_id: "S1131"
mitre_name: "NPPSPY"
mitre_type: "tool"
mitre_stix_id: "tool--0630d1a7-54da-4a48-a6af-eb8a62b13c17"
mitre_created: "2024-05-17T18:49:15.318Z"
mitre_modified: "2024-10-28T19:00:14.732Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S1131/"
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
  - "NPPSPY"
aliases:
  - "S1131"
  - "NPPSPY"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

NPPSPY is an implementation of a theoretical mechanism first presented in 2004 for capturing credentials submitted to a Windows system via a rogue Network Provider API item. NPPSPY captures credentials following submission and writes them to a file on the victim system for follow-on exfiltration.(Citation: Huntress NPPSPY 2022)(Citation: Polak NPPSPY 2004)

## Workspace

- [[workspaces/tools/S1131-nppspy-note|Open workspace note]]

![[workspaces/tools/S1131-nppspy-note]]

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1656-impersonation|T1656: Impersonation]]

