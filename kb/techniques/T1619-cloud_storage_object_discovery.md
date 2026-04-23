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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0007"
---

# T1619: Cloud Storage Object Discovery

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]] on a local host, after identifying available storage services (i.e. [[T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Tools

- [[peirates|Peirates]]
- [[pacu|Pacu]]

## Platforms

- IaaS

