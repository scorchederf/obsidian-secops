---
mitre_id: "S0262"
mitre_name: "QuasarRAT"
mitre_type: "tool"
mitre_stix_id: "tool--da04ac30-27da-4959-a67d-450ce47d9470"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2024-05-07T19:10:03.843Z"
mitre_version: "2.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0262/"
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
  - "QuasarRAT"
  - "xRAT"
aliases:
  - "S0262"
  - "QuasarRAT"
  - "xRAT"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)

## Workspace

- [[workspaces/tools/S0262-quasarrat-note|Open workspace note]]

![[workspaces/tools/S0262-quasarrat-note]]

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553002-code-signing|T1553.002: Code Signing]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]
    - [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]

