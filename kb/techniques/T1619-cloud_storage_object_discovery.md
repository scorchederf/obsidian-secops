---
id: T1619
name: Cloud Storage Object Discovery
created: 2021-10-01 17:58:26.445000+00:00
modified: 2025-10-24 17:49:03.853000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Platforms

- IaaS

