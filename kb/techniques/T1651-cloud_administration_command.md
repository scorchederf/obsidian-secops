---
mitre_id: "T1651"
mitre_name: "Cloud Administration Command"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d94b3ae9-8059-4989-8e9f-ea0f601f80a7"
mitre_created: "2023-03-13T15:26:11.741Z"
mitre_modified: "2025-04-15T19:59:13.081Z"
mitre_version: "2.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1651/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0002"
---

# T1651: Cloud Administration Command

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [[T1199-trusted_relationship|T1199: Trusted Relationship]] to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Tools

- [[aadinternals|AADInternals]]
- [[pacu|Pacu]]

## Platforms

- IaaS

