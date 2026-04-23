---
mitre_id: "S0106"
mitre_name: "cmd"
mitre_type: "tool"
mitre_stix_id: "tool--bba595da-b73a-4354-aa6c-224d4de7cb4e"
mitre_created: "2017-05-31T21:33:05.319Z"
mitre_modified: "2025-04-16T20:38:55.702Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0106/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "cmd"
  - "cmd.exe"
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

