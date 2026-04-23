---
mitre_id: "T1537"
mitre_name: "Transfer Data to Cloud Account"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d4bdbdea-eaec-4071-b4f9-5105e12ea4b6"
mitre_created: "2019-08-30T13:03:04.038Z"
mitre_modified: "2025-10-24T17:49:27.409Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1537/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Office Suite"
  - "SaaS"
mitre_tactic_ids:
  - "TA0010"
---

# T1537: Transfer Data to Cloud Account

Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups of cloud environments, to another cloud account they control on the same service.

A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces.(Citation: TLDRSec AWS Attacks)

Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI.(Citation: Microsoft Azure Storage Shared Access Signature)

Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts.(Citation: DOJ GRU Indictment Jul 2018) 

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1054-software_configuration|M1054: Software Configuration]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- IaaS
- Office Suite
- SaaS

