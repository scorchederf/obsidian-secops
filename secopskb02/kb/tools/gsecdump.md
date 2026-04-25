---
mitre_id: "S0008"
mitre_name: "gsecdump"
mitre_type: "tool"
mitre_stix_id: "tool--b07c2c47-fefb-4d7c-a69e-6a3296171f54"
mitre_created: "2017-05-31T21:32:13.755Z"
mitre_modified: "2024-11-17T23:49:27.288Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0008/"
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
  - "gsecdump"
aliases:
  - "S0008"
  - "gsecdump"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump)

## Workspace

- [[workspaces/tools/S0008-gsecdump-note|Open workspace note]]

![[workspaces/tools/S0008-gsecdump-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]

