---
id: T1538
name: Cloud Service Dashboard
created: 2019-08-30 18:11:24.582000+00:00
modified: 2025-10-24 17:49:32.022000+00:00
type: attack-pattern
x_mitre_version: 1.5
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Properties

- id: T1538
- name: Cloud Service Dashboard
- created: 2019-08-30 18:11:24.582000+00:00
- modified: 2025-10-24 17:49:32.022000+00:00
- type: attack-pattern
- x_mitre_version: 1.5
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Platforms

- IaaS
- SaaS
- Office Suite
- Identity Provider

