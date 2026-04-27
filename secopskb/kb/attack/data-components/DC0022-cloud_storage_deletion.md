---
mitre_id: "DC0022"
mitre_name: "Cloud Storage Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--4c41e296-b8d2-4a37-b789-eb565c87c00c"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Cloud Storage Deletion refers to the removal or destruction of cloud storage infrastructure, such as buckets, containers, or directories, within a cloud environment. Monitoring this activity is critical to detecting potential unauthorized or malicious actions, such as data destruction by adversaries or accidental deletions that may lead to data loss. Examples: 

- AWS S3 Bucket Deletion: An AWS user deletes an S3 bucket using the `DeleteBucket` API call.
- Azure Blob Storage Container Deletion: A user deletes a container in Azure Blob Storage using the `Delete Container` operation.
- Google Cloud Storage Bucket Deletion: A Google Cloud user deletes a bucket using the `storage.buckets.delete` API.
- OpenStack Swift Container Deletion: A user deletes a container in OpenStack Swift using the `DELETE` method.

This data component can be collected through the following measures:

Enable Logging for Cloud Storage Services

- AWS S3: Enable AWS CloudTrail to log DeleteBucket API actions.
- Azure Blob Storage: Enable Azure Monitor and Diagnostic Logs to capture Delete Container operations. Use Azure Event Grid to capture and trigger alerts for container deletion.
- Google Cloud Storage: Enable Data Access logs in Cloud Audit Logs to monitor storage.buckets.delete API calls.
- OpenStack Swift: Configure Swift logging to capture DELETE requests for containers.

Centralized Logging and Analysis

- Use platforms like Splunk or native SIEMs to forward and analyze logs for anomalies in cloud storage deletions.

## Workspace

- [[workspaces/attack/data-components/DC0022-cloud_storage_deletion-note|Open workspace note]]

![[workspaces/attack/data-components/DC0022-cloud_storage_deletion-note]]

