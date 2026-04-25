---
mitre_id: "DC0075"
mitre_name: "Instance Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--2a80d95f-08c4-48e3-833e-151ef19d90f5"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:38.969Z"
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

The process of retrieving or querying a list of virtual machine instances or compute instances within a cloud infrastructure. This activity provides a view of all available or running instances, typically including their associated metadata such as instance ID, name, state, and configuration details. Examples:

- AWS: instance enumeration involves the `DescribeInstances` API call, which retrieves information about running or stopped EC2 instances.
- Azure: VM enumeration can be monitored via the `Microsoft.Compute/virtualMachines/read` operation.
- GCP: instance enumeration is logged as an `instance.list` operation within GCP Audit Logs.

*Data Collection Measures:*

- AWS CloudTrail: CloudTrail logs stored in S3 or forwarded to CloudWatch.
- Azure Activity Logs: Accessible via Azure Monitor or exported to a storage account.
- GCP Audit Logs: Logs Explorer or BigQuery.

## Workspace

- [[workspaces/attack/data-components/DC0075-instance_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0075-instance_enumeration-note]]

