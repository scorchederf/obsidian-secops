---
mitre_id: "DC0099"
mitre_name: "Group Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--8e44412e-3238-4d64-8878-4f11e27784fe"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:14:39.499Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Extracting group lists from identity systems identifies permissions, roles, or configurations. Adversaries may exploit high-privilege groups or misconfigurations. Examples:

- AWS CLI: `aws iam list-groups`
- PowerShell: `Get-ADGroup -Filter *`
- (Saas) Google Workspace: Admin SDK Directory API
- Azure: `Get-AzureADGroup`
- Microsoft 365:  Graph API `GET https://graph.microsoft.com/v1.0/groups`

*Data Collection Measures:*

- Cloud Logging: Enable AWS CloudTrail, Azure Activity Logs, and Google Workspace Admin Logs for group-related actions.
- Directory Monitoring: Track logs like AD Event ID 4662 (object operations).
- API Monitoring: Log API activity like AWS IAM queries.
- SaaS Monitoring: Use platform logs (e.g., Office 365 Unified Audit Logs).
- SIEM Integration: Centralize group query tracking.

## Workspace

- [[workspaces/attack/data-components/DC0099-group_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0099-group_enumeration-note]]

