---
id: T1578
name: Modify Cloud Compute Infrastructure
created: 2019-08-30 18:03:05.864000+00:00
modified: 2025-10-24 17:48:26.284000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Properties

- id: T1578
- name: Modify Cloud Compute Infrastructure
- created: 2019-08-30 18:03:05.864000+00:00
- modified: 2025-10-24 17:48:26.284000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1578.001: Create Snapshot

^t1578001-create-snapshot

**Parent Technique**
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

An adversary may create a snapshot or data backup within a cloud account to evade defenses. A snapshot is a point-in-time copy of an existing cloud compute component such as a virtual machine (VM), virtual hard drive, or volume. An adversary may leverage permissions to create a snapshot in order to bypass restrictions that prevent access to existing compute service infrastructure, unlike in [Revert Cloud Instance](https://attack.mitre.org/techniques/T1578/004) where an adversary may revert to a snapshot to evade detection and remove evidence of their presence.

An adversary may [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002), mount one or more created snapshots to that instance, and then apply a policy that allows the adversary access to the created instance, such as a firewall policy that allows them inbound and outbound SSH access.(Citation: Mandiant M-Trends 2020)

#### Properties

- id: T1578.001
- name: Create Snapshot
- created: 2020-06-09 15:33:13.563000+00:00
- modified: 2025-10-24 17:49:34.416000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1578.002: Create Cloud Instance

^t1578002-create-cloud-instance

**Parent Technique**
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may [Create Snapshot](https://attack.mitre.org/techniques/T1578/001) of one or more volumes in an account, create a new instance, mount the snapshots, and then apply a less restrictive security policy to collect [Data from Local System](https://attack.mitre.org/techniques/T1005) or for [Remote Data Staging](https://attack.mitre.org/techniques/T1074/002).(Citation: Mandiant M-Trends 2020)

Creating a new instance may also allow an adversary to carry out malicious activity within an environment without affecting the execution of current running instances.

#### Properties

- id: T1578.002
- name: Create Cloud Instance
- created: 2020-05-14 14:45:15.978000+00:00
- modified: 2025-10-24 17:49:24.804000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1578.003: Delete Cloud Instance

^t1578003-delete-cloud-instance

**Parent Technique**
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is not recoverable.

An adversary may also [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and later terminate the instance after achieving their objectives.(Citation: Mandiant M-Trends 2020)

#### Properties

- id: T1578.003
- name: Delete Cloud Instance
- created: 2020-06-16 17:23:06.508000+00:00
- modified: 2025-10-24 17:48:56.705000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1578.004: Revert Cloud Instance

^t1578004-revert-cloud-instance

**Parent Technique**
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)

#### Properties

- id: T1578.004
- name: Revert Cloud Instance
- created: 2020-06-16 18:42:20.734000+00:00
- modified: 2025-10-24 17:48:21.210000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1578.005: Modify Cloud Compute Configurations

^t1578005-modify-cloud-compute-configurations

**Parent Technique**
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]

**Tactic**
- [[defense_evasion|Defense Evasion]]

Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim.

For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider. Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities, such as enabling additional [Resource Hijacking](https://attack.mitre.org/techniques/T1496) without raising suspicion by using up a victim’s entire quota.(Citation: Microsoft Cryptojacking 2023) Adversaries may also increase allowed resource usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines.(Citation: Microsoft Azure Policy)

Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling [Unused/Unsupported Cloud Regions](https://attack.mitre.org/techniques/T1535). 

#### Properties

- id: T1578.005
- name: Modify Cloud Compute Configurations
- created: 2023-09-05 14:19:17.486000+00:00
- modified: 2025-04-15 22:49:17.012000+00:00
- type: attack-pattern
- x_mitre_version: 2.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- IaaS

