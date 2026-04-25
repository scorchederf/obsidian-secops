---
mitre_id: "DC0059"
mitre_name: "File Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--639e87f3-acb6-448a-9645-258f20da4bc5"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
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

contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: 

- File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows.
- Timestamps: Analyzing the creation, modification, and access timestamps of a file.
- File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation.
- File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows.
- File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds.
- File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

## Workspace

- [[workspaces/attack/data-components/DC0059-file_metadata-note|Open workspace note]]

![[workspaces/attack/data-components/DC0059-file_metadata-note]]

