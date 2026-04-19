---
id: T1005
name: Data from Local System
created: 2017-05-31 21:30:20.537000+00:00
modified: 2025-10-24 17:48:40.839000+00:00
type: attack-pattern
x_mitre_version: 1.8
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as [cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008), which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.


## Properties

- id: T1005
- name: Data from Local System
- created: 2017-05-31 21:30:20.537000+00:00
- modified: 2025-10-24 17:48:40.839000+00:00
- type: attack-pattern
- x_mitre_version: 1.8
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[S0193-forfiles|S0193: Forfiles]]
- [[S0194-powersploit|S0194: PowerSploit]]
- [[S0250-koadic|S0250: Koadic]]
- [[S0262-quasarrat|S0262: QuasarRAT]]
- [[S0404-esentutl|S0404: esentutl]]
- [[S0500-mcmd|S0500: MCMD]]
- [[S0594-out1|S0594: Out1]]
- [[S0645-wevtutil|S0645: Wevtutil]]
- [[S1050-pcshare|S1050: PcShare]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]
- [[S1131-nppspy|S1131: NPPSPY]]

