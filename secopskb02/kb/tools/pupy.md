---
mitre_id: "S0192"
mitre_name: "Pupy"
mitre_type: "tool"
mitre_stix_id: "tool--cb69b20d-56d0-41ab-8440-4a4b251614d4"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2023-09-28T21:08:47.128Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0192/"
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
  - "Pupy"
aliases:
  - "S0192"
  - "Pupy"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. (Citation: GitHub Pupy) It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). (Citation: GitHub Pupy) [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. (Citation: GitHub Pupy)

## Workspace

- [[workspaces/tools/S0192-pupy-note|Open workspace note]]

![[workspaces/tools/S0192-pupy-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
    - [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
- [[T1135-network_share_discovery|T1135: Network Share Discovery]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547013-xdg-autostart-entries|T1547.013: XDG Autostart Entries]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
    - [[T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

