---
id: S0364
name: RawDisk
created: 2019-03-25 12:30:40.919000+00:00
modified: 2024-11-17 19:51:16.652000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# RawDisk

[RawDisk](https://attack.mitre.org/software/S0364) is a legitimate commercial driver from the EldoS Corporation that is used for interacting with files, disks, and partitions. The driver allows for direct modification of data on a local computer's hard drive. In some cases, the tool can enact these raw disk modifications from user-mode processes, circumventing Windows operating system security features.(Citation: EldoS RawDisk ITpro)(Citation: Novetta Blockbuster Destructive Malware)

## Properties

- id: S0364
- name: RawDisk
- created: 2019-03-25 12:30:40.919000+00:00
- modified: 2024-11-17 19:51:16.652000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1485-data_destruction|T1485: Data Destruction]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
    - [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
    - [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]

