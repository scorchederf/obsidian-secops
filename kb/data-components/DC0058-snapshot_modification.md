---
mitre_id: "DC0058"
mitre_name: "Snapshot Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--f1eb6ea9-f3ab-414f-af35-2d5427199984"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:14:39.957Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0058: Snapshot Modification

Changes made to a cloud snapshot's metadata, attributes, or control settings. These modifications may involve adjusting access permissions, changing retention policies, or altering encryption settings. 

*Data Collection Measures:*

- AWS CloudTrail
    - Tracks API calls such as `ModifySnapshotAttribute`, `ResetSnapshotAttribute`, and `ModifySnapshotTier`.
- Azure Monitor Logs
    - Logs changes via `Microsoft.Compute/snapshots/write`.
- Google Cloud Logging
    - Captures modifications through `compute.snapshots.setIamPolicy` and `compute.snapshots.patch`.

