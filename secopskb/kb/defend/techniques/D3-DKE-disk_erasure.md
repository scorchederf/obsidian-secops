---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DKE"
d3fend_name: "Disk Erasure"
d3fend_ontology_id: "d3f:DiskErasure"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADiskErasure/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Disk Erasure is the process of securely deleting all data on a disk to ensure that it cannot be recovered by any means.

## Workspace

- [[workspaces/defend/techniques/D3-DKE-disk_erasure-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DKE-disk_erasure-note]]

## Parent Technique

- [[D3-DKF-disk_formatting|D3-DKF: Disk Formatting]]

## Related ATT&CK Techniques

- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

## Knowledge Base Article

### How it works

Disk Erasure involves overwriting the existing data with random or specific patterns multiple times. Disk erasure is crucial for data sanitization, ensuring that sensitive information is completely removed from storage devices before they are repurposed, disposed of, or transferred to another party.

## Ontology Relationships

- [[D3-DKF-disk_formatting|D3-DKF: Disk Formatting]]

