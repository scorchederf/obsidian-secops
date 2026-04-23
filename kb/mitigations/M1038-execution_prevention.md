---
mitre_id: "M1038"
mitre_name: "Execution Prevention"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--47e0e9fe-96ce-4f65-8bb1-8be1feacb5db"
mitre_created: "2019-06-11T16:35:25.488Z"
mitre_modified: "2024-12-11T18:10:27.976Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1038/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# M1038: Execution Prevention

Prevent the execution of unauthorized or malicious code on systems by implementing application control, script blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:

Application Control:

- Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory access control policies for application execution.
- Implementation: Allow only digitally signed or pre-approved applications to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath "C:\Policies\AppLocker.xml"`) 


Script Blocking:

- Use Case: Use script control mechanisms to block unauthorized execution of scripts, such as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted sources.
- Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g., `Set-ExecutionPolicy AllSigned`) 

Executable Blocking:

- Use Case: Prevent execution of binaries from suspicious locations, such as `%TEMP%` or `%APPDATA%` directories.
- Implementation: Block execution of `.exe`, `.bat`, or `.ps1` files from user-writable directories.

Dynamic Analysis Prevention:
- Use Case: Use behavior-based execution prevention tools to identify and block malicious activity in real time.
- Implemenation: Employ EDR solutions that analyze runtime behavior and block suspicious code execution.

## Mitigates Techniques

- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
    - [[T1036-masquerading#^t1036008-masquerade-file-type|T1036.008: Masquerade File Type]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
    - [[T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]
    - [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
    - [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
    - [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]]
    - [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]
    - [[T1059-command_and_scripting_interpreter#^t1059010-autohotkey-&-autoit|T1059.010: AutoHotKey & AutoIT]]
    - [[T1059-command_and_scripting_interpreter#^t1059011-lua|T1059.011: Lua]]
    - [[T1059-command_and_scripting_interpreter#^t1059013-container-cli-api|T1059.013: Container CLI/API]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1080-taint_shared_content|T1080: Taint Shared Content]]
- [[T1106-native_api|T1106: Native API]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127003-jamplus|T1127.003: JamPlus]]
- [[T1129-shared_modules|T1129: Shared Modules]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions|T1176: Software Extensions]]
    - [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
    - [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
    - [[T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
- [[T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]
- [[T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]
    - [[T1216-system_script_proxy_execution#^t1216001-pubprn|T1216.001: PubPrn]]
    - [[T1216-system_script_proxy_execution#^t1216002-syncappvpublishingserver|T1216.002: SyncAppvPublishingServer]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218001-compiled-html-file|T1218.001: Compiled HTML File]]
    - [[T1218-system_binary_proxy_execution#^t1218002-control-panel|T1218.002: Control Panel]]
    - [[T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]
    - [[T1218-system_binary_proxy_execution#^t1218004-installutil|T1218.004: InstallUtil]]
    - [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
    - [[T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]
    - [[T1218-system_binary_proxy_execution#^t1218009-regsvcs-regasm|T1218.009: Regsvcs/Regasm]]
    - [[T1218-system_binary_proxy_execution#^t1218012-verclsid|T1218.012: Verclsid]]
    - [[T1218-system_binary_proxy_execution#^t1218013-mavinject|T1218.013: Mavinject]]
    - [[T1218-system_binary_proxy_execution#^t1218014-mmc|T1218.014: MMC]]
    - [[T1218-system_binary_proxy_execution#^t1218015-electron-applications|T1218.015: Electron Applications]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
- [[T1219-remote_access_tools|T1219: Remote Access Tools]]
    - [[T1219-remote_access_tools#^t1219001-ide-tunneling|T1219.001: IDE Tunneling]]
    - [[T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]
- [[T1220-xsl_script_processing|T1220: XSL Script Processing]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]
    - [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
    - [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
    - [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
    - [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547006-kernel-modules-and-extensions|T1547.006: Kernel Modules and Extensions]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548004-elevated-execution-with-prompt|T1548.004: Elevated Execution with Prompt]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553001-gatekeeper-bypass|T1553.001: Gatekeeper Bypass]]
    - [[T1553-subvert_trust_controls#^t1553003-sip-and-trust-provider-hijacking|T1553.003: SIP and Trust Provider Hijacking]]
    - [[T1553-subvert_trust_controls#^t1553005-mark-of-the-web-bypass|T1553.005: Mark-of-the-Web Bypass]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
    - [[T1562-impair_defenses#^t1562011-spoof-security-alerting|T1562.011: Spoof Security Alerting]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]
    - [[T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]
    - [[T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
    - [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]
    - [[T1574-hijack_execution_flow#^t1574012-cor-profiler|T1574.012: COR_PROFILER]]
- [[T1609-container_administration_command|T1609: Container Administration Command]]
- [[T1611-escape_to_host|T1611: Escape to Host]]
- [[T1674-input_injection|T1674: Input Injection]]

