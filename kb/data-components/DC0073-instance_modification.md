---
mitre_id: "DC0073"
mitre_name: "Instance Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--45d0ff14-b9c4-41f5-8603-156657c20b75"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:40.223Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# DC0073: Instance Modification

Changes made to a virtual machine (VM) or compute instance, including alterations to its configuration, metadata, attached policies, or operational state. Such modifications can include updating metadata, attaching or detaching resource policies, resizing instances, or modifying network configurations. Examples:

- AWS: instance modifications include API actions like `ModifyInstanceAttribute`, `ModifyInstanceMetadataOptions`, or `RebootInstances`.
- Azure: modifications can be tracked through operations like `Microsoft.Compute/virtualMachines/write`.
- GCP: instance modification events include operations like `instances.setMetadata`, `instances.addResourcePolicies`, or `instances.resize`.

*Data Collection Measures:*

- AWS CloudTrail: Log Location: Stored in S3 or forwarded to CloudWatch.
- Azure Activity Logs: Log Location: Accessible via Azure Monitor or exported to a storage account.
- GCP Audit Logs: Log Location: Logs Explorer or BigQuery.

