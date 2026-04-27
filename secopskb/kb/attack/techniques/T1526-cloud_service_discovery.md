---
mitre_id: "T1526"
mitre_name: "Cloud Service Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e24fcba8-2557-4442-a139-1ee2f2e784db"
mitre_created: "2019-08-30T13:01:10.120Z"
mitre_modified: "2025-10-24T17:49:30.791Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1526/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Identity Provider"
  - "Office Suite"
  - "SaaS"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-CI"
  - "D3-RC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.

Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity.(Citation: Azure - Resource Manager API)(Citation: Azure AD Graph API)

For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services.(Citation: Azure - Stormspotter)(Citation: GitHub Pacu)

Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated services or evading identified defenses through [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]] or [[T1562-impair_defenses#^t1562008-disable-or-modify-cloud-logs|T1562.008: Disable or Modify Cloud Logs]].

## Workspace

- [[workspaces/attack/techniques/T1526-cloud_service_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1526-cloud_service_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/35b781cc_1a08_4a5a_80af_42fd7c315c6b-discovery_using_azurehound|Discovery Using AzureHound (high; azure / signinlogs)]]
- [[kb/sigma/rules/38646daa_e78f_4ace_9de0_55547b2d30da-pua_seatbelt_execution|PUA - Seatbelt Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/1e40bb1d_195e_401e_a86b_c192f55e005c-azure_dump_subscription_data_with_microburst|Azure - Dump Subscription Data with MicroBurst (powershell; iaas:azure)]]
- [[kb/atomic/tests/58f57c8f_db14_4e62_a4d3_5aaf556755d7-azure_enumerate_common_cloud_services|Azure - Enumerate common cloud services (powershell; iaas:azure)]]
- [[kb/atomic/tests/aa8b9bcc_46fa_4a59_9237_73c7b93a980c-aws_enumerate_common_cloud_services|AWS - Enumerate common cloud services (powershell; iaas:aws)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Tools
- [[aadinternals|AADInternals (S0677)]]
- [[pacu|Pacu (S1091)]]
- [[roadtools|ROADTools (S0684)]]


## Platforms

- IaaS
- Identity Provider
- Office Suite
- SaaS

