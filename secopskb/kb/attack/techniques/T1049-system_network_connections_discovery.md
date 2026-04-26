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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network. 

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate.(Citation: Amazon AWS VPC Guide)(Citation: Microsoft Azure Virtual Network Overview)(Citation: Google VPC Overview) Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include [[netstat|netstat (S0104)]], "net use," and "net session" with [[net|Net (S0039)]]. In Mac and Linux, [[netstat|netstat (S0104)]] and `lsof` can be used to list current connections. `who -a` and `w` can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] may be used (e.g. `show ip sockets`, `show tcp brief`).(Citation: US-CERT-TA18-106A) On ESXi servers, the command `esxi network ip connection list` can be used to list active network connections.(Citation: Sygnia ESXi Ransomware 2025)

## Workspace

- [[workspaces/attack/techniques/T1049-system_network_connections_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1049-system_network_connections_discovery-note]]

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

