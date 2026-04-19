---
id: S0193
name: Forfiles
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-04-25 14:45:23.318000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Forfiles

[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. (Citation: Microsoft Forfiles Aug 2016)

## Properties

- id: S0193
- name: Forfiles
- created: 2018-04-18 17:59:24.739000+00:00
- modified: 2025-04-25 14:45:23.318000+00:00
- type: tool
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1202-indirect_command_execution|T1202: Indirect Command Execution]]

