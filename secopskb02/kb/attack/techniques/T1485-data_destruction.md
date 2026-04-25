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
build_date: "2026-04-25 20:43:29"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as `del` and `rm` often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]] and [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]] because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic Destroyer 2018).

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction - Threat Post)(Citation: DOJ  - Cisco Insider) Similarly, they may delete virtual machines from on-prem virtualized environments.

## Workspace

- [[workspaces/attack/techniques/T1485-data_destruction-note|Open workspace note]]

![[workspaces/attack/techniques/T1485-data_destruction-note]]

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

- [[sdelete|SDelete (S0195)]]
- [[rawdisk|RawDisk (S0364)]]

## Platforms

- Containers
- ESXi
- IaaS
- Linux
- macOS
- Windows

