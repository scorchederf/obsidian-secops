---
id: S0106
name: cmd
created: 2017-05-31 21:33:05.319000+00:00
modified: 2025-04-16 20:38:55.702000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# cmd

[cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. (Citation: TechNet Cmd)

Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)).

## Uses Techniques

- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

