---
mitre_id: "T1119"
mitre_name: "Automated Collection"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--30208d3e-0d6b-43c8-883e-44462a514619"
mitre_created: "2017-05-31T21:31:27.985Z"
mitre_modified: "2025-10-24T17:48:35.995Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1119/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] and [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]] to identify and move files, as well as [[T1538-cloud_service_dashboard|T1538: Cloud Service Dashboard]] and [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]] to identify resources in cloud environments.

## Workspace

- [[workspaces/attack/techniques/T1119-automated_collection-note|Open workspace note]]

![[workspaces/attack/techniques/T1119-automated_collection-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]

## Mitigations

- [[M1029-remote_data_storage|M1029: Remote Data Storage]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Tools
- [[empire|Empire (S0363)]]
- [[mythic|Mythic (S0699)]]
- [[nppspy|NPPSPY (S1131)]]
- [[pacu|Pacu (S1091)]]
- [[poshc2|PoshC2 (S0378)]]
- [[roadtools|ROADTools (S0684)]]
- [[shimratreporter|ShimRatReporter (S0445)]]


## Platforms

- IaaS
- Linux
- macOS
- Office Suite
- SaaS
- Windows

