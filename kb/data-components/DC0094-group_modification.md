---
mitre_id: "DC0094"
mitre_name: "Group Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--05d5b5b4-ef93-4807-b05f-33d8c5a35bc5"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:14:40.086Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0094: Group Modification

Changes made to a group, such as membership, name, or permissions (ex: Windows EID 4728 or 4732, AWS IAM UpdateGroup). Examples: 

- Active Directory:
    - Event ID 4728: Member added to a global group.
    - Event ID 4732: Member added to a local group.
- Azure AD: `Set-AzureADGroup -ObjectId <GroupId> -DisplayName "New Name"`
- AWS IAM: `aws iam update-group --group-name <GroupName> --new-path "/admin/"`
- Google Workspace: Modify permissions via Admin SDK API: `PATCH https://admin.googleapis.com/admin/directory/v1/groups/<groupKey>`
- Office 365: Modify groups via Graph API: `PATCH https://graph.microsoft.com/v1.0/groups/<groupId>`

*Data Collection Measures:*

- Directory Logging:
    - Windows: Log EIDs 4728 (add), 4729 (remove).
    - Azure AD: Enable "Audit logs."
    - Google Workspace: Enable Admin Activity logs.
    - Office 365: Use Unified Audit Logs.
- Cloud Monitoring:
    - AWS: Log `UpdateGroup`, `AttachGroupPolicy`, `RemoveUserFromGroup`.
    - Azure: Track modifications via Audit logs.
- API Monitoring: Log Google Admin SDK and Microsoft Graph API calls.
- SIEM Integration: Centralize and monitor group modification logs.

