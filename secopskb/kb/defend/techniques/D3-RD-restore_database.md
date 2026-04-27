---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RD"
d3fend_name: "Restore Database"
d3fend_ontology_id: "d3f:RestoreDatabase"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARestoreDatabase/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.002"
  - "T1003.004"
  - "T1003.008"
  - "T1012"
  - "T1033"
  - "T1112"
  - "T1137"
  - "T1137.006"
  - "T1207"
  - "T1213"
  - "T1213.003"
  - "T1218"
  - "T1218.014"
  - "T1543"
  - "T1543.003"
  - "T1546"
  - "T1546.012"
  - "T1546.015"
  - "T1548"
  - "T1548.004"
  - "T1552"
  - "T1552.002"
  - "T1555"
  - "T1555.001"
  - "T1555.002"
  - "T1555.003"
  - "T1555.004"
  - "T1555.005"
  - "T1555.006"
  - "T1564"
  - "T1564.003"
  - "T1564.005"
  - "T1614"
  - "T1614.001"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Restoring the data in a database.

## Workspace

- [[workspaces/defend/techniques/D3-RD-restore_database-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RD-restore_database-note]]

## Parent Technique

- [[D3-RO-restore_object|D3-RO: Restore Object]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1003-os_credential_dumping#^t1003008--etc-passwd-and--etc-shadow|T1003.008: /etc/passwd and /etc/shadow]]
- [[T1012-query_registry|T1012: Query Registry]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218014-mmc|T1218.014: MMC]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546012-image-file-execution-options-injection|T1546.012: Image File Execution Options Injection]]
- [[T1546-event_triggered_execution#^t1546015-component-object-model-hijacking|T1546.015: Component Object Model Hijacking]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548004-elevated-execution-with-prompt|T1548.004: Elevated Execution with Prompt]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]
- [[T1555-credentials_from_password_stores#^t1555002-securityd-memory|T1555.002: Securityd Memory]]
- [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]]
- [[T1555-credentials_from_password_stores#^t1555005-password-managers|T1555.005: Password Managers]]
- [[T1555-credentials_from_password_stores#^t1555006-cloud-secrets-management-stores|T1555.006: Cloud Secrets Management Stores]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]
- [[T1564-hide_artifacts#^t1564005-hidden-file-system|T1564.005: Hidden File System]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]
- [[T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Ontology Relationships

- [[D3-RO-restore_object|D3-RO: Restore Object]]

