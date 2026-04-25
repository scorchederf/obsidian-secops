---
mitre_id: "S0193"
mitre_name: "Forfiles"
mitre_type: "tool"
mitre_stix_id: "tool--90ec2b22-7061-4469-b539-0989ec4f96c2"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-04-25T14:45:23.318Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0193/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
aliases:
  - "S0193"
  - "Forfiles"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. (Citation: Microsoft Forfiles Aug 2016)

## Workspace

- [[workspaces/tools/S0193-forfiles-note|Open workspace note]]

![[workspaces/tools/S0193-forfiles-note]]

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1202-indirect_command_execution|T1202: Indirect Command Execution]]

