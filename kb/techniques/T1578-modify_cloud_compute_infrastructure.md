---
mitre_id: "T1578"
mitre_name: "Modify Cloud Compute Infrastructure"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--144e007b-e638-431d-a894-45d90c54ab90"
mitre_created: "2019-08-30T18:03:05.864Z"
mitre_modified: "2025-10-24T17:48:26.284Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1578/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0005"
---

# T1578: Modify Cloud Compute Infrastructure

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.(Citation: Mandiant M-Trends 2020)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Subtechniques

### T1578.001: Create Snapshot

^t1578001-create-snapshot

An adversary may create a snapshot or data backup within a cloud account to evade defenses. A snapshot is a point-in-time copy of an existing cloud compute component such as a virtual machine (VM), virtual hard drive, or volume. An adversary may leverage permissions to create a snapshot in order to bypass restrictions that prevent access to existing compute service infrastructure, unlike in [[T1578-modify_cloud_compute_infrastructure#^t1578004-revert-cloud-instance|T1578.004: Revert Cloud Instance]] where an adversary may revert to a snapshot to evade detection and remove evidence of their presence.

An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]], mount one or more created snapshots to that instance, and then apply a policy that allows the adversary access to the created instance, such as a firewall policy that allows them inbound and outbound SSH access.(Citation: Mandiant M-Trends 2020)

### T1578.002: Create Cloud Instance

^t1578002-create-cloud-instance

An adversary may create a new instance or virtual machine (VM) within the compute service of a cloud account to evade defenses. Creating a new instance may allow an adversary to bypass firewall rules and permissions that exist on instances currently residing within an account. An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578001-create-snapshot|T1578.001: Create Snapshot]] of one or more volumes in an account, create a new instance, mount the snapshots, and then apply a less restrictive security policy to collect [[T1005-data_from_local_system|T1005: Data from Local System]] or for [[T1074-data_staged#^t1074002-remote-data-staging|T1074.002: Remote Data Staging]].(Citation: Mandiant M-Trends 2020)

Creating a new instance may also allow an adversary to carry out malicious activity within an environment without affecting the execution of current running instances.

### T1578.003: Delete Cloud Instance

^t1578003-delete-cloud-instance

An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts and other evidence of suspicious behavior if the instance is not recoverable.

An adversary may also [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]] and later terminate the instance after achieving their objectives.(Citation: Mandiant M-Trends 2020)

### T1578.004: Revert Cloud Instance

^t1578004-revert-cloud-instance

An adversary may revert changes made to a cloud instance after they have performed malicious activities in attempt to evade detection and remove evidence of their presence. In highly virtualized environments, such as cloud-based infrastructure, this may be accomplished by restoring virtual machine (VM) or data storage snapshots through the cloud management dashboard or cloud APIs.

Another variation of this technique is to utilize temporary storage attached to the compute instance. Most cloud providers provide various types of storage including persistent, local, and/or ephemeral, with the ephemeral types often reset upon stop/restart of the VM.(Citation: Tech Republic - Restore AWS Snapshots)(Citation: Google - Restore Cloud Snapshot)

### T1578.005: Modify Cloud Compute Configurations

^t1578005-modify-cloud-compute-configurations

Adversaries may modify settings that directly affect the size, locations, and resources available to cloud compute infrastructure in order to evade defenses. These settings may include service quotas, subscription associations, tenant-wide policies, or other configurations that impact available compute. Such modifications may allow adversaries to abuse the victim’s compute resources to achieve their goals, potentially without affecting the execution of running instances and/or revealing their activities to the victim.

For example, cloud providers often limit customer usage of compute resources via quotas. Customers may request adjustments to these quotas to support increased computing needs, though these adjustments may require approval from the cloud provider. Adversaries who compromise a cloud environment may similarly request quota adjustments in order to support their activities, such as enabling additional [[T1496-resource_hijacking|T1496: Resource Hijacking]] without raising suspicion by using up a victim’s entire quota.(Citation: Microsoft Cryptojacking 2023) Adversaries may also increase allowed resource usage by modifying any tenant-wide policies that limit the sizes of deployed virtual machines.(Citation: Microsoft Azure Policy)

Adversaries may also modify settings that affect where cloud resources can be deployed, such as enabling [[T1535-unused_unsupported_cloud_regions|T1535: Unused/Unsupported Cloud Regions]]. 

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- IaaS

