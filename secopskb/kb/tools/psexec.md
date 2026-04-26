---
mitre_id: "S0029"
mitre_name: "PsExec"
mitre_type: "tool"
mitre_stix_id: "tool--ff6caf67-ea1f-4895-b80e-4bb0fc31c6db"
mitre_created: "2017-05-31T21:32:21.771Z"
mitre_modified: "2024-09-25T20:31:21.768Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0029/"
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
  - "PsExec"
aliases:
  - "S0029"
  - "PsExec"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec)

## Workspace

- [[workspaces/tools/S0029-psexec-note|Open workspace note]]

![[workspaces/tools/S0029-psexec-note]]

## Uses Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

