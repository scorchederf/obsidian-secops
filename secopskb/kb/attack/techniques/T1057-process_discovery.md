---
mitre_id: "T1057"
mitre_name: "Process Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--8f4a33ec-8b1f-4b80-a2f6-642b2e479580"
mitre_created: "2017-05-31T21:30:48.728Z"
mitre_modified: "2025-10-24T17:49:05.839Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1057/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
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

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from [[T1057-process_discovery|T1057: Process Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

In Windows environments, adversaries could obtain details on running processes using the [[tasklist|Tasklist (S0057)]] utility via [[cmd|cmd (S0106)]] or `Get-Process` via [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]. Information about processes can also be extracted from the output of [[T1106-native_api|T1106: Native API]] calls such as `CreateToolhelp32Snapshot`. In Mac and Linux, this is accomplished with the `ps` command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.(Citation: Sygnia ESXi Ransomware 2025)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show processes` can be used to display current running processes.(Citation: US-CERT-TA18-106A)(Citation: show_processes_cisco_cmd)

## Workspace

- [[workspaces/attack/techniques/T1057-process_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1057-process_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

### Sigma Rules

- [[kb/sigma/rules/fca949cc_79ca_446e_8064_01aa7e52ece5-hacktool_pchunter_execution|HackTool - PCHunter Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/11ba69ee_902e_4a0f_b3b6_418aed7d7ddb-discover_specific_process_tasklist|Discover Specific Process - tasklist (command_prompt; windows)]]
- [[kb/atomic/tests/3b3809b6_a54b_4f5b_8aff_cb51f2e97b34-process_discovery_get_process|Process Discovery - Get-Process (powershell; windows)]]
- [[kb/atomic/tests/4fd35378_39aa_481e_b7c4_e3bf49375c67-launch_taskmgr_from_cmd_to_view_running_processes|Launch Taskmgr from cmd to View running processes (command_prompt; windows)]]
- [[kb/atomic/tests/4ff64f0b_aaf2_4866_b39d_38d9791407cc-process_discovery_ps|Process Discovery - ps (sh; linux, macos)]]
- [[kb/atomic/tests/640cbf6d_659b_498b_ba53_f6dd1a1cc02c-process_discovery_wmic_process|Process Discovery - wmic process (command_prompt; windows)]]
- [[kb/atomic/tests/966f4c16_1925_4d9b_8ce0_01334ee0867d-process_discovery_process_hacker|Process Discovery - Process Hacker (powershell; windows)]]
- [[kb/atomic/tests/b4ca838d_d013_4461_bf2c_f7132617b409-process_discovery_pc_hunter|Process Discovery - PC Hunter (powershell; windows)]]
- [[kb/atomic/tests/b51239b4_0129_474f_a2b4_70f855b9f2c2-process_discovery_get_wmiobject|Process Discovery - get-wmiObject (powershell; windows)]]
- [[kb/atomic/tests/c5806a4f_62b8_4900_980b_c7ec004e9908-process_discovery_tasklist|Process Discovery - tasklist (command_prompt; windows)]]

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
- [[asyncrat|AsyncRAT (S1087)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[donut|Donut (S0695)]]
- [[empire|Empire (S0363)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[ironnetinjector|IronNetInjector (S0581)]]
- [[pcshare|PcShare (S1050)]]
- [[powersploit|PowerSploit (S0194)]]
- [[pupy|Pupy (S0192)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[tasklist|Tasklist (S0057)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

