---
mitre_id: "M1042"
mitre_name: "Disable or Remove Feature or Program"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--eb88d97c-32f1-40be-80f0-d61a4b0b4b31"
mitre_created: "2019-06-11T16:45:19.740Z"
mitre_modified: "2024-12-10T19:21:06.027Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1042/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

# M1042: Disable or Remove Feature or Program

Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 

Remove Legacy Software:

- Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash).
- Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date.

Disable Unused Features:

- Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required.
- Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue.

Control Applications Installed by Users:

- Use Case: Prevent users from installing unauthorized software via group policies or other management tools.
- Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment.

Remove Unnecessary Services:

- Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices.
- Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations.

Restrict Add-ons and Plugins:

- Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes.
- Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.



## Mitigates Techniques

- [[T1011-exfiltration_over_other_network_medium|T1011: Exfiltration Over Other Network Medium]]
- [[T1011-exfiltration_over_other_network_medium|T1011: Exfiltration Over Other Network Medium]]
    - [[T1011-exfiltration_over_other_network_medium#^t1011001-exfiltration-over-bluetooth|T1011.001: Exfiltration Over Bluetooth]]
- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
    - [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
    - [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
    - [[T1021-remote_services#^t1021008-direct-cloud-vm-connections|T1021.008: Direct Cloud VM Connections]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
    - [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1092-communication_through_removable_media|T1092: Communication Through Removable Media]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
    - [[T1098-account_manipulation#^t1098002-additional-email-delegate-permissions|T1098.002: Additional Email Delegate Permissions]]
    - [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127002-clickonce|T1127.002: ClickOnce]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127003-jamplus|T1127.003: JamPlus]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
    - [[T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]
- [[T1205-traffic_signaling|T1205: Traffic Signaling]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]
    - [[T1218-system_binary_proxy_execution#^t1218004-installutil|T1218.004: InstallUtil]]
    - [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
    - [[T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]
    - [[T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]
    - [[T1218-system_binary_proxy_execution#^t1218009-regsvcs-regasm|T1218.009: Regsvcs/Regasm]]
    - [[T1218-system_binary_proxy_execution#^t1218012-verclsid|T1218.012: Verclsid]]
    - [[T1218-system_binary_proxy_execution#^t1218013-mavinject|T1218.013: Mavinject]]
    - [[T1218-system_binary_proxy_execution#^t1218014-mmc|T1218.014: MMC]]
    - [[T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
    - [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
- [[T1221-template_injection|T1221: Template Injection]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]
    - [[T1546-event_triggered_execution#^t1546014-emond|T1546.014: Emond]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547007-re-opened-applications|T1547.007: Re-opened Applications]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553005-mark-of-the-web-bypass|T1553.005: Mark-of-the-Web Bypass]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562010-downgrade-attack|T1562.010: Downgrade Attack]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]
    - [[T1564-hide_artifacts#^t1564007-vba-stomping|T1564.007: VBA Stomping]]
- [[T1595-active_scanning|T1595: Active Scanning]]
    - [[T1595-active_scanning#^t1595003-wordlist-scanning|T1595.003: Wordlist Scanning]]
- [[T1609-container_administration_command|T1609: Container Administration Command]]
- [[T1611-escape_to_host|T1611: Escape to Host]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]
- [[T1671-cloud_application_integration|T1671: Cloud Application Integration]]

## Workspace

- [[kb/notes/attack/mitigations/m1042-notes|Open workspace note]]

