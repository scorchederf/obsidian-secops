---
mitre_id: "S0119"
mitre_name: "Cachedump"
mitre_type: "tool"
mitre_stix_id: "tool--c9cd7ec9-40b7-49db-80be-1399eddd9c52"
mitre_created: "2017-05-31T21:33:10.197Z"
mitre_modified: "2025-04-25T14:45:28.653Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0119/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Cachedump"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

[Cachedump](https://attack.mitre.org/software/S0119) is a publicly-available tool that program extracts cached password hashes from a system’s registry. (Citation: Mandiant APT1)

## Workspace

- [[notes/tools/S0119-cachedump-note|Open workspace note]]

![[notes/tools/S0119-cachedump-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]

