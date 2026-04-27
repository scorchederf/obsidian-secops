---
mitre_id: "S1091"
mitre_name: "Pacu"
mitre_type: "tool"
mitre_stix_id: "tool--1b3b8f96-43b1-4460-8e02-1f53d7802fb9"
mitre_created: "2023-09-28T13:21:49.652Z"
mitre_modified: "2023-10-19T12:18:43.123Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S1091/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Pacu"
aliases:
  - "S1091"
  - "Pacu"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Pacu is an open-source AWS exploitation framework. The tool is written in Python and publicly available on GitHub.(Citation: GitHub Pacu)

## Workspace

- [[workspaces/tools/S1091-pacu-note|Open workspace note]]

![[workspaces/tools/S1091-pacu-note]]

## Uses Techniques

- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069003-cloud-groups|T1069.003: Cloud Groups]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1526-cloud_service_discovery|T1526: Cloud Service Discovery]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555006-cloud-secrets-management-stores|T1555.006: Cloud Secrets Management Stores]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562007-disable-or-modify-cloud-firewall|T1562.007: Disable or Modify Cloud Firewall]]
    - [[T1562-impair_defenses#^t1562008-disable-or-modify-cloud-logs|T1562.008: Disable or Modify Cloud Logs]]
- [[T1578-modify_cloud_compute_infrastructure|T1578: Modify Cloud Compute Infrastructure]]
    - [[T1578-modify_cloud_compute_infrastructure#^t1578001-create-snapshot|T1578.001: Create Snapshot]]
- [[T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]
- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]
- [[T1648-serverless_execution|T1648: Serverless Execution]]
- [[T1651-cloud_administration_command|T1651: Cloud Administration Command]]
- [[T1654-log_enumeration|T1654: Log Enumeration]]

