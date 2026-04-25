---
mitre_id: "T1666"
mitre_name: "Modify Cloud Resource Hierarchy"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0ce73446-8722-4086-9d43-514f1d0f669e"
mitre_created: "2024-09-25T14:16:19.234Z"
mitre_modified: "2025-04-15T22:49:45.874Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1666/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-CI"
  - "D3-RC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses.  

IaaS environments often group resources into a hierarchy, enabling improved resource management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example, in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple subscriptions can be grouped under a single management group.(Citation: AWS Organizations)(Citation: Microsoft Azure Resources)

Adversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments, an adversary who has gained access to a Global Administrator account may create new subscriptions in which to deploy resources. They may also engage in subscription hijacking by transferring an existing pay-as-you-go subscription from a victim tenant to an adversary-controlled tenant. This will allow the adversary to use the victim’s compute resources without generating logs on the victim tenant.(Citation: Microsoft Peach Sandstorm 2023)(Citation: Microsoft Subscription Hijacking 2022)

In AWS environments, adversaries with appropriate permissions in a given account may call the `LeaveOrganization` API, causing the account to be severed from the AWS Organization to which it was tied and removing any Service Control Policies, guardrails, or restrictions imposed upon it by its former Organization. Alternatively, adversaries may call the `CreateAccount` API in order to create a new account within an AWS Organization. This account will use the same payment methods registered to the payment account but may not be subject to existing detections or Service Control Policies.(Citation: AWS RE:Inforce Threat Detection 2024)

## Workspace

- [[workspaces/attack/techniques/T1666-modify_cloud_resource_hierarchy-note|Open workspace note]]

![[workspaces/attack/techniques/T1666-modify_cloud_resource_hierarchy-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1047-audit|M1047: Audit]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- IaaS

