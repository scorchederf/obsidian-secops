---
id: S0108
name: netsh
created: 2017-05-31 21:33:06.083000+00:00
modified: 2025-02-25 17:54:17.038000+00:00
type: tool
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

# netsh

[netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh)

## Properties

- id: S0108
- name: netsh
- created: 2017-05-31 21:33:06.083000+00:00
- modified: 2025-02-25 17:54:17.038000+00:00
- type: tool
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

