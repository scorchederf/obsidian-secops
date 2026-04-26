---
mitre_id: "S0122"
mitre_name: "Pass-The-Hash Toolkit"
mitre_type: "tool"
mitre_stix_id: "tool--a52edc76-328d-4596-85e7-d56ef5a9eb69"
mitre_created: "2017-05-31T21:33:11.426Z"
mitre_modified: "2025-04-25T14:45:25.272Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0122/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
aliases:
  - "S0122"
  - "Pass-The-Hash Toolkit"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

[Pass-The-Hash Toolkit](https://attack.mitre.org/software/S0122) is a toolkit that allows an adversary to "pass" a password hash (without knowing the original password) to log in to systems. (Citation: Mandiant APT1)

## Workspace

- [[workspaces/tools/S0122-pass-the-hash_toolkit-note|Open workspace note]]

![[workspaces/tools/S0122-pass-the-hash_toolkit-note]]

## Uses Techniques

- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]

