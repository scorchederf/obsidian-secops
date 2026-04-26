---
mitre_id: "DC0023"
mitre_name: "Cloud Storage Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--45977f14-1bcc-4ec4-ac14-a30fd3a11f44"
mitre_created: "2021-10-20T15:05:19.272Z"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Cloud Storage Modification involves tracking changes made to cloud storage infrastructure, including updates to settings, permissions, or stored data. Examples include modifying object access control lists (ACLs), uploading new objects, or updating bucket policies. Examples: 

AWS S3: An object is uploaded or its ACL is modified.
- Azure Blob Storage: A blob's metadata or permissions are updated.
- Google Cloud Storage: An object's lifecycle policy is updated, or a bucket policy is changed.
- OpenStack Swift: Modifications to container settings or uploading of new objects.

## Workspace

- [[workspaces/attack/data-components/DC0023-cloud_storage_modification-note|Open workspace note]]

![[workspaces/attack/data-components/DC0023-cloud_storage_modification-note]]

