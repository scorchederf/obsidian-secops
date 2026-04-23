---
mitre_id: "DC0089"
mitre_name: "Instance Stop"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--1361e324-b594-4c0e-a517-20cee32b8d7f"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:37.816Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0089: Instance Stop

The deactivation or shutdown of a virtual machine instance within a cloud infrastructure. This action typically involves stopping a running instance, which halts its operation and releases certain associated resources, such as CPU and memory. Examples: 

- Google Cloud Platform (GCP): `instance.stop` events recorded in GCP Audit Logs indicate the deactivation of an instance.
- Amazon Web Services (AWS): `StopInstances` actions in AWS CloudTrail indicate EC2 instances being stopped.
- Microsoft Azure: `Microsoft.Compute/virtualMachines/deallocate` or `stop` events in Azure Activity Logs represent a virtual machine being stopped or deallocated.

