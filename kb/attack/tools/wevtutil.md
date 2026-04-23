---
mitre_id: "S0645"
mitre_name: "Wevtutil"
mitre_type: "tool"
mitre_stix_id: "tool--f91162cc-1686-4ff8-8115-bf3f61a4cc7a"
mitre_created: "2021-09-14T21:45:30.280Z"
mitre_modified: "2024-09-25T20:32:25.006Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0645/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Wevtutil"
---

# Wevtutil

[Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.(Citation: Wevtutil Microsoft Documentation)

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Workspace

- [[kb/notes/attack/tools/s0645-notes|Open workspace note]]

