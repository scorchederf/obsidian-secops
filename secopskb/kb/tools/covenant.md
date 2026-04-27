---
mitre_id: "S1155"
mitre_name: "Covenant"
mitre_type: "tool"
mitre_stix_id: "tool--05fb53c8-e2ac-4e17-a0c9-a0825e1198bf"
mitre_created: "2024-09-04T17:08:08.985Z"
mitre_modified: "2024-09-06T18:11:55.619Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S1155/"
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
  - "Covenant"
aliases:
  - "S1155"
  - "Covenant"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155) functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.(Citation: Github Covenant)(Citation: Microsoft HAFNIUM March 2020)

## Workspace

- [[workspaces/tools/S1155-covenant-note|Open workspace note]]

![[workspaces/tools/S1155-covenant-note]]

## Uses Techniques

- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218004-installutil|T1218.004: InstallUtil]]
    - [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
    - [[T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

