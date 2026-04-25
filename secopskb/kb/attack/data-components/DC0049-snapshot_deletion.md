---
mitre_id: "DC0049"
mitre_name: "Snapshot Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--16e07530-764b-4d83-bae0-cdbfc31bf21d"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:14:39.893Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

The removal of a point-in-time backup of a cloud storage volume, virtual machine (VM), or database.

*Data Collection Measures:*

- AWS CloudTrail
    - Logs `DeleteSnapshot` API calls in EC2, RDS, and EBS services.
- Azure Monitor Logs
    - Tracks snapshot deletions via `Microsoft.Compute/snapshots/delete` API calls.
- Google Cloud Logging
    - Detects snapshot removal through `compute.disks.deleteSnapshot` events.

## Workspace

- [[notes/attack/data-components/DC0049-snapshot_deletion-note|Open workspace note]]

![[notes/attack/data-components/DC0049-snapshot_deletion-note]]

