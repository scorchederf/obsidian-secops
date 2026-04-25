---
mitre_id: "M1022"
mitre_name: "Restrict File and Directory Permissions"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--987988f0-cf86-4680-a875-2f6456ab2448"
mitre_created: "2019-06-06T20:54:49.964Z"
mitre_modified: "2024-12-18T19:18:58.856Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1022/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Enforce Least Privilege Permissions:

- Remove unnecessary write permissions on sensitive files and directories.
- Use file ownership and groups to control access for specific roles.

Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs.

Harden File Shares:

- Disable anonymous access to shared folders.
- Enforce NTFS permissions for shared folders on Windows.

Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access.

On Linux, apply:
`chmod 750 /etc/sensitive.conf`
`chown root:admin /etc/sensitive.conf`

File Integrity Monitoring (FIM):

- Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions.

Audit File System Access:

- Enable auditing to track permission changes or unauthorized access attempts.
- Use auditd (Linux) or Event Viewer (Windows) to log activities.

Restrict Startup Directories:

- Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`.

Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`.

- On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F`
- On Linux, monitor permissions using tools like `lsattr` or `auditd`.

## Workspace

- [[workspaces/attack/mitigations/M1022-restrict_file_and_directory_permissions-note|Open workspace note]]

![[workspaces/attack/mitigations/M1022-restrict_file_and_directory_permissions-note]]

## Mitigates Techniques

- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037002-login-hook|T1037.002: Login Hook]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037003-network-logon-script|T1037.003: Network Logon Script]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
    - [[T1037-boot_or_logon_initialization_scripts#^t1037005-startup-items|T1037.005: Startup Items]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055009-proc-memory|T1055.009: Proc Memory]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
    - [[T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]
    - [[T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]
    - [[T1070-indicator_removal#^t1070008-clear-mailbox-data|T1070.008: Clear Mailbox Data]]
    - [[T1070-indicator_removal#^t1070009-clear-persistence|T1070.009: Clear Persistence]]
- [[T1080-taint_shared_content|T1080: Taint Shared Content]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098004-ssh-authorized-keys|T1098.004: SSH Authorized Keys]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218002-control-panel|T1218.002: Control Panel]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
- [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]
    - [[T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]
    - [[T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]
- [[T1489-service_stop|T1489: Service Stop]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]
    - [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]]
    - [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547003-time-providers|T1547.003: Time Providers]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547013-xdg-autostart-entries|T1547.013: XDG Autostart Entries]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548006-tcc-manipulation|T1548.006: TCC Manipulation]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
    - [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553003-sip-and-trust-provider-hijacking|T1553.003: SIP and Trust Provider Hijacking]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
    - [[T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]
    - [[T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]
    - [[T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
    - [[T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]
    - [[T1565-data_manipulation#^t1565003-runtime-data-manipulation|T1565.003: Runtime Data Manipulation]]
- [[T1569-system_services|T1569: System Services]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574004-dylib-hijacking|T1574.004: Dylib Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
    - [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
    - [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]
    - [[T1574-hijack_execution_flow#^t1574014-appdomainmanager|T1574.014: AppDomainManager]]

