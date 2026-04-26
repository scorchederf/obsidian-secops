---
mitre_id: "T1648"
mitre_name: "Serverless Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e848506b-8484-4410-8017-3d235a52f5b3"
mitre_created: "2022-05-27T13:19:51.112Z"
mitre_modified: "2025-04-15T19:59:17.861Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1648/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "SaaS"
  - "IaaS"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may abuse serverless computing, integration, and automation services to execute arbitrary code in cloud environments. Many cloud providers offer a variety of serverless resources, including compute engines, application integration services, and web servers. 

Adversaries may abuse these resources in various ways as a means of executing arbitrary commands. For example, adversaries may use serverless functions to execute malicious code, such as crypto-mining malware (i.e. [[T1496-resource_hijacking|T1496: Resource Hijacking]]).(Citation: Cado Security Denonia) Adversaries may also create functions that enable further compromise of the cloud environment. For example, an adversary may use the `IAM:PassRole` permission in AWS or the `iam.serviceAccounts.actAs` permission in Google Cloud to add [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]] to a serverless cloud function, which may then be able to perform actions the original user cannot.(Citation: Rhino Security Labs AWS Privilege Escalation)(Citation: Rhingo Security Labs GCP Privilege Escalation)

Serverless functions can also be invoked in response to cloud events (i.e. [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]), potentially enabling persistent execution over time. For example, in AWS environments, an adversary may create a Lambda function that automatically adds [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]] to a user and a corresponding CloudWatch events rule that invokes that function whenever a new user is created.(Citation: Backdooring an AWS account) This is also possible in many cloud-based office application suites. For example, in Microsoft 365 environments, an adversary may create a Power Automate workflow that forwards all emails a user receives or creates anonymous sharing links whenever a user is granted access to a document in SharePoint.(Citation: Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001) In Google Workspace environments, they may instead create an Apps Script that exfiltrates a user's data when they open a file.(Citation: Cloud Hack Tricks GWS Apps Script)(Citation: OWN-CERT Google App Script 2024)

## Workspace

- [[workspaces/attack/techniques/T1648-serverless_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1648-serverless_execution-note]]

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1036-account_use_policies|M1036: Account Use Policies]]

## Tools

- [[pacu|Pacu (S1091)]]

## Platforms

- SaaS
- IaaS
- Office Suite

