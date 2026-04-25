---
mitre_id: "T1619"
mitre_name: "Cloud Storage Object Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--8565825b-21c8-4518-b75e-cbc4c717a156"
mitre_created: "2021-10-01T17:58:26.445Z"
mitre_modified: "2025-10-24T17:49:03.853Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1619/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-DENCR"
  - "D3-DKE"
  - "D3-DKF"
  - "D3-HBWP"
  - "D3-HCI"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] on a local host, after identifying available storage services (i.e. [[T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Workspace

- [[notes/attack/techniques/T1619-cloud_storage_object_discovery-note|Open workspace note]]

![[notes/attack/techniques/T1619-cloud_storage_object_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DENCR-disk_encryption|D3-DENCR: Disk Encryption]]
- [[D3-DKE-disk_erasure|D3-DKE: Disk Erasure]]
- [[D3-DKF-disk_formatting|D3-DKF: Disk Formatting]]
- [[D3-HBWP-hardware-based_write_protection|D3-HBWP: Hardware-based Write Protection]]
- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Tools

- [[peirates|Peirates]]
- [[pacu|Pacu]]

## Platforms

- IaaS

