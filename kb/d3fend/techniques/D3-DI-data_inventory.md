---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DI"
d3fend_name: "Data Inventory"
d3fend_ontology_id: "d3f:DataInventory"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADataInventory/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.002"
  - "T1003.004"
  - "T1003.008"
  - "T1012"
  - "T1033"
  - "T1112"
  - "T1114"
  - "T1114.001"
  - "T1137"
  - "T1137.003"
  - "T1137.006"
  - "T1207"
  - "T1213"
  - "T1213.003"
  - "T1218"
  - "T1218.005"
  - "T1218.014"
  - "T1534"
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
  - "T1564.007"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
  - "T1614"
  - "T1614.001"
---

# D3-DI: Data Inventory

Data inventorying identifies and records the schemas, formats, volumes, and locations of data stored and used on the organization's architecture.

## Parent Technique

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1003-os_credential_dumping#^t1003008--etc-passwd-and--etc-shadow|T1003.008: /etc/passwd and /etc/shadow]]
- [[T1012-query_registry|T1012: Query Registry]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137003-outlook-forms|T1137.003: Outlook Forms]]
- [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
- [[T1218-system_binary_proxy_execution#^t1218014-mmc|T1218.014: MMC]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
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
- [[T1564-hide_artifacts#^t1564007-vba-stomping|T1564.007: VBA Stomping]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]
- [[T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Ontology Relationships

- [[D3-AI-asset_inventory|D3-AI: Asset Inventory]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-di-notes|Open workspace note]]

