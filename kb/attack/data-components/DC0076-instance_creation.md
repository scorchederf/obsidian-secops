---
mitre_id: "DC0076"
mitre_name: "Instance Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--b5b0e8ae-7436-4951-950a-7b83c4dd3f2c"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
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

# DC0076: Instance Creation

The initial provisioning and construction of a virtual machine (VM) or compute instance within a cloud infrastructure environment. This activity involves defining and allocating resources such as CPU, memory, storage, and networking to spin up a new compute instance. Examples:

- AWS: creating an EC2 instance using RunInstances API calls.
- Azure, creating a VM through the Azure Resource Manager (ARM).
- GCP, an `instance.insert` action recorded.

## Workspace

- [[kb/notes/attack/data-components/dc0076-notes|Open workspace note]]

