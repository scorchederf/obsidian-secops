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
build_date: "2026-04-25 20:43:29"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from [[T1057-process_discovery|T1057: Process Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

In Windows environments, adversaries could obtain details on running processes using the [[tasklist|Tasklist (S0057)]] utility via [[cmd|cmd (S0106)]] or `Get-Process` via [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]. Information about processes can also be extracted from the output of [[T1106-native_api|T1106: Native API]] calls such as `CreateToolhelp32Snapshot`. In Mac and Linux, this is accomplished with the `ps` command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.(Citation: Sygnia ESXi Ransomware 2025)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

On network devices, [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `show processes` can be used to display current running processes.(Citation: US-CERT-TA18-106A)(Citation: show_processes_cisco_cmd)

## Workspace

- [[workspaces/attack/techniques/T1057-process_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1057-process_discovery-note]]

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

- [[tasklist|Tasklist (S0057)]]
- [[pupy|Pupy (S0192)]]
- [[powersploit|PowerSploit (S0194)]]
- [[empire|Empire (S0363)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[ironnetinjector|IronNetInjector (S0581)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[donut|Donut (S0695)]]
- [[pcshare|PcShare (S1050)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[asyncrat|AsyncRAT (S1087)]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

