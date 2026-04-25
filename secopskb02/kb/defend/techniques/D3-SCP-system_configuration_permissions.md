---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SCP"
d3fend_name: "System Configuration Permissions"
d3fend_ontology_id: "d3f:SystemConfigurationPermissions"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemConfigurationPermissions/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1012"
  - "T1112"
  - "T1137"
  - "T1137.006"
  - "T1207"
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
  - "T1564"
  - "T1564.003"
  - "T1564.005"
  - "T1614"
  - "T1614.001"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Restricting system configuration modifications to a specific user or group of users.

## Workspace

- [[workspaces/defend/techniques/D3-SCP-system_configuration_permissions-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SCP-system_configuration_permissions-note]]

## Parent Technique

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

## Related ATT&CK Techniques

- [[T1012-query_registry|T1012: Query Registry]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
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
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]
- [[T1564-hide_artifacts#^t1564005-hidden-file-system|T1564.005: Hidden File System]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]
- [[T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Ontology Relationships

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

