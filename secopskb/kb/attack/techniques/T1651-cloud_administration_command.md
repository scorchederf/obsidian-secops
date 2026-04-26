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
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [[T1199-trusted_relationship|T1199: Trusted Relationship]] to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)

## Workspace

- [[workspaces/attack/techniques/T1651-cloud_administration_command-note|Open workspace note]]

![[workspaces/attack/techniques/T1651-cloud_administration_command-note]]

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Tools

- [[aadinternals|AADInternals (S0677)]]
- [[pacu|Pacu (S1091)]]

## Platforms

- IaaS

