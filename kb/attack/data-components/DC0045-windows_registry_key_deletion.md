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
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0045: Windows Registry Key Deletion

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

- [[kb/notes/attack/data-components/dc0045-notes|Open workspace note]]

