---
mitre_id: "DC0055"
mitre_name: "File Access"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--235b7491-2d2b-4617-9a52-3c0783680f71"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0055: File Access

To events where a file is opened or accessed, making its contents available to the requester. This includes reading, executing, or interacting with files by authorized or unauthorized entities. Examples include logging file access events (e.g., Windows Event ID 4663), monitoring file reads, and detecting unusual file access patterns. Examples: 

- File Read Operations: A user opens a sensitive document (e.g., financial_report.xlsx) on a shared drive.
- File Execution: A script or executable file is accessed and executed (e.g., malware.exe is run from a temporary directory).
- Unauthorized File Access: An unauthorized user attempts to access a protected configuration file (e.g., `/etc/passwd` on Linux or `System32` files on Windows).
- File Access Patterns: Bulk access to multiple files in a short time (e.g., mass access to documents on a file server).
- File Access via Network: Files on a network share are accessed remotely (e.g., logs of SMB file access).

