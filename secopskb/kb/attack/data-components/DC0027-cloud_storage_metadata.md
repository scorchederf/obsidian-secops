---
mitre_id: "DC0027"
mitre_name: "Cloud Storage Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--e214eb6d-de8f-4154-9015-6d47915fbed1"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Cloud Storage Metadata provides contextual information about cloud storage infrastructure and its associated activity. This data may include attributes such as storage name, size, owner, permissions, creation date, region, and activity metadata. It is essential for monitoring, auditing, and identifying anomalies in cloud storage environments. Examples: 

- AWS S3 Bucket Metadata: Metadata about an S3 bucket includes the bucket name, region, creation date, owner, storage class, and permissions.
- Azure Blob Storage Metadata: Metadata for an Azure Blob container includes container name, access level (e.g., private or public), size, and tags.
- Google Cloud Storage Metadata: Metadata includes bucket name, storage class, location, labels, lifecycle policies, and versioning status.
- OpenStack Swift Metadata: Metadata for a Swift container includes name, access level, quota, and custom attributes.

## Workspace

- [[workspaces/attack/data-components/DC0027-cloud_storage_metadata-note|Open workspace note]]

![[workspaces/attack/data-components/DC0027-cloud_storage_metadata-note]]

