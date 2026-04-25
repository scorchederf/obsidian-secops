---
mitre_id: "S0194"
mitre_name: "PowerSploit"
mitre_type: "tool"
mitre_stix_id: "tool--13cd9151-83b7-410d-9f98-25d0f0d1d80d"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-04-16T20:38:50.246Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0194/"
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
  - "PowerSploit"
aliases:
  - "S0194"
  - "PowerSploit"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation)

## Workspace

- [[workspaces/tools/S0194-powersploit-note|Open workspace note]]

![[workspaces/tools/S0194-powersploit-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1012-query_registry|T1012: Query Registry]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027005-indicator-removal-from-tools|T1027.005: Indicator Removal from Tools]]
    - [[T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547005-security-support-provider|T1547.005: Security Support Provider]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
    - [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]
    - [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
    - [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]
- [[T1620-reflective_code_loading|T1620: Reflective Code Loading]]

