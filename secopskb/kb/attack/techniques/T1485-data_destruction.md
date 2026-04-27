---
mitre_id: "T1485"
mitre_name: "Data Destruction"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d45a3d09-b3cf-48f4-9f0f-f521ee5cb05c"
mitre_created: "2019-03-14T18:47:17.701Z"
mitre_modified: "2025-10-24T17:49:27.149Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1485/"
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
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as `del` and `rm` often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]] and [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]] because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic Destroyer 2018).

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction - Threat Post)(Citation: DOJ  - Cisco Insider) Similarly, they may delete virtual machines from on-prem virtualized environments.

## Workspace

- [[workspaces/attack/techniques/T1485-data_destruction-note|Open workspace note]]

![[workspaces/attack/techniques/T1485-data_destruction-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/a4824fca_976f_4964_b334_0621379e84c4-potential_file_overwrite_via_sysinternals_sdelete|Potential File Overwrite Via Sysinternals SDelete (high; windows / process_creation)]]
- [[kb/sigma/rules/add64136_62e5_48ea_807e_88638d02df1e-fsutil_suspicious_invocation|Fsutil Suspicious Invocation (high; windows / process_creation)]]
- [[kb/sigma/rules/c1d867fe_8d95_4487_aab4_e53f2d339f90-renamed_sysinternals_sdelete_execution|Renamed Sysinternals Sdelete Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/1207ddff_f25b_41b3_aa0e_7c26d2b546d1-esxi_delete_vm_snapshots|ESXi - Delete VM Snapshots (command_prompt; windows)]]
- [[kb/atomic/tests/321fd25e_0007_417f_adec_33232252be19-overwrite_deleted_data_on_c_drive|Overwrite deleted data on C drive (command_prompt; windows)]]
- [[kb/atomic/tests/38deee99_fd65_4031_bec8_bfa4f9f26146-freebsd_macos_linux_overwrite_file_with_dd|FreeBSD/macOS/Linux - Overwrite file with DD (sh; linux, macos)]]
- [[kb/atomic/tests/476419b5_aebf_4366_a131_ae3e8dae5fc2-windows_overwrite_file_with_sysinternals_sdelete|Windows - Overwrite file with SysInternals SDelete (powershell; windows)]]
- [[kb/atomic/tests/4ac71389_40f4_448a_b73f_754346b3f928-gcp_delete_bucket|GCP - Delete Bucket (sh; iaas:gcp)]]

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-cipher_exe|Cipher.exe (Tamper)]]
- [[kb/lolbas/entries/osbinaries-fsutil_exe|Fsutil.exe (Tamper, Execute)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Subtechniques

### T1485.001: Lifecycle-Triggered Deletion

^t1485001-lifecycle-triggered-deletion

Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within.  

Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time.(Citation: AWS Storage Lifecycles)(Citation: GCP Storage Lifecycles)(Citation: Azure Storage Lifecycles) If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. 

For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day.(Citation: Palo Alto Cloud Ransomware)(Citation: Halcyon AWS Ransomware 2025) In addition to destroying data for purposes of extortion and [[T1657-financial_theft|T1657: Financial Theft]], adversaries may also perform this action on buckets storing cloud logs for [[T1070-indicator_removal|T1070: Indicator Removal]].(Citation: Datadog S3 Lifecycle CloudTrail Logs)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1053-data_backup|M1053: Data Backup]]

## Tools
- [[rawdisk|RawDisk (S0364)]]
- [[sdelete|SDelete (S0195)]]


## Platforms

- Containers
- ESXi
- IaaS
- Linux
- macOS
- Windows

