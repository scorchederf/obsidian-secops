---
mitre_id: "T1495"
mitre_name: "Firmware Corruption"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f5bb433e-bdf6-4781-84bc-35e97e43be89"
mitre_created: "2019-04-12T18:28:15.451Z"
mitre_modified: "2025-10-24T17:49:37.207Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1495/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system.(Citation: Symantec Chernobyl W95.CIH) Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable.(Citation: dhs_threat_to_net_devices)(Citation: cisa_malware_orgs_ukraine) Depending on the device, this attack may also result in [[T1485-data_destruction|T1485: Data Destruction]]. 

## Workspace

- [[workspaces/attack/techniques/T1495-firmware_corruption-note|Open workspace note]]

![[workspaces/attack/techniques/T1495-firmware_corruption-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1046-boot_integrity|M1046: Boot Integrity]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- macOS
- Network Devices
- Windows

