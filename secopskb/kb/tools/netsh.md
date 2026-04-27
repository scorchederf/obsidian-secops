---
mitre_id: "S0108"
mitre_name: "netsh"
mitre_type: "tool"
mitre_stix_id: "tool--5a63f900-5e7e-4928-a746-dd4558e1df71"
mitre_created: "2017-05-31T21:33:06.083Z"
mitre_modified: "2025-02-25T17:54:17.038Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0108/"
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
  - "netsh"
  - "netsh.exe"
aliases:
  - "S0108"
  - "netsh"
  - "netsh.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh)

## Workspace

- [[workspaces/tools/S0108-netsh-note|Open workspace note]]

![[workspaces/tools/S0108-netsh-note]]

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

