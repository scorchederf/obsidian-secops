---
id: T1495
name: Firmware Corruption
created: 2019-04-12 18:28:15.451000+00:00
modified: 2025-10-24 17:49:37.207000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[impact|Impact]]

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system.(Citation: Symantec Chernobyl W95.CIH) Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable.(Citation: dhs_threat_to_net_devices)(Citation: cisa_malware_orgs_ukraine) Depending on the device, this attack may also result in [Data Destruction](https://attack.mitre.org/techniques/T1485). 

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1046-boot_integrity|M1046: Boot Integrity]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- macOS
- Network Devices
- Windows

## Tools


