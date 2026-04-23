---
mitre_id: "S0364"
mitre_name: "RawDisk"
mitre_type: "tool"
mitre_stix_id: "tool--3ffbdc1f-d2bf-41ab-91a2-c7b857e98079"
mitre_created: "2019-03-25T12:30:40.919Z"
mitre_modified: "2024-11-17T19:51:16.652Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0364/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "RawDisk"
---

# RawDisk

[RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware)

## Uses Techniques

- [[T1485-data_destruction|T1485: Data Destruction]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
    - [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
    - [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]

