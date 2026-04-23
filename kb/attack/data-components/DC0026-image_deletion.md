---
mitre_id: "DC0026"
mitre_name: "Image Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--8b4ca854-ac08-47da-b24f-601b28a39aff"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0026: Image Deletion

Removal of a virtual machine image in a cloud infrastructure (ex: Azure Compute Service Images DELETE) Examples: 

- Azure Compute Service Image Deletion
    - Example: Deleting a virtual machine image using Azure CLI: `az image delete --name MyImage --resource-group MyResourceGroup`
- AWS EC2 AMI (Amazon Machine Image) Deletion
    - Example: Deregistering an AMI in AWS: `aws ec2 deregister-image --image-id ami-1234567890abcdef0`
- Google Cloud Compute Engine Image Deletion
    - Example: Deleting a custom image in Google Cloud: `gcloud compute images delete my-custom-image`
- VMware vSphere
    - Example: Deleting a VM image/template from a vSphere environment:

This data component can be collected through the following measures:

Enable Cloud Platform Logging

- Azure: Enable "Activity Logs" to capture DELETE requests to `Microsoft.Compute/images`.
- AWS: Use AWS CloudTrail to monitor `DeregisterImage` or `DeleteSnapshot` API calls.
- Google Cloud: Enable "Cloud Audit Logs" to track image deletion events under `compute.googleapis.com/images`.

API Monitoring

- Monitor API activity to track the deletion of images using:
    - AWS SDK/CLI `DeregisterImage` or `DeleteSnapshot`.
    - Azure REST API DELETE operations for images.
    - Google Cloud Compute Engine APIs for image deletion.

Cloud SIEM Integration

- Ingest logs into a centralized SIEM platform for monitoring and alerting:

Event Correlation

- Correlate image deletion events with unusual account activity or concurrent unauthorized operations.


## Workspace

- [[kb/notes/attack/data-components/dc0026-notes|Open workspace note]]

