---
mitre_id: "DC0061"
mitre_name: "File Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--84572de3-9583-4c73-aabd-06ea88123dd8"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware, or adversarial modifications). Examples: 

- Content Modifications: Changes to the content of a configuration file, such as modifying `/etc/ssh/sshd_config` on Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows.
- Permission Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying NTFS permissions on Windows.
- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system on Windows.
- Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch` in Linux or timestomping tools on Windows.
- Software or System File Changes: Modifying system files such as `boot.ini`, kernel modules, or application binaries.

## Workspace

- [[workspaces/attack/data-components/DC0061-file_modification-note|Open workspace note]]

![[workspaces/attack/data-components/DC0061-file_modification-note]]

