---
id: S1155
name: Covenant
created: 2024-09-04 17:08:08.985000+00:00
modified: 2024-09-06 18:11:55.619000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Covenant

[Covenant](https://attack.mitre.org/software/S1155) is a multi-platform command and control framework written in .NET. While designed for penetration testing and security research, the tool has also been used by threat actors such as [HAFNIUM](https://attack.mitre.org/groups/G0125) during operations. [Covenant](https://attack.mitre.org/software/S1155) functions through a central listener managing multiple deployed "Grunts" that communicate back to the controller.(Citation: Github Covenant)(Citation: Microsoft HAFNIUM March 2020)

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

