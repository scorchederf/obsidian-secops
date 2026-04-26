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
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as `sc query`, `tasklist /svc`, `systemctl --type=service`, and `net start`. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [[T1007-system_service_discovery|T1007: System Service Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Workspace

- [[workspaces/attack/techniques/T1007-system_service_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1007-system_service_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

### Sigma Rules

- [[kb/sigma/rules/fca949cc_79ca_446e_8064_01aa7e52ece5-hacktool_pchunter_execution|HackTool - PCHunter Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/51f17016_d8fa_4360_888a_df4bf92c4a04-get_service_execution|Get-Service Execution (command_prompt; windows)]]
- [[kb/atomic/tests/5f864a3f_8ce9_45c0_812c_bdf7d8aeacc3-system_service_discovery_net_exe|System Service Discovery - net.exe (command_prompt; windows)]]
- [[kb/atomic/tests/7cd7eaa3_9ccc_460d_96d2_c6fb13e6d58a-system_service_discovery_windows_scheduled_tasks_schtasks|System Service Discovery - Windows Scheduled Tasks (schtasks) (command_prompt; windows)]]
- [[kb/atomic/tests/89676ba1_b1f8_47ee_b940_2e1a113ebc71-system_service_discovery|System Service Discovery (command_prompt; windows)]]
- [[kb/atomic/tests/8f2a5d2b_4018_46d4_8f3f_0fea53754690-system_service_discovery_linux_init_scripts|System Service Discovery - Linux init scripts (sh; linux)]]
- [[kb/atomic/tests/9b378962_a75e_4856_b117_2503d6dcebba-system_service_discovery_macos_launchctl|System Service Discovery - macOS launchctl (sh; macos)]]
- [[kb/atomic/tests/d70d82bd_bb00_4837_b146_b40d025551b2-system_service_discovery_services_registry_enumeration|System Service Discovery - Services Registry Enumeration (powershell; windows)]]
- [[kb/atomic/tests/f4b26bce_4c2c_46c0_bcc5_fce062d38bef-system_service_discovery_systemctl_service|System Service Discovery - systemctl/service (bash; linux)]]

<!-- generated-detection-validation-end -->

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
- [[poshc2|PoshC2 (S0378)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[tasklist|Tasklist (S0057)]]


## Platforms

- Linux
- macOS
- Windows

