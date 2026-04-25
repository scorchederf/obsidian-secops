---
mitre_id: "T1671"
mitre_name: "Cloud Application Integration"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c31aebd6-c9b5-420f-ba2a-5853bbf897fa"
mitre_created: "2025-03-20T22:21:59.326Z"
mitre_modified: "2025-04-15T19:59:05.283Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1671/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Office Suite"
  - "SaaS"
mitre_tactic_ids:
  - "TA0003"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends.(Citation: Push Security SaaS Persistence 2022)(Citation: SaaS Attacks GitHub Evil Twin Integrations)

OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks.  

Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account.(Citation: Wiz Midnight Blizzard 2024)(Citation: Microsoft Malicious OAuth Applications 2022)(Citation: Huntress Persistence Microsoft 365 Compromise 2024) In some cases, integrations may remain valid even after the original consenting user account is disabled.(Citation: Push Security Slack Persistence 2023) Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]s. Finally, they may enable persistent [[T1020-automated_exfiltration|T1020: Automated Exfiltration]] over time.(Citation: Synes Cyber Corner Malicious Azure Application 2023)

Creating or adding a new application may require the adversary to create a dedicated [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]] for the application and assign it [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]] – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal.(Citation: Microsoft Entra ID Service Principals)  

## Workspace

- [[notes/attack/techniques/T1671-cloud_application_integration-note|Open workspace note]]

![[notes/attack/techniques/T1671-cloud_application_integration-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## Mitigations

- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Office Suite
- SaaS

