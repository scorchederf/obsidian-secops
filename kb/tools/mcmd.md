---
id: S0500
name: MCMD
created: 2020-08-13 17:15:25.702000+00:00
modified: 2025-04-16 20:38:54.178000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# MCMD

[MCMD](https://attack.mitre.org/software/S0500) is a remote access tool that provides remote command shell capability used by [Dragonfly 2.0](https://attack.mitre.org/groups/G0074).(Citation: Secureworks MCMD July 2019)

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

