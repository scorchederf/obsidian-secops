---
mitre_id: "DC0024"
mitre_name: "Cloud Storage Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--59ec10d9-546b-4b8e-bccb-fa85f71e5055"
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

Cloud Storage Creation refers to the initial creation of a new cloud storage resource, such as buckets, containers, or directories, within a cloud environment. This action is critical to track as it might indicate the legitimate provisioning of resources or unauthorized actions taken by adversaries to stage, store, or exfiltrate data. Examples: 

- AWS S3 Bucket Creation: An AWS user creates a new S3 bucket using the `CreateBucket` API call.
- Azure Blob Storage Container Creation: A user creates a new container in Azure Blob Storage using the `Create Container` operation.
- Google Cloud Storage Bucket Creation: A Google Cloud user creates a new bucket using `storage.buckets.create`.
- OpenStack Swift Container Creation: A user creates a new container in OpenStack Swift using the `PUT` method.

## Workspace

- [[workspaces/attack/data-components/DC0024-cloud_storage_creation-note|Open workspace note]]

![[workspaces/attack/data-components/DC0024-cloud_storage_creation-note]]

