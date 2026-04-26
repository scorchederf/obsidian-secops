---
mitre_id: "DC0054"
mitre_name: "Drive Access"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--73ff2dcc-24b1-4368-b9dc-706dd9e68354"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
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

Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: 

- Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed.
- Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`.
- External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files.
- System Volume Access: The system volume `C:\` is accessed for modifications to critical files.
- Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.

## Workspace

- [[workspaces/attack/data-components/DC0054-drive_access-note|Open workspace note]]

![[workspaces/attack/data-components/DC0054-drive_access-note]]

