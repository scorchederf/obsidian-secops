---
mitre_id: "T1007"
mitre_name: "System Service Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--322bad5a-1c49-4d23-ab79-76d641794afa"
mitre_created: "2017-05-31T21:30:21.315Z"
mitre_modified: "2025-10-24T17:48:36.812Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1007/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-PSA"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as `sc query`, `tasklist /svc`, `systemctl --type=service`, and `net start`. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [[T1007-system_service_discovery|T1007: System Service Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Workspace

- [[workspaces/attack/techniques/T1007-system_service_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1007-system_service_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools

- [[net|Net (S0039)]]
- [[tasklist|Tasklist (S0057)]]
- [[poshc2|PoshC2 (S0378)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]

## Platforms

- Linux
- macOS
- Windows

