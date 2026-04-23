---
mitre_id: "S0332"
mitre_name: "Remcos"
mitre_type: "tool"
mitre_stix_id: "tool--7cd0bc75-055b-4098-a00e-83dc8beaff14"
mitre_created: "2019-01-29T18:55:20.245Z"
mitre_modified: "2025-04-16T20:38:53.082Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0332/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "Remcos"
---

# Remcos

[Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been observed being used in malware campaigns.(Citation: Riskiq Remcos Jan 2018)(Citation: Talos Remcos Aug 2018)

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1115-clipboard_data|T1115: Clipboard Data]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

