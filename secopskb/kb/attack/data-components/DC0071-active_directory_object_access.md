---
mitre_id: "DC0071"
mitre_name: "Active Directory Object Access"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--5c6de881-bc70-4070-855a-7a9631a407f7"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:35.607Z"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Object access refers to activities where AD objects (e.g., user accounts, groups, policies) are accessed or queried. Example: Windows Event ID 4661 logs object access attempts. Examples:

- Attribute Access: e.g., `userPassword`, `memberOf`, `securityDescriptor`.
- Group Enumeration: Enumerating critical group members (e.g., Domain Admins).
- User Attributes: Commonly accessed attributes like `samAccountName`, `lastLogonTimestamp`.
- Policy Access: Accessing GPOs to understand security settings.

*Data Collection Measures:*

- Audit Policies:
    - Enable "Audit Directory Service Access" under Advanced Audit Policies (Success and Failure).
    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Object AccessEnable: Audit Directory Service Access` (Success and Failure).
    - Captured Events: IDs 4661, 4662.
- Event Forwarding: Use WEF to centralize logs for SIEM analysis.
- SIEM Integration: Collect and parse logs (e.g., 4661, 4662) using tools like Splunk or Azure Sentinel.
- Log Filtering:
- Focus on sensitive objects/attributes like:
    - `Domain Admins` group.
    - `userPassword`, `ntSecurityDescriptor`.
- Enable EDR Monitoring:
    - Detect processes accessing sensitive AD objects (e.g., samAccountName, securityDescriptor).
    - Log all attempts to enumerate critical groups (e.g., "Domain Admins").

## Workspace

- [[workspaces/attack/data-components/DC0071-active_directory_object_access-note|Open workspace note]]

![[workspaces/attack/data-components/DC0071-active_directory_object_access-note]]

