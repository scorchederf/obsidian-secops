---
mitre_id: "T1082"
mitre_name: "System Information Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1"
mitre_created: "2017-05-31T21:31:04.307Z"
mitre_modified: "2025-10-24T17:48:38.277Z"
mitre_version: "3.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1082/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-DE"
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

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [[T1680-local_storage_discovery|T1680: Local Storage Discovery]] which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as [[systeminfo|Systeminfo (S0096)]] can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather detailed system information (e.g. `show version`).(Citation: US-CERT-TA18-106A) On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: Varonis)

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.(Citation: Amazon Describe Instance)(Citation: Google Instances Resource)(Citation: Microsoft Virutal Machine API)

[[T1082-system_information_discovery|T1082: System Information Discovery]] combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.(Citation: OSX.FairyTale)(Citation: 20 macOS Common Tools and Techniques) 

## Workspace

- [[workspaces/attack/techniques/T1082-system_information_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1082-system_information_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools

- [[systeminfo|Systeminfo (S0096)]]
- [[dsquery|dsquery (S0105)]]
- [[cmd|cmd (S0106)]]
- [[pupy|Pupy (S0192)]]
- [[koadic|Koadic (S0250)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[empire|Empire (S0363)]]
- [[poshc2|PoshC2 (S0378)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[covenant|Covenant (S1155)]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows

