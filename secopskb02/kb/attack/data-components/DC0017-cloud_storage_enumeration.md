---
mitre_id: "DC0017"
mitre_name: "Cloud Storage Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--fcc4811f-9cc8-4db5-8097-4d8242a380de"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
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

Cloud Storage Enumeration involves retrieving a list of available cloud storage infrastructure, such as buckets, containers, or objects, within a cloud environment. This activity may be performed for legitimate administrative purposes or malicious reconnaissance by adversaries seeking to identify accessible storage resources.Examples:

- AWS S3 Bucket Enumeration: An AWS user lists all buckets using the `ListBuckets` API call.
- Azure Blob Storage Container Enumeration: A user retrieves a list of all containers within a storage account using the Azure Storage SDK or API.
- Google Cloud Storage Bucket Enumeration: A Google Cloud user lists all buckets within a project using the `storage.buckets.list` API.
- OpenStack Swift Container Enumeration: A user retrieves a list of containers in OpenStack Swift using the `GET` method on the storage endpoint.

## Workspace

- [[workspaces/attack/data-components/DC0017-cloud_storage_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0017-cloud_storage_enumeration-note]]

