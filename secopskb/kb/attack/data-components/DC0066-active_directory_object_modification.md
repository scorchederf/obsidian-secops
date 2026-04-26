---
mitre_id: "DC0066"
mitre_name: "Active Directory Object Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--5b8b466b-2c81-4fe7-946f-d677a74ae3db"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Changes to AD objects (e.g., users, groups, OUs) are logged as Event ID 5136 (Object Modification) or 5163 (Attribute Changes). Examples:

- User Account: Modifying attributes (e.g., group membership, enabling/disabling accounts).
- Group Membership: Adding/removing members.
- OU: Changing properties/permissions (e.g., delegation).
- Service Account: Modifying SPNs or other attributes.
- Object Attributes: Changes to passwords, logon hours, or control flags.

## Workspace

- [[workspaces/attack/data-components/DC0066-active_directory_object_modification-note|Open workspace note]]

![[workspaces/attack/data-components/DC0066-active_directory_object_modification-note]]

