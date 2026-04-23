---
mitre_id: "DC0098"
mitre_name: "Volume Deletion"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--3acecdde-c327-4498-9bb8-33a2e63c6c57"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# DC0098: Volume Deletion

The removal of a cloud-based or on-premise block storage volume. This action permanently deletes the allocated storage and may result in data loss if not backed up.

*Data Collection Measures:*

- Cloud Logging & APIs
    - AWS CloudTrail Logs
        - `eventName: DeleteVolume` (tracks volume deletions)
    - Azure Monitor Logs
        - `operationName: Microsoft.Compute/disks/delete`
        - `status: Success | Failure` (flag unauthorized delete attempts)
    - Google Cloud Audit Logs
        - `protoPayload.methodName: "v1.compute.disks.delete"`
        - `authenticationInfo.principalEmail` (identifies the user deleting the volume)
- System & Host-Based Logging
    - Linux & macOS Logs:
        - `/var/log/syslog` or `/var/log/messages` for volume detach/deletion actions
    - Windows Event Logs:
        - Event ID 98 (Storage Class Memory)
        - Event ID 225 (Volume Removal Detected)
        - Event ID 12 (Disk Removal Notification)

