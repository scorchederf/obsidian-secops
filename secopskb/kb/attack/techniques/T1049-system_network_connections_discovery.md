---
mitre_id: "T1049"
mitre_name: "System Network Connections Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7e150503-88e7-4861-866b-ff1ac82c4475"
mitre_created: "2017-05-31T21:30:45.139Z"
mitre_modified: "2025-10-24T17:49:01.094Z"
mitre_version: "2.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1049/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "ESXi"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. 

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon AWS VPC Guide)(Citation: Microsoft Azure Virtual Network Overview)(Citation: Google VPC Overview) Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include [[netstat|netstat (S0104)]], "net use," and "net session" with [[net|Net (S0039)]]. In Mac and Linux, [[netstat|netstat (S0104)]] and `lsof` can be used to list current connections. `who -a` and `w` can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] may be used (e.g. `show ip sockets`, `show tcp brief`).(Citation: US-CERT-TA18-106A) On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.(Citation: Sygnia ESXi Ransomware 2025)

## Workspace

- [[workspaces/attack/techniques/T1049-system_network_connections_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1049-system_network_connections_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

### Sigma Rules

- [[kb/sigma/rules/b2317cfa_4a47_4ead_b3ff_297438c0bc2d-hacktool_sharpview_execution|HackTool - SharpView Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0940a971_809a_48f1_9c4d_b1d785e96ee5-system_network_connections_discovery|System Network Connections Discovery (command_prompt; windows)]]
- [[kb/atomic/tests/96f974bb_a0da_4d87_a744_ff33e73367e9-system_discovery_using_sharpview|System Discovery using SharpView (powershell; windows)]]
- [[kb/atomic/tests/997bb0a6_421e_40c7_b5d2_0f493904ef9b-system_network_connections_discovery_via_sockstat_linux_freebsd|System Network Connections Discovery via sockstat (Linux, FreeBSD) (sh; linux)]]
- [[kb/atomic/tests/9ae28d3f_190f_4fa0_b023_c7bd3e0eabf2-system_network_connections_discovery_freebsd_linux_macos|System Network Connections Discovery FreeBSD, Linux & MacOS (sh; linux, macos)]]
- [[kb/atomic/tests/b52c8233_8f71_4bd7_9928_49fec8215cf5-system_network_connections_discovery_via_powershell_process_mapping|System Network Connections Discovery via PowerShell (Process Mapping) (powershell; windows)]]
- [[kb/atomic/tests/bcf05343_ef1d_4052_8a27_b00c9be42b9f-system_network_connections_discovery_via_ss_or_lsof_linux_macos|System Network Connections Discovery via ss or lsof (Linux/MacOS) (bash; linux, macos)]]
- [[kb/atomic/tests/f069f0f1_baad_4831_aa2b_eddac4baac4a-system_network_connections_discovery_with_powershell|System Network Connections Discovery with PowerShell (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[frp|FRP (S1144)]]
- [[nbtstat|nbtstat (S0102)]]
- [[netstat|netstat (S0104)]]
- [[net|Net (S0039)]]
- [[pacu|Pacu (S1091)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- Windows
- IaaS
- Linux
- macOS
- Network Devices
- ESXi

