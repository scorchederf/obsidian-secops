---
mitre_id: "T1490"
mitre_name: "Inhibit System Recovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f5d8eed6-48a9-4cdf-a3d7-d1ffa99c3d2a"
mitre_created: "2019-04-02T13:54:43.136Z"
mitre_modified: "2025-10-24T17:49:37.297Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1490/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
d3fend_ids:
  - "D3-AVE"
  - "D3-CI"
  - "D3-RC"
  - "D3-RS"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery.(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) This may deny access to available backups and recovery options.

Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of [[T1485-data_destruction|T1485: Data Destruction]] and [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]].(Citation: Talos Olympic Destroyer 2018)(Citation: FireEye WannaCry 2017) Furthermore, adversaries may disable recovery notifications, then corrupt backups.(Citation: disable_notif_synology_ransom)

A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:

* `vssadmin.exe` can be used to delete all volume shadow copies on a system - `vssadmin.exe delete shadows /all /quiet`
* [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]] can be used to delete volume shadow copies - `wmic shadowcopy delete`
* `wbadmin.exe` can be used to delete the Windows Backup Catalog - `wbadmin.exe delete catalog -quiet`
* `bcdedit.exe` can be used to disable automatic Windows recovery features by modifying boot configuration data - `bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no`
* `REAgentC.exe` can be used to disable Windows Recovery Environment (WinRE) repair/recovery options of an infected system
* `diskshadow.exe` can be used to delete all volume shadow copies on a system - `diskshadow delete shadows all` (Citation: Diskshadow) (Citation: Crytox Ransomware)

On network devices, adversaries may leverage [[T1561-disk_wipe|T1561: Disk Wipe]] to delete backup firmware images and reformat the file system, then [[T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]] to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.

On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]], preventing them from being leveraged as backups (e.g., via ` vim-cmd vmsvc/snapshot.removeall`).(Citation: Cybereason)

Adversaries may also delete “online” backups that are connected to their network – whether via network storage media or through folders that sync to cloud services.(Citation: ZDNet Ransomware Backups 2020) In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios.(Citation: Dark Reading Code Spaces Cyber Attack)(Citation: Rhino Security Labs AWS S3 Ransomware)

## Workspace

- [[workspaces/attack/techniques/T1490-inhibit_system_recovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1490-inhibit_system_recovery-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- Containers
- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows

