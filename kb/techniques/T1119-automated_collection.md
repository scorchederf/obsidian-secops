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
build_date: "2026-04-23 20:16:46"
build_source: "script"
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
---

# T1119: Automated Collection

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]] to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals. 

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) 

This functionality could also be built into remote access tools. 

This technique may incorporate use of other techniques such as [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] and [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]] to identify and move files, as well as [[T1538-cloud_service_dashboard|T1538: Cloud Service Dashboard]] and [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]] to identify resources in cloud environments.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Mitigations

- [[M1029-remote_data_storage|M1029: Remote Data Storage]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Tools

- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[shimratreporter|ShimRatReporter]]
- [[roadtools|ROADTools]]
- [[mythic|Mythic]]
- [[pacu|Pacu]]
- [[nppspy|NPPSPY]]

## Platforms

- IaaS
- Linux
- macOS
- Office Suite
- SaaS
- Windows

