---
id: S0029
name: PsExec
created: 2017-05-31 21:32:21.771000+00:00
modified: 2024-09-25 20:31:21.768000+00:00
type: tool
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

# PsExec

[PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec)

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

