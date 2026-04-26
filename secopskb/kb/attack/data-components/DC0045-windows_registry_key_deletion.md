---
mitre_id: "DC0045"
mitre_name: "Windows Registry Key Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--1177a4c5-31c8-400c-8544-9071166afa0e"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

The removal of a registry key within the Windows operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4658 - Registry Key Handle Closed: Captures when a handle to a registry key is closed, which may indicate deletion.
    - Event ID 4660 - Object Deleted: Logs when a registry key is deleted.
- Sysmon (System Monitor) for Windows
    - Sysmon Event ID 12 - Registry Key Deleted: Logs when a registry key is removed.
    - Sysmon Event ID 13 - Registry Value Deleted: Captures removal of specific registry values.
- Endpoint Detection and Response (EDR) Solutions
    - Monitor registry deletions for suspicious behavior.

## Workspace

- [[workspaces/attack/data-components/DC0045-windows_registry_key_deletion-note|Open workspace note]]

![[workspaces/attack/data-components/DC0045-windows_registry_key_deletion-note]]

