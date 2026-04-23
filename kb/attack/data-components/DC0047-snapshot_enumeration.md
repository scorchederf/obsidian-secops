---
mitre_id: "DC0047"
mitre_name: "Snapshot Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--ffd73905-2e51-4f2d-8549-e72fb0eb6c38"
mitre_created: "2021-10-20T15:05:19.273Z"
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

# DC0047: Snapshot Enumeration

The process of listing or retrieving metadata about existing snapshots in a cloud environment.

*Data Collection Measures:*

- AWS CloudTrail
    - Logs API calls such as `DescribeSnapshots`, `ListSnapshots`, and `GetSnapshotAttributes`.
- Azure Monitor Logs
    - Tracks snapshot enumeration via `Microsoft.Compute/snapshots/read`.
- Google Cloud Logging
    - Detects snapshot listing through `compute.disks.listSnapshots`.


## Workspace

- [[kb/notes/attack/data-components/dc0047-notes|Open workspace note]]

