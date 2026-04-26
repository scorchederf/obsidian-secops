---
mitre_id: "S0075"
mitre_name: "Reg"
mitre_type: "tool"
mitre_stix_id: "tool--cde2d700-9ed1-46cf-9bce-07364fe8b24f"
mitre_created: "2017-05-31T21:32:49.000Z"
mitre_modified: "2025-04-16T20:38:56.474Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0075/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Reg"
  - "reg.exe"
aliases:
  - "S0075"
  - "Reg"
  - "reg.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

[Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)

Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT)

## Workspace

- [[workspaces/tools/S0075-reg-note|Open workspace note]]

![[workspaces/tools/S0075-reg-note]]

## Uses Techniques

- [[T1012-query_registry|T1012: Query Registry]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

