---
mitre_id: "T1538"
mitre_name: "Cloud Service Dashboard"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e49920b0-6c54-40c1-9571-73723653205f"
mitre_created: "2019-08-30T18:11:24.582Z"
mitre_modified: "2025-10-24T17:49:32.022Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1538/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "SaaS"
  - "Office Suite"
  - "Identity Provider"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports.(Citation: Google Command Center Dashboard)

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

## Workspace

- [[workspaces/attack/techniques/T1538-cloud_service_dashboard-note|Open workspace note]]

![[workspaces/attack/techniques/T1538-cloud_service_dashboard-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Platforms

- IaaS
- SaaS
- Office Suite
- Identity Provider

