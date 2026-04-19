---
id: S0695
name: Donut
created: 2022-03-25 13:35:46.781000+00:00
modified: 2025-04-16 20:38:54.932000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Donut

[Donut](https://attack.mitre.org/software/S0695) is an open source framework used to generate position-independent shellcode.(Citation: Donut Github)(Citation: Introducing Donut) [Donut](https://attack.mitre.org/software/S0695) generated code has been used by multiple threat actors to inject and load malicious payloads into memory.(Citation: NCC Group WastedLocker June 2020)

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027002-software-packing|T1027.002: Software Packing]]
    - [[T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]
    - [[T1027-obfuscated_files_or_information#^t1027015-compression|T1027.015: Compression]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1106-native_api|T1106: Native API]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
- [[T1620-reflective_code_loading|T1620: Reflective Code Loading]]

