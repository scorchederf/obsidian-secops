---
id: T1651
name: Cloud Administration Command
created: 2023-03-13 15:26:11.741000+00:00
modified: 2025-04-15 19:59:13.081000+00:00
type: attack-pattern
x_mitre_version: 2.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Run Command)(Citation: Microsoft Run Command)

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a [Trusted Relationship](https://attack.mitre.org/techniques/T1199) to execute commands in connected virtual machines.(Citation: MSTIC Nobelium Oct 2021)

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]

## Platforms

- IaaS

