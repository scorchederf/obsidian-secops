---
id: S0645
name: Wevtutil
created: 2021-09-14 21:45:30.280000+00:00
modified: 2024-09-25 20:32:25.006000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# Wevtutil

[Wevtutil](https://attack.mitre.org/software/S0645) is a Windows command-line utility that enables administrators to retrieve information about event logs and publishers.(Citation: Wevtutil Microsoft Documentation)

## Properties

- id: S0645
- name: Wevtutil
- created: 2021-09-14 21:45:30.280000+00:00
- modified: 2024-09-25 20:32:25.006000+00:00
- type: tool
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

