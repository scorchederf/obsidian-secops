---
id: T1485
name: Data Destruction
created: 2019-03-14 18:47:17.701000+00:00
modified: 2025-10-24 17:49:27.149000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[impact|Impact]]

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as <code>del</code> and <code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from [Disk Content Wipe](https://attack.mitre.org/techniques/T1561/001) and [Disk Structure Wipe](https://attack.mitre.org/techniques/T1561/002) because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable.(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3 2018) In some cases politically oriented image files have been used to overwrite data.(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like [Valid Accounts](https://attack.mitre.org/techniques/T1078), [OS Credential Dumping](https://attack.mitre.org/techniques/T1003), and [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002).(Citation: Symantec Shamoon 2012)(Citation: FireEye Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Talos Olympic Destroyer 2018).

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers.(Citation: Data Destruction - Threat Post)(Citation: DOJ  - Cisco Insider) Similarly, they may delete virtual machines from on-prem virtualized environments.

## Subtechniques

### T1485.001: Lifecycle-Triggered Deletion
^t1485001-lifecycle-triggered-deletion

**Parent Technique**
- [[T1485-data_destruction|T1485: Data Destruction]]

**Tactic**
- [[impact|Impact]]

Adversaries may modify the lifecycle policies of a cloud storage bucket to destroy all objects stored within.  

Cloud storage buckets often allow users to set lifecycle policies to automate the migration, archival, or deletion of objects after a set period of time.(Citation: AWS Storage Lifecycles)(Citation: GCP Storage Lifecycles)(Citation: Azure Storage Lifecycles) If a threat actor has sufficient permissions to modify these policies, they may be able to delete all objects at once. 

For example, in AWS environments, an adversary with the `PutLifecycleConfiguration` permission may use the `PutBucketLifecycle` API call to apply a lifecycle policy to an S3 bucket that deletes all objects in the bucket after one day.(Citation: Palo Alto Cloud Ransomware)(Citation: Halcyon AWS Ransomware 2025) In addition to destroying data for purposes of extortion and [Financial Theft](https://attack.mitre.org/techniques/T1657), adversaries may also perform this action on buckets storing cloud logs for [Indicator Removal](https://attack.mitre.org/techniques/T1070).(Citation: Datadog S3 Lifecycle CloudTrail Logs)

#### Properties

- id: T1485.001
- name: Lifecycle-Triggered Deletion
- created: 2024-09-25 13:16:14.166000+00:00
- modified: 2025-04-15 19:58:06.787000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- Containers
- ESXi
- IaaS
- Linux
- macOS
- Windows

## Tools

- [[rawdisk|RawDisk]]
- [[sdelete|SDelete]]

