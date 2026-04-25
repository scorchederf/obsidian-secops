---
mitre_id: "S0121"
mitre_name: "Lslsass"
mitre_type: "tool"
mitre_stix_id: "tool--2fab555f-7664-4623-b4e0-1675ae38190b"
mitre_created: "2017-05-31T21:33:10.962Z"
mitre_modified: "2025-04-25T14:45:15.980Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0121/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Lslsass"
aliases:
  - "S0121"
  - "Lslsass"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[Lslsass](https://attack.mitre.org/software/S0121) is a publicly-available tool that can dump active logon session password hashes from the lsass process. (Citation: Mandiant APT1)

## Workspace

- [[workspaces/tools/S0121-lslsass-note|Open workspace note]]

![[workspaces/tools/S0121-lslsass-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

