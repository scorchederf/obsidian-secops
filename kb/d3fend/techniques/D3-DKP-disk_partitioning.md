---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DKP"
d3fend_name: "Disk Partitioning"
d3fend_ontology_id: "d3f:DiskPartitioning"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADiskPartitioning/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1561"
  - "T1561.001"
  - "T1561.002"
---

# D3-DKP: Disk Partitioning

Disk Partitioning is the process of dividing a disk into multiple distinct sections, known as partitions.

## Parent Technique

- [[D3-DKF-disk_formatting|D3-DKF: Disk Formatting]]

## Related ATT&CK Techniques

- [[T1561-disk_wipe|T1561: Disk Wipe]]
- [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
- [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]

## Knowledge Base Article

### How it works

Each partition can be managed separately and can have its own file system. Disk partitioning can be used to segregate sensitive data from less critical data, improve system performance, and enhance data management and recovery processes. It can also help in isolating different operating systems or environments on the same physical disk.

## Ontology Relationships

- [[D3-DKF-disk_formatting|D3-DKF: Disk Formatting]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-dkp-notes|Open workspace note]]

