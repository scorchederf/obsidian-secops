---
mitre_id: "DC0081"
mitre_name: "Instance Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--7561ed50-16cb-4826-82c7-c1ddca61785e"
mitre_created: "2021-10-20T15:05:19.274Z"
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

Removal of a virtual machine (VM) or compute instance within a cloud infrastructure. This activity results in the termination and deletion of the allocated resources (e.g., CPU, memory, storage), making the instance unavailable for future use. Examples:

- AWS: instance deletion involves the `TerminateInstances` API call, which is recorded in CloudTrail logs.
- Azure: VM deletion can be monitored via Azure Activity Logs, showing the `Microsoft.Compute/virtualMachines/delete` operation.
- GCP: instance deletion is logged as an instance.delete operation within GCP Audit Logs.

## Workspace

- [[workspaces/attack/data-components/DC0081-instance_deletion-note|Open workspace note]]

![[workspaces/attack/data-components/DC0081-instance_deletion-note]]

