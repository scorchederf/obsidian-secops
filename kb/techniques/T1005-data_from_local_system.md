---
mitre_id: "T1005"
mitre_name: "Data from Local System"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3c4a2599-71ee-4405-ba1e-0e28414b4bc5"
mitre_created: "2017-05-31T21:30:20.537Z"
mitre_modified: "2025-10-24T17:48:40.839Z"
mitre_version: "1.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1005/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
---

# T1005: Data from Local System

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]], such as [[cmd|cmd]] as well as a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]], which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries may also use [[T1119-automated_collection|T1119: Automated Collection]] on the local system.


## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools

- [[forfiles|Forfiles]]
- [[powersploit|PowerSploit]]
- [[koadic|Koadic]]
- [[quasarrat|QuasarRAT]]
- [[esentutl|esentutl]]
- [[mcmd|MCMD]]
- [[out1|Out1]]
- [[wevtutil|Wevtutil]]
- [[pcshare|PcShare]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[nppspy|NPPSPY]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

