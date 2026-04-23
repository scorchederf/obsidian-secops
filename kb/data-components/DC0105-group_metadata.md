---
mitre_id: "DC0105"
mitre_name: "Group Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--8d8c7cac-94cf-4726-8989-cab33851168c"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:14:39.577Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# DC0105: Group Metadata

Group metadata includes attributes like name, permissions, purpose, and associated user accounts or roles, which adversaries may exploit for privilege escalation. Examples:

- Active Directory: `Get-ADGroup -Identity "Domain Admins" -Properties Members, Description`
- Azure AD: `Get-AzureADGroup -ObjectId <GroupId>`
- Google Workspace: `GET https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`
- AWS IAM: `aws iam list-group-policies --group-name <group_name>`
- Office 365: `GET https://graph.microsoft.com/v1.0/groups/<id>`

*Data Collection Measures:*

- Cloud Logging:
    - AWS CloudTrail for IAM group-related activities.
    - Azure AD Sign-In/Audit logs for metadata changes.
    - Google Admin Activity logs for API calls.
- Directory Logging: Log metadata access (e.g., Windows Event ID 4662).
- API Monitoring: Log API calls to modify group metadata (e.g., Microsoft Graph API).
- SIEM Integration: Centralize group metadata logs for analysis.


