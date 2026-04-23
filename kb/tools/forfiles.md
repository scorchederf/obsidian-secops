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
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# Forfiles

[Forfiles](https://attack.mitre.org/software/S0193) is a Windows utility commonly used in batch jobs to execute commands on one or more selected files or directories (ex: list all directories in a drive, read the first line of all files created yesterday, etc.). Forfiles can be executed from either the command line, Run window, or batch files/scripts. (Citation: Microsoft Forfiles Aug 2016)

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1202-indirect_command_execution|T1202: Indirect Command Execution]]

