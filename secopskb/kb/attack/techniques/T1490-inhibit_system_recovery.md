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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

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

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2021-01-009-detecting_shadow_copy_deletion_or_resize|CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize]]
- [[kb/car/analytics/CAR-2021-05-003-bcdedit_failure_recovery_modification|CAR-2021-05-003: BCDEdit Failure Recovery Modification]]

### Sigma Rules

- [[kb/sigma/rules/1444443e_6757_43e4_9ea4_c8fc705f79a2-boot_configuration_tampering_via_bcdedit_exe|Boot Configuration Tampering Via Bcdedit.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/21ff4ca9_f13a_41ad_b828_0077b2af2e40-deletion_of_volume_shadow_copies_via_wmi_with_powershell|Deletion of Volume Shadow Copies via WMI with PowerShell (high; windows / process_creation)]]
- [[kb/sigma/rules/333cdbe8_27bb_4246_bf82_b41a0dca4b70-suspicious_volume_shadow_copy_vss_ps_dll_load|Suspicious Volume Shadow Copy VSS_PS.dll Load (high; windows / image_load)]]
- [[kb/sigma/rules/37774c23_25a1_4adb_bb6d_8bb9fd59c0f8-suspicious_volume_shadow_copy_vssapi_dll_load|Suspicious Volume Shadow Copy Vssapi.dll Load (high; windows / image_load)]]
- [[kb/sigma/rules/5de03871_5d46_4539_a82d_3aa992a69a83-registry_disable_system_restore|Registry Disable System Restore (high; windows / registry_set)]]
- [[kb/sigma/rules/639c9081_f482_47d3_a0bd_ddee3d4ecd76-all_backups_deleted_via_wbadmin_exe|All Backups Deleted Via Wbadmin.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/87df9ee1_5416_453a_8a08_e8d4a51e9ce1-delete_volume_shadow_copies_via_wmi_with_powershell|Delete Volume Shadow Copies Via WMI With PowerShell (high; windows / ps_classic_start)]]
- [[kb/sigma/rules/c1337eb8_921a_4b59_855b_4ba188ddcc42-deletion_of_volume_shadow_copies_via_wmi_with_powershell_ps_script|Deletion of Volume Shadow Copies via WMI with PowerShell - PS Script (high; windows / ps_script)]]
- [[kb/sigma/rules/c73124a7_3e89_44a3_bdc1_25fe4df754b1-copy_from_volumeshadowcopy_via_cmd_exe|Copy From VolumeShadowCopy Via Cmd.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/c947b146_0abc_4c87_9c64_b17e9d7274a2-shadow_copies_deletion_using_operating_systems_utilities|Shadow Copies Deletion Using Operating Systems Utilities (high; windows / process_creation)]]
- 1 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/1c68c68d_83a4_4981_974e_8993055fa034-windows_disable_the_sr_scheduled_task|Windows - Disable the SR scheduled task (command_prompt; windows)]]
- [[kb/atomic/tests/263ba6cb_ea2b_41c9_9d4e_b652dadd002c-windows_wbadmin_delete_windows_backup_catalog|Windows - wbadmin Delete Windows Backup Catalog (command_prompt; windows)]]
- [[kb/atomic/tests/39a295ca_7059_4a88_86f6_09556c1211e7-windows_delete_volume_shadow_copies_via_wmi_with_powershell|Windows - Delete Volume Shadow Copies via WMI with PowerShell (powershell; windows)]]
- [[kb/atomic/tests/42111a6f_7e7f_482c_9b1b_3cfd090b999c-windows_delete_volume_shadow_copies_via_diskshadow|Windows - Delete Volume Shadow Copies via Diskshadow (powershell; windows)]]
- [[kb/atomic/tests/43819286_91a9_4369_90ed_d31fb4da2c01-windows_delete_volume_shadow_copies|Windows - Delete Volume Shadow Copies (command_prompt; windows)]]
- [[kb/atomic/tests/584331dd_75bc_4c02_9e0b_17f5fd81c748-windows_wbadmin_delete_systemstatebackup|Windows - wbadmin Delete systemstatebackup (command_prompt; windows)]]
- [[kb/atomic/tests/66e647d1_8741_4e43_b7c1_334760c2047f-disable_system_restore_through_registry|Disable System Restore Through Registry (command_prompt; windows)]]
- [[kb/atomic/tests/6a3ff8dd_f49c_4272_a658_11c2fe58bd88-windows_delete_volume_shadow_copies_via_wmi|Windows - Delete Volume Shadow Copies via WMI (command_prompt; windows)]]
- [[kb/atomic/tests/6b1dbaf6_cc8a_4ea6_891f_6058569653bf-windows_delete_backup_files|Windows - Delete Backup Files (command_prompt; windows)]]
- [[kb/atomic/tests/a4420f93_5386_4290_b780_f4f66abc7070-modify_vss_service_permissions|Modify VSS Service Permissions (command_prompt; windows)]]
- 3 more in the generated source index

<!-- generated-detection-validation-end -->

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

