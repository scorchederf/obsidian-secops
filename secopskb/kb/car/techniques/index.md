[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CAR Analytics by ATT&CK Technique

## [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-07-001-suspicious_arguments|CAR-2013-07-001: Suspicious Arguments]]
- [[kb/car/analytics/CAR-2019-04-004-credential_dumping_via_mimikatz|CAR-2019-04-004: Credential Dumping via Mimikatz]]
- [[kb/car/analytics/CAR-2019-07-002-lsass_process_dump_via_procdump|CAR-2019-07-002: Lsass Process Dump via Procdump]]
- [[kb/car/analytics/CAR-2019-08-001-credential_dumping_via_windows_task_manager|CAR-2019-08-001: Credential Dumping via Windows Task Manager]]
- [[kb/car/analytics/CAR-2019-08-002-active_directory_dumping_via_ntdsutil|CAR-2019-08-002: Active Directory Dumping via NTDSUtil]]
- [[kb/car/analytics/CAR-2020-05-001-minidump_of_lsass|CAR-2020-05-001: MiniDump of LSASS]]
- [[kb/car/analytics/CAR-2021-05-011-create_remote_thread_into_lsass|CAR-2021-05-011: Create Remote Thread into LSASS]]

## [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

- [[kb/car/analytics/CAR-2013-07-001-suspicious_arguments|CAR-2013-07-001: Suspicious Arguments]]
- [[kb/car/analytics/CAR-2019-04-004-credential_dumping_via_mimikatz|CAR-2019-04-004: Credential Dumping via Mimikatz]]
- [[kb/car/analytics/CAR-2019-07-002-lsass_process_dump_via_procdump|CAR-2019-07-002: Lsass Process Dump via Procdump]]
- [[kb/car/analytics/CAR-2019-08-001-credential_dumping_via_windows_task_manager|CAR-2019-08-001: Credential Dumping via Windows Task Manager]]
- [[kb/car/analytics/CAR-2021-05-011-create_remote_thread_into_lsass|CAR-2021-05-011: Create Remote Thread into LSASS]]

## [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

- [[kb/car/analytics/CAR-2019-08-002-active_directory_dumping_via_ntdsutil|CAR-2019-08-002: Active Directory Dumping via NTDSUtil]]
- [[kb/car/analytics/CAR-2020-05-001-minidump_of_lsass|CAR-2020-05-001: MiniDump of LSASS]]

## [[kb/attack/techniques/T1007-system_service_discovery|T1007: System Service Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1010-application_window_discovery|T1010: Application Window Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]]

- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]

## [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1021-remote_services|T1021: Remote Services]]

- [[kb/car/analytics/CAR-2013-01-003-smb_events_monitoring|CAR-2013-01-003: SMB Events Monitoring]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2013-07-001-suspicious_arguments|CAR-2013-07-001: Suspicious Arguments]]
- [[kb/car/analytics/CAR-2013-07-002-rdp_connection_detection|CAR-2013-07-002: RDP Connection Detection]]
- [[kb/car/analytics/CAR-2013-10-001-user_login_activity_monitoring|CAR-2013-10-001: User Login Activity Monitoring]]
- [[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001: RPC Activity]]
- [[kb/car/analytics/CAR-2014-11-004-remote_powershell_sessions|CAR-2014-11-004: Remote PowerShell Sessions]]
- [[kb/car/analytics/CAR-2014-11-006-windows_remote_management_winrm|CAR-2014-11-006: Windows Remote Management (WinRM)]]
- [[kb/car/analytics/CAR-2016-04-005-remote_desktop_logon|CAR-2016-04-005: Remote Desktop Logon]]

## [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

- [[kb/car/analytics/CAR-2013-07-002-rdp_connection_detection|CAR-2013-07-002: RDP Connection Detection]]
- [[kb/car/analytics/CAR-2013-10-001-user_login_activity_monitoring|CAR-2013-10-001: User Login Activity Monitoring]]
- [[kb/car/analytics/CAR-2016-04-005-remote_desktop_logon|CAR-2016-04-005: Remote Desktop Logon]]

## [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]

- [[kb/car/analytics/CAR-2013-01-003-smb_events_monitoring|CAR-2013-01-003: SMB Events Monitoring]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001: RPC Activity]]

## [[kb/attack/techniques/T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]

- [[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001: RPC Activity]]

## [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

- [[kb/car/analytics/CAR-2014-05-001-rpc_activity|CAR-2014-05-001: RPC Activity]]
- [[kb/car/analytics/CAR-2014-11-004-remote_powershell_sessions|CAR-2014-11-004: Remote PowerShell Sessions]]
- [[kb/car/analytics/CAR-2014-11-006-windows_remote_management_winrm|CAR-2014-11-006: Windows Remote Management (WinRM)]]

## [[kb/attack/techniques/T1029-scheduled_transfer|T1029: Scheduled Transfer]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]

- [[kb/car/analytics/CAR-2013-05-002-suspicious_run_locations|CAR-2013-05-002: Suspicious Run Locations]]
- [[kb/car/analytics/CAR-2013-05-009-running_executables_with_same_hash_and_different_names|CAR-2013-05-009: Running executables with same hash and different names]]
- [[kb/car/analytics/CAR-2021-04-001-common_windows_process_masquerading|CAR-2021-04-001: Common Windows Process Masquerading]]

## [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

- [[kb/car/analytics/CAR-2013-05-009-running_executables_with_same_hash_and_different_names|CAR-2013-05-009: Running executables with same hash and different names]]

## [[kb/attack/techniques/T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]

- [[kb/car/analytics/CAR-2021-04-001-common_windows_process_masquerading|CAR-2021-04-001: Common Windows Process Masquerading]]

## [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2020-11-001-boot_or_logon_initialization_scripts|CAR-2020-11-001: Boot or Logon Initialization Scripts]]

## [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts#^t1037001-logon-script-(windows)|T1037.001: Logon Script (Windows)]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2020-11-001-boot_or_logon_initialization_scripts|CAR-2020-11-001: Boot or Logon Initialization Scripts]]

## [[kb/attack/techniques/T1039-data_from_network_shared_drive|T1039: Data from Network Shared Drive]]

- [[kb/car/analytics/CAR-2013-01-003-smb_events_monitoring|CAR-2013-01-003: SMB Events Monitoring]]

## [[kb/attack/techniques/T1040-network_sniffing|T1040: Network Sniffing]]

- [[kb/car/analytics/CAR-2020-11-002-local_network_sniffing|CAR-2020-11-002: Local Network Sniffing]]

## [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2021-01-001-identifying_port_scanning_activity|CAR-2021-01-001: Identifying Port Scanning Activity]]

## [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]

- [[kb/car/analytics/CAR-2014-11-007-remote_windows_management_instrumentation_wmi_over_rpc|CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC]]
- [[kb/car/analytics/CAR-2014-12-001-remotely_launched_executables_via_wmi|CAR-2014-12-001: Remotely Launched Executables via WMI]]
- [[kb/car/analytics/CAR-2016-03-002-create_remote_process_via_wmic|CAR-2016-03-002: Create Remote Process via WMIC]]

## [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1053-scheduled_task_job|T1053: Scheduled Task/Job]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-05-004-execution_with_at|CAR-2013-05-004: Execution with AT]]
- [[kb/car/analytics/CAR-2013-08-001-execution_with_schtasks|CAR-2013-08-001: Execution with schtasks]]
- [[kb/car/analytics/CAR-2015-04-001-remotely_scheduled_tasks_via_at|CAR-2015-04-001: Remotely Scheduled Tasks via AT]]
- [[kb/car/analytics/CAR-2015-04-002-remotely_scheduled_tasks_via_schtasks|CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks]]
- [[kb/car/analytics/CAR-2020-09-001-scheduled_task_fileaccess|CAR-2020-09-001: Scheduled Task - FileAccess]]
- [[kb/car/analytics/CAR-2021-12-001-scheduled_task_creation_or_modification_containing_suspicious_scripts_extensions_or_user_writable_paths|CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths]]

## [[kb/attack/techniques/T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-05-004-execution_with_at|CAR-2013-05-004: Execution with AT]]
- [[kb/car/analytics/CAR-2015-04-001-remotely_scheduled_tasks_via_at|CAR-2015-04-001: Remotely Scheduled Tasks via AT]]

## [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-08-001-execution_with_schtasks|CAR-2013-08-001: Execution with schtasks]]
- [[kb/car/analytics/CAR-2015-04-002-remotely_scheduled_tasks_via_schtasks|CAR-2015-04-002: Remotely Scheduled Tasks via Schtasks]]
- [[kb/car/analytics/CAR-2020-09-001-scheduled_task_fileaccess|CAR-2020-09-001: Scheduled Task - FileAccess]]
- [[kb/car/analytics/CAR-2021-12-001-scheduled_task_creation_or_modification_containing_suspicious_scripts_extensions_or_user_writable_paths|CAR-2021-12-001: Scheduled Task Creation or Modification Containing Suspicious Scripts, Extensions or User Writable Paths]]

## [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

- [[kb/car/analytics/CAR-2013-10-002-dll_injection_via_load_library|CAR-2013-10-002: DLL Injection via Load Library]]
- [[kb/car/analytics/CAR-2020-11-003-dll_injection_with_mavinject|CAR-2020-11-003: DLL Injection with Mavinject]]
- [[kb/car/analytics/CAR-2020-11-004-processes_started_from_irregular_parent|CAR-2020-11-004: Processes Started From Irregular Parent]]

## [[kb/attack/techniques/T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]

- [[kb/car/analytics/CAR-2013-10-002-dll_injection_via_load_library|CAR-2013-10-002: DLL Injection via Load Library]]
- [[kb/car/analytics/CAR-2020-11-003-dll_injection_with_mavinject|CAR-2020-11-003: DLL Injection with Mavinject]]

## [[kb/attack/techniques/T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]

- [[kb/car/analytics/CAR-2020-11-004-processes_started_from_irregular_parent|CAR-2020-11-004: Processes Started From Irregular Parent]]

## [[kb/attack/techniques/T1057-process_discovery|T1057: Process Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

- [[kb/car/analytics/CAR-2013-02-003-processes_spawning_cmd_exe|CAR-2013-02-003: Processes Spawning cmd.exe]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-04-003-powershell_execution|CAR-2014-04-003: Powershell Execution]]
- [[kb/car/analytics/CAR-2014-11-002-outlier_parents_of_cmd|CAR-2014-11-002: Outlier Parents of Cmd]]
- [[kb/car/analytics/CAR-2014-11-004-remote_powershell_sessions|CAR-2014-11-004: Remote PowerShell Sessions]]
- [[kb/car/analytics/CAR-2021-01-002-unusually_long_command_line_strings|CAR-2021-01-002: Unusually Long Command Line Strings]]

## [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

- [[kb/car/analytics/CAR-2014-04-003-powershell_execution|CAR-2014-04-003: Powershell Execution]]
- [[kb/car/analytics/CAR-2014-11-004-remote_powershell_sessions|CAR-2014-11-004: Remote PowerShell Sessions]]

## [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

- [[kb/car/analytics/CAR-2013-02-003-processes_spawning_cmd_exe|CAR-2013-02-003: Processes Spawning cmd.exe]]
- [[kb/car/analytics/CAR-2014-11-002-outlier_parents_of_cmd|CAR-2014-11-002: Outlier Parents of Cmd]]

## [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]

- [[kb/car/analytics/CAR-2021-01-004-unusual_child_process_for_spoolsv_exe_or_connhost_exe|CAR-2021-01-004: Unusual Child Process for Spoolsv.Exe or Connhost.Exe]]

## [[kb/attack/techniques/T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]
- [[kb/car/analytics/CAR-2020-11-006-local_permission_group_discovery|CAR-2020-11-006: Local Permission Group Discovery]]

## [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]
- [[kb/car/analytics/CAR-2020-11-006-local_permission_group_discovery|CAR-2020-11-006: Local Permission Group Discovery]]

## [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]
- [[kb/car/analytics/CAR-2020-11-006-local_permission_group_discovery|CAR-2020-11-006: Local Permission Group Discovery]]

## [[kb/attack/techniques/T1070-indicator_removal|T1070: Indicator Removal]]

- [[kb/car/analytics/CAR-2016-04-002-user_activity_from_clearing_event_logs|CAR-2016-04-002: User Activity from Clearing Event Logs]]
- [[kb/car/analytics/CAR-2020-11-005-clear_powershell_console_command_history|CAR-2020-11-005: Clear Powershell Console Command History]]
- [[kb/car/analytics/CAR-2020-11-007-network_share_connection_removal|CAR-2020-11-007: Network Share Connection Removal]]
- [[kb/car/analytics/CAR-2021-01-003-clearing_windows_logs_with_wevtutil|CAR-2021-01-003: Clearing Windows Logs with Wevtutil]]

## [[kb/attack/techniques/T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]

- [[kb/car/analytics/CAR-2016-04-002-user_activity_from_clearing_event_logs|CAR-2016-04-002: User Activity from Clearing Event Logs]]
- [[kb/car/analytics/CAR-2021-01-003-clearing_windows_logs_with_wevtutil|CAR-2021-01-003: Clearing Windows Logs with Wevtutil]]

## [[kb/attack/techniques/T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]

- [[kb/car/analytics/CAR-2020-11-005-clear_powershell_console_command_history|CAR-2020-11-005: Clear Powershell Console Command History]]

## [[kb/attack/techniques/T1070-indicator_removal#^t1070005-network-share-connection-removal|T1070.005: Network Share Connection Removal]]

- [[kb/car/analytics/CAR-2020-11-007-network_share_connection_removal|CAR-2020-11-007: Network Share Connection Removal]]

## [[kb/attack/techniques/T1078-valid_accounts|T1078: Valid Accounts]]

- [[kb/car/analytics/CAR-2013-02-008-simultaneous_logins_on_a_host|CAR-2013-02-008: Simultaneous Logins on a Host]]
- [[kb/car/analytics/CAR-2013-02-012-user_logged_in_to_multiple_hosts|CAR-2013-02-012: User Logged in to Multiple Hosts]]
- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2013-10-001-user_login_activity_monitoring|CAR-2013-10-001: User Login Activity Monitoring]]

## [[kb/attack/techniques/T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]

- [[kb/car/analytics/CAR-2013-02-008-simultaneous_logins_on_a_host|CAR-2013-02-008: Simultaneous Logins on a Host]]
- [[kb/car/analytics/CAR-2013-02-012-user_logged_in_to_multiple_hosts|CAR-2013-02-012: User Logged in to Multiple Hosts]]
- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2013-10-001-user_login_activity_monitoring|CAR-2013-10-001: User Login Activity Monitoring]]

## [[kb/attack/techniques/T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]

- [[kb/car/analytics/CAR-2013-02-008-simultaneous_logins_on_a_host|CAR-2013-02-008: Simultaneous Logins on a Host]]
- [[kb/car/analytics/CAR-2013-02-012-user_logged_in_to_multiple_hosts|CAR-2013-02-012: User Logged in to Multiple Hosts]]
- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2013-10-001-user_login_activity_monitoring|CAR-2013-10-001: User Login Activity Monitoring]]

## [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

## [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

- [[kb/car/analytics/CAR-2013-07-001-suspicious_arguments|CAR-2013-07-001: Suspicious Arguments]]
- [[kb/car/analytics/CAR-2021-05-005-bitsadmin_download_file|CAR-2021-05-005: BITSAdmin Download File]]
- [[kb/car/analytics/CAR-2021-05-006-certutil_download_with_urlcache_and_split_arguments|CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments]]
- [[kb/car/analytics/CAR-2021-05-007-certutil_download_with_verifyctl_and_split_arguments|CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments]]

## [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-11-005-remote_registry|CAR-2014-11-005: Remote Registry]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-11-001-registry_edit_with_creation_of_safedllsearchmode_key_set_to_0|CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0]]
- [[kb/car/analytics/CAR-2021-11-002-registry_edit_with_modification_of_userinit_shell_or_notify|CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify]]
- [[kb/car/analytics/CAR-2021-12-002-modification_of_default_startup_folder_in_the_registry_key_common_startup|CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup']]

## [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

- [[kb/car/analytics/CAR-2020-11-008-msbuild_and_msxsl|CAR-2020-11-008: MSBuild and msxsl]]

## [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]

- [[kb/car/analytics/CAR-2020-11-008-msbuild_and_msxsl|CAR-2020-11-008: MSBuild and msxsl]]

## [[kb/attack/techniques/T1136-create_account|T1136: Create Account]]

- [[kb/car/analytics/CAR-2021-05-010-create_local_admin_accounts_using_net_exe|CAR-2021-05-010: Create local admin accounts using net exe]]

## [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]

- [[kb/car/analytics/CAR-2021-05-010-create_local_admin_accounts_using_net_exe|CAR-2021-05-010: Create local admin accounts using net exe]]

## [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]

- [[kb/car/analytics/CAR-2021-05-009-certutil_with_decode_argument|CAR-2021-05-009: CertUtil With Decode Argument]]

## [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

- [[kb/car/analytics/CAR-2013-09-003-smb_session_setups|CAR-2013-09-003: SMB Session Setups]]

## [[kb/attack/techniques/T1197-bits_jobs|T1197: BITS Jobs]]

- [[kb/car/analytics/CAR-2021-05-004-bits_job_persistence|CAR-2021-05-004: BITS Job Persistence]]
- [[kb/car/analytics/CAR-2021-05-005-bitsadmin_download_file|CAR-2021-05-005: BITSAdmin Download File]]

## [[kb/attack/techniques/T1204-user_execution|T1204: User Execution]]

- [[kb/car/analytics/CAR-2021-05-002-batch_file_write_to_system32|CAR-2021-05-002: Batch File Write to System32]]

## [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

- [[kb/car/analytics/CAR-2021-05-002-batch_file_write_to_system32|CAR-2021-05-002: Batch File Write to System32]]

## [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

- [[kb/car/analytics/CAR-2014-03-006-rundll32_exe_monitoring|CAR-2014-03-006: RunDLL32.exe monitoring]]
- [[kb/car/analytics/CAR-2019-04-002-generic_regsvr32|CAR-2019-04-002: Generic Regsvr32]]
- [[kb/car/analytics/CAR-2019-04-003-squiblydoo|CAR-2019-04-003: Squiblydoo]]
- [[kb/car/analytics/CAR-2020-11-009-compiled_html_access|CAR-2020-11-009: Compiled HTML Access]]
- [[kb/car/analytics/CAR-2020-11-010-cmstp|CAR-2020-11-010: CMSTP]]

## [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218001-compiled-html-file|T1218.001: Compiled HTML File]]

- [[kb/car/analytics/CAR-2020-11-009-compiled_html_access|CAR-2020-11-009: Compiled HTML Access]]

## [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]

- [[kb/car/analytics/CAR-2020-11-010-cmstp|CAR-2020-11-010: CMSTP]]

## [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]

- [[kb/car/analytics/CAR-2019-04-002-generic_regsvr32|CAR-2019-04-002: Generic Regsvr32]]
- [[kb/car/analytics/CAR-2019-04-003-squiblydoo|CAR-2019-04-003: Squiblydoo]]

## [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

- [[kb/car/analytics/CAR-2014-03-006-rundll32_exe_monitoring|CAR-2014-03-006: RunDLL32.exe monitoring]]

## [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]]

- [[kb/car/analytics/CAR-2019-07-001-access_permission_modification|CAR-2019-07-001: Access Permission Modification]]

## [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]

- [[kb/car/analytics/CAR-2019-07-001-access_permission_modification|CAR-2019-07-001: Access Permission Modification]]

## [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222002-linux-and-mac-file-and-directory-permissions-modification|T1222.002: Linux and Mac File and Directory Permissions Modification]]

- [[kb/car/analytics/CAR-2019-07-001-access_permission_modification|CAR-2019-07-001: Access Permission Modification]]

## [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

- [[kb/car/analytics/CAR-2021-01-009-detecting_shadow_copy_deletion_or_resize|CAR-2021-01-009: Detecting Shadow Copy Deletion or Resize]]
- [[kb/car/analytics/CAR-2021-05-003-bcdedit_failure_recovery_modification|CAR-2021-05-003: BCDEdit Failure Recovery Modification]]

## [[kb/attack/techniques/T1505-server_software_component|T1505: Server Software Component]]

- [[kb/car/analytics/CAR-2021-02-001-webshell_indicative_process_tree|CAR-2021-02-001: Webshell-Indicative Process Tree]]

## [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

- [[kb/car/analytics/CAR-2021-02-001-webshell_indicative_process_tree|CAR-2021-02-001: Webshell-Indicative Process Tree]]

## [[kb/attack/techniques/T1518-software_discovery|T1518: Software Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]

## [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-09-005-service_outlier_executables|CAR-2013-09-005: Service Outlier Executables]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005: Remotely Launched Executables via Services]]
- [[kb/car/analytics/CAR-2014-05-002-services_launching_cmd|CAR-2014-05-002: Services launching Cmd]]

## [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2013-09-005-service_outlier_executables|CAR-2013-09-005: Service Outlier Executables]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005: Remotely Launched Executables via Services]]
- [[kb/car/analytics/CAR-2014-05-002-services_launching_cmd|CAR-2014-05-002: Services launching Cmd]]

## [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2014-11-003-debuggers_for_accessibility_applications|CAR-2014-11-003: Debuggers for Accessibility Applications]]
- [[kb/car/analytics/CAR-2014-11-008-command_launched_from_winlogon|CAR-2014-11-008: Command Launched from WinLogon]]
- [[kb/car/analytics/CAR-2020-09-002-component_object_model_hijacking|CAR-2020-09-002: Component Object Model Hijacking]]
- [[kb/car/analytics/CAR-2020-09-005-appinit_dlls|CAR-2020-09-005: AppInit DLLs]]
- [[kb/car/analytics/CAR-2020-11-011-registry_edit_from_screensaver|CAR-2020-11-011: Registry Edit from Screensaver]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546001-change-default-file-association|T1546.001: Change Default File Association]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]

- [[kb/car/analytics/CAR-2020-11-011-registry_edit_from_screensaver|CAR-2020-11-011: Registry Edit from Screensaver]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2014-11-003-debuggers_for_accessibility_applications|CAR-2014-11-003: Debuggers for Accessibility Applications]]
- [[kb/car/analytics/CAR-2014-11-008-command_launched_from_winlogon|CAR-2014-11-008: Command Launched from WinLogon]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2020-09-005-appinit_dlls|CAR-2020-09-005: AppInit DLLs]]

## [[kb/attack/techniques/T1546-event_triggered_execution#^t1546015-component-object-model-hijacking|T1546.015: Component Object Model Hijacking]]

- [[kb/car/analytics/CAR-2020-09-002-component_object_model_hijacking|CAR-2020-09-002: Component Object Model Hijacking]]

## [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-11-002-registry_edit_with_modification_of_userinit_shell_or_notify|CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify]]
- [[kb/car/analytics/CAR-2021-12-002-modification_of_default_startup_folder_in_the_registry_key_common_startup|CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup']]

## [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-12-002-modification_of_default_startup_folder_in_the_registry_key_common_startup|CAR-2021-12-002: Modification of Default Startup Folder in the Registry Key 'Common Startup']]

## [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2021-11-002-registry_edit_with_modification_of_userinit_shell_or_notify|CAR-2021-11-002: Registry Edit with Modification of Userinit, Shell or Notify]]

## [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547010-port-monitors|T1547.010: Port Monitors]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]

## [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]

- [[kb/car/analytics/CAR-2013-10-002-dll_injection_via_load_library|CAR-2013-10-002: DLL Injection via Load Library]]
- [[kb/car/analytics/CAR-2019-04-001-uac_bypass|CAR-2019-04-001: UAC Bypass]]
- [[kb/car/analytics/CAR-2021-01-008-disable_uac|CAR-2021-01-008: Disable UAC]]
- [[kb/car/analytics/CAR-2021-02-002-get_system_elevation|CAR-2021-02-002: Get System Elevation]]

## [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

- [[kb/car/analytics/CAR-2013-10-002-dll_injection_via_load_library|CAR-2013-10-002: DLL Injection via Load Library]]
- [[kb/car/analytics/CAR-2019-04-001-uac_bypass|CAR-2019-04-001: UAC Bypass]]
- [[kb/car/analytics/CAR-2021-01-008-disable_uac|CAR-2021-01-008: Disable UAC]]

## [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]

- [[kb/car/analytics/CAR-2016-04-004-successful_local_account_login|CAR-2016-04-004: Successful Local Account Login]]

## [[kb/attack/techniques/T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]

- [[kb/car/analytics/CAR-2016-04-004-successful_local_account_login|CAR-2016-04-004: Successful Local Account Login]]

## [[kb/attack/techniques/T1552-unsecured_credentials|T1552: Unsecured Credentials]]

- [[kb/car/analytics/CAR-2020-09-004-credentials_in_files_registry|CAR-2020-09-004: Credentials in Files & Registry]]

## [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

- [[kb/car/analytics/CAR-2020-09-004-credentials_in_files_registry|CAR-2020-09-004: Credentials in Files & Registry]]

## [[kb/attack/techniques/T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

- [[kb/car/analytics/CAR-2020-09-004-credentials_in_files_registry|CAR-2020-09-004: Credentials in Files & Registry]]

## [[kb/attack/techniques/T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]

- [[kb/car/analytics/CAR-2021-05-001-attempt_to_add_certificate_to_untrusted_store|CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store]]

## [[kb/attack/techniques/T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]

- [[kb/car/analytics/CAR-2021-05-001-attempt_to_add_certificate_to_untrusted_store|CAR-2021-05-001: Attempt To Add Certificate To Untrusted Store]]

## [[kb/attack/techniques/T1559-inter-process_communication|T1559: Inter-Process Communication]]

- [[kb/car/analytics/CAR-2021-01-006-unusual_child_process_spawned_using_dde_exploit|CAR-2021-01-006: Unusual Child Process spawned using DDE exploit]]

## [[kb/attack/techniques/T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]

- [[kb/car/analytics/CAR-2021-01-006-unusual_child_process_spawned_using_dde_exploit|CAR-2021-01-006: Unusual Child Process spawned using DDE exploit]]

## [[kb/attack/techniques/T1560-archive_collected_data|T1560: Archive Collected Data]]

- [[kb/car/analytics/CAR-2013-07-005-command_line_usage_of_archiving_software|CAR-2013-07-005: Command Line Usage of Archiving Software]]

## [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

- [[kb/car/analytics/CAR-2013-07-005-command_line_usage_of_archiving_software|CAR-2013-07-005: Command Line Usage of Archiving Software]]

## [[kb/attack/techniques/T1562-impair_defenses|T1562: Impair Defenses]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-04-003-user_activity_from_stopping_windows_defensive_services|CAR-2016-04-003: User Activity from Stopping Windows Defensive Services]]
- [[kb/car/analytics/CAR-2020-09-003-indicator_blocking_driver_unloaded|CAR-2020-09-003: Indicator Blocking - Driver Unloaded]]
- [[kb/car/analytics/CAR-2021-01-007-detecting_tampering_of_windows_defender_command_prompt|CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt]]
- [[kb/car/analytics/CAR-2022-03-001-disable_windows_event_logging|CAR-2022-03-001: Disable Windows Event Logging]]

## [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-04-003-user_activity_from_stopping_windows_defensive_services|CAR-2016-04-003: User Activity from Stopping Windows Defensive Services]]
- [[kb/car/analytics/CAR-2021-01-007-detecting_tampering_of_windows_defender_command_prompt|CAR-2021-01-007: Detecting Tampering of Windows Defender Command Prompt]]

## [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

- [[kb/car/analytics/CAR-2022-03-001-disable_windows_event_logging|CAR-2022-03-001: Disable Windows Event Logging]]

## [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2020-09-003-indicator_blocking_driver_unloaded|CAR-2020-09-003: Indicator Blocking - Driver Unloaded]]

## [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

- [[kb/car/analytics/CAR-2020-08-001-ntfs_alternate_data_stream_execution_system_utilities|CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities]]
- [[kb/car/analytics/CAR-2020-08-002-ntfs_alternate_data_stream_execution_lolbas|CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS]]

## [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

- [[kb/car/analytics/CAR-2020-08-001-ntfs_alternate_data_stream_execution_system_utilities|CAR-2020-08-001: NTFS Alternate Data Stream Execution - System Utilities]]
- [[kb/car/analytics/CAR-2020-08-002-ntfs_alternate_data_stream_execution_lolbas|CAR-2020-08-002: NTFS Alternate Data Stream Execution - LOLBAS]]

## [[kb/attack/techniques/T1569-system_services|T1569: System Services]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005: Remotely Launched Executables via Services]]
- [[kb/car/analytics/CAR-2021-05-012-create_service_in_suspicious_file_path|CAR-2021-05-012: Create Service In Suspicious File Path]]

## [[kb/attack/techniques/T1569-system_services#^t1569001-launchctl|T1569.001: Launchctl]]

- [[kb/car/analytics/CAR-2021-05-012-create_service_in_suspicious_file_path|CAR-2021-05-012: Create Service In Suspicious File Path]]

## [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005: Remotely Launched Executables via Services]]
- [[kb/car/analytics/CAR-2021-05-012-create_service_in_suspicious_file_path|CAR-2021-05-012: Create Service In Suspicious File Path]]

## [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

- [[kb/car/analytics/CAR-2013-05-003-smb_write_request|CAR-2013-05-003: SMB Write Request]]
- [[kb/car/analytics/CAR-2013-05-005-smb_copy_and_execution|CAR-2013-05-005: SMB Copy and Execution]]
- [[kb/car/analytics/CAR-2014-03-001-smb_write_request_namedpipes|CAR-2014-03-001: SMB Write Request - NamedPipes]]

## [[kb/attack/techniques/T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-07-001-service_search_path_interception|CAR-2014-07-001: Service Search Path Interception]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]
- [[kb/car/analytics/CAR-2021-11-001-registry_edit_with_creation_of_safedllsearchmode_key_set_to_0|CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

- [[kb/car/analytics/CAR-2021-11-001-registry_edit_with_creation_of_safedllsearchmode_key_set_to_0|CAR-2021-11-001: Registry Edit with Creation of SafeDllSearchMode Key Set to 0]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2014-07-001-service_search_path_interception|CAR-2014-07-001: Service Search Path Interception]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]

## [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]

- [[kb/car/analytics/CAR-2013-01-002-autorun_differences|CAR-2013-01-002: Autorun Differences]]
- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]

## [[kb/attack/techniques/T1606-forge_web_credentials|T1606: Forge Web Credentials]]

- [[kb/car/analytics/CAR-2021-05-008-certutil_exe_certificate_extraction|CAR-2021-05-008: Certutil exe certificate extraction]]

## [[kb/attack/techniques/T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]

- [[kb/car/analytics/CAR-2021-05-008-certutil_exe_certificate_extraction|CAR-2021-05-008: Certutil exe certificate extraction]]

