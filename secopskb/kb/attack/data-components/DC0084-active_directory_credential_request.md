---
mitre_id: "DC0084"
mitre_name: "Active Directory Credential Request"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--02d090b6-8157-48da-98a2-517f7edd49fc"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Requests for authentication credentials via Kerberos or other methods like NTLM and LDAP queries. Examples:

- Kerberos TGT and Service Tickets (Event IDs 4768, 4769)
- NTLM Authentication Events
- LDAP Bind Requests.

## Workspace

- [[notes/attack/data-components/DC0084-active_directory_credential_request-note|Open workspace note]]

![[notes/attack/data-components/DC0084-active_directory_credential_request-note]]

