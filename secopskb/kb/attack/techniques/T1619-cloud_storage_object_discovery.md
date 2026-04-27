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
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] on a local host, after identifying available storage services (i.e. [[T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Workspace

- [[workspaces/attack/techniques/T1619-cloud_storage_object_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1619-cloud_storage_object_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/070322a4_2c60_4c50_8ffb_c450a34fe7bf-azure_enumerate_storage_account_objects_via_shared_key_authorization_using_azure_cli|Azure - Enumerate Storage Account Objects via Shared Key authorization using Azure CLI (powershell; iaas:azure)]]
- [[kb/atomic/tests/146af1f1_b74e_4aa7_9895_505eb559b4b0-azure_scan_for_anonymous_access_to_azure_storage_powershell|Azure - Scan for Anonymous Access to Azure Storage (Powershell) (powershell; iaas:azure)]]
- [[kb/atomic/tests/3c7094f8_71ec_4917_aeb8_a633d7ec4ef5-aws_s3_enumeration|AWS S3 Enumeration (sh; iaas:aws)]]
- [[kb/atomic/tests/3dab4bcc_667f_4459_aea7_4162dd2d6590-azure_enumerate_azure_blobs_with_microburst|Azure - Enumerate Azure Blobs with MicroBurst (powershell; iaas:azure)]]

<!-- generated-detection-validation-end -->

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
- [[pacu|Pacu (S1091)]]
- [[peirates|Peirates (S0683)]]


## Platforms

- IaaS

