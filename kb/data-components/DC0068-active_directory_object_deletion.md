---
mitre_id: "DC0068"
mitre_name: "Active Directory Object Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--9085a576-636a-455b-91d2-c2921bbe6d1d"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# DC0068: Active Directory Object Deletion

Object deletion in AD (e.g., user accounts, groups, OUs) is logged as Event ID 5141. Examples:

- User Account: Deleted user.
- Group: Deleted security/distribution group.
- Organizational Unit (OU): Loss of configurations or policies.
- Service Account: Disrupted operations or cover tracks.
- Trust Object: Removed domain trust, disrupting connectivity.

*Data Collection Measures:*

- Audit Policy:
    - Enable "Audit Directory Service Changes" (Success and Failure).
    - Path: `Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > Directory Service Changes`.
    - Key Event: Event ID 5141.
- Log Forwarding: Use WEF to centralize logs for SIEM tools (e.g., Splunk).
- Enable EDR Monitoring:
    - Detect processes or users that initiate unauthorized object deletions.
    - Monitor tools and scripts that may delete key directory objects.

