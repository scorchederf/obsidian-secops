---
mitre_id: "T1561"
mitre_name: "Disk Wipe"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1988cc35-ced8-4dad-b2d1-7628488fa967"
mitre_created: "2020-02-20T22:02:20.372Z"
mitre_modified: "2025-10-24T17:48:27.697Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1561/"
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
  - "Network Devices"
mitre_tactic_ids:
  - "TA0040"
d3fend_ids:
  - "D3-DKP"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: Novetta Blockbuster Destructive Malware)

On network devices, adversaries may wipe configuration files and other data from the device using [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `erase`.(Citation: erase_cmd_cisco)

## Workspace

- [[workspaces/attack/techniques/T1561-disk_wipe-note|Open workspace note]]

![[workspaces/attack/techniques/T1561-disk_wipe-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## D3FEND

- [[D3-DKP-disk_partitioning|D3-DKP: Disk Partitioning]]

## Subtechniques

### T1561.001: Disk Content Wipe

^t1561001-disk-content-wipe

Adversaries may erase the contents of storage devices on specific systems or in large numbers in a network to interrupt availability to system and network resources.

Adversaries may partially or completely overwrite the contents of a storage device rendering the data irrecoverable through the storage interface.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware)(Citation: DOJ Lazarus Sony 2018) Instead of wiping specific disk structures or files, adversaries with destructive intent may wipe arbitrary portions of disk content. To wipe disk content, adversaries may acquire direct access to the hard drive in order to overwrite arbitrarily sized portions of disk with random data.(Citation: Novetta Blockbuster Destructive Malware) Adversaries have also been observed leveraging third-party drivers like [[rawdisk|RawDisk (S0364)]] to directly access disk content.(Citation: Novetta Blockbuster)(Citation: Novetta Blockbuster Destructive Malware) This behavior is distinct from [[T1485-data_destruction|T1485: Data Destruction]] because sections of the disk are erased instead of individual files.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disk content may have worm-like features to propagate across a network by leveraging additional techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: Novetta Blockbuster Destructive Malware)

### T1561.002: Disk Structure Wipe

^t1561002-disk-structure-wipe

Adversaries may corrupt or wipe the disk data structures on a hard drive necessary to boot a system; targeting specific critical systems or in large numbers in a network to interrupt availability to system and network resources. 

Adversaries may attempt to render the system unable to boot by overwriting critical data located in structures such as the master boot record (MBR) or partition table.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) The data contained in disk structures may include the initial executable code for loading an operating system or the location of the file system partitions on disk. If this information is not present, the computer will not be able to load an operating system during the boot process, leaving the computer unavailable. [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]] may be performed in isolation, or along with [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]] if all sectors of a disk are wiped.

On a network devices, adversaries may reformat the file system using [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `format`.(Citation: format_cmd_cisco)

To maximize impact on the target organization, malware designed for destroying disk structures may have worm-like features to propagate across a network by leveraging other techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

## Mitigations

- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- Linux
- macOS
- Windows
- Network Devices

