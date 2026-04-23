---
mitre_id: "DC0080"
mitre_name: "Instance Start"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--f8213cde-6b3a-420d-9ab7-41c9af1a919f"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0080: Instance Start

The initiation or activation of a virtual machine instance within a cloud infrastructure. This action typically involves starting an existing instance that had been stopped or paused, allowing it to resume operation. Examples: 

- Google Cloud Platform (GCP): Starting an instance through `instance.start` API activity.
- AWS: Logging of `StartInstances` in AWS CloudTrail for EC2 instances.
- Azure: `Microsoft.Compute/virtualMachines/start` entries indicate a VM instance being started.

