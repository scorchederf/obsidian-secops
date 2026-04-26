---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DKF"
d3fend_name: "Disk Formatting"
d3fend_ontology_id: "d3f:DiskFormatting"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADiskFormatting/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1619"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Disk Formatting is the process of preparing a data storage device, such as a hard drive, solid-state drive, or USB flash drive, for initial use.

## Workspace

- [[workspaces/defend/techniques/D3-DKF-disk_formatting-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DKF-disk_formatting-note]]

## Parent Technique

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

## Child Techniques

- [[D3-DKE-disk_erasure|D3-DKE: Disk Erasure]]
- [[D3-DKP-disk_partitioning|D3-DKP: Disk Partitioning]]

## Related ATT&CK Techniques

- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

## Knowledge Base Article

### How it works

This process involves setting up an empty file system on the disk, which includes creating a directory structure and initializing metadata structures. In cybersecurity, disk formatting can be used to remove all existing data on a disk, making it a clean slate for new data storage or to prevent unauthorized access to previously stored data.

## Ontology Relationships

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

