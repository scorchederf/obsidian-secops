---
mitre_id: "S0500"
mitre_name: "MCMD"
mitre_type: "tool"
mitre_stix_id: "tool--975737f1-b10d-476f-8bda-3ec26ea57172"
mitre_created: "2020-08-13T17:15:25.702Z"
mitre_modified: "2025-04-16T20:38:54.178Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0500/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "MCMD"
aliases:
  - "S0500"
  - "MCMD"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[MCMD](https://attack.mitre.org/software/S0500) is a remote access tool that provides remote command shell capability used by [Dragonfly 2.0](https://attack.mitre.org/groups/G0074).(Citation: Secureworks MCMD July 2019)

## Workspace

- [[workspaces/tools/S0500-mcmd-note|Open workspace note]]

![[workspaces/tools/S0500-mcmd-note]]

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070009-clear-persistence|T1070.009: Clear Persistence]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]

