---
mitre_id: "T1074"
mitre_name: "Data Staged"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7dd95ff6-712e-4056-9626-312ea4ab4c5e"
mitre_created: "2017-05-31T21:30:58.938Z"
mitre_modified: "2025-10-24T17:49:01.010Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1074/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-DNR"
  - "D3-FA"
  - "D3-FCA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-NRAM"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd (S0106)]] and bash may be used to copy data into a staging location.(Citation: PWC Cloud Hopper April 2017)

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]] and stage data in that instance.(Citation: Mandiant M-Trends 2020)

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

## Workspace

- [[workspaces/attack/techniques/T1074-data_staged-note|Open workspace note]]

![[workspaces/attack/techniques/T1074-data_staged-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FCA-file_creation_analysis|D3-FCA: File Creation Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Subtechniques

### T1074.001: Local Data Staging

^t1074001-local-data-staging

Adversaries may stage collected data in a central location or directory on the local system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd (S0106)]] and bash may be used to copy data into a staging location.

Adversaries may also stage collected data in various available formats/locations of a system, including local storage databases/repositories or the Windows Registry.(Citation: Prevailion DarkWatchman 2021)

### T1074.002: Remote Data Staging

^t1074002-remote-data-staging

Adversaries may stage data collected from multiple systems in a central location or directory on one system prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as [[T1560-archive_collected_data|T1560: Archive Collected Data]]. Interactive command shells may be used, and common functionality within [[cmd|cmd (S0106)]] and bash may be used to copy data into a staging location.

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may [[T1578-modify_cloud_compute_infrastructure#^t1578002-create-cloud-instance|T1578.002: Create Cloud Instance]] and stage data in that instance.(Citation: Mandiant M-Trends 2020)

By staging data on one system prior to Exfiltration, adversaries can minimize the number of connections made to their C2 server and better evade detection.

## Platforms

- Windows
- IaaS
- Linux
- macOS
- ESXi

