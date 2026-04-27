---
mitre_id: "T1569"
mitre_name: "System Services"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d157f9d2-d09a-4efa-bb2a-64963f94e253"
mitre_created: "2020-03-10T18:23:06.482Z"
mitre_modified: "2025-10-24T17:49:25.548Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1569/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may abuse system services or daemons to execute commands or programs. Adversaries can execute malicious content by interacting with or creating services either locally or remotely. Many services are set to run at boot, which can aid in achieving persistence ([[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]), but adversaries can also abuse services for one-time or temporary execution.

## Workspace

- [[workspaces/attack/techniques/T1569-system_services-note|Open workspace note]]

![[workspaces/attack/techniques/T1569-system_services-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2014-02-001-service_binary_modifications|CAR-2014-02-001: Service Binary Modifications]]
- [[kb/car/analytics/CAR-2014-03-005-remotely_launched_executables_via_services|CAR-2014-03-005: Remotely Launched Executables via Services]]
- [[kb/car/analytics/CAR-2021-05-012-create_service_in_suspicious_file_path|CAR-2021-05-012: Create Service In Suspicious File Path]]

### Sigma Rules

- [[kb/sigma/rules/10018e73_06ec_46ec_8107_9172f1e04ff2-remote_server_service_abuse_for_lateral_movement|Remote Server Service Abuse for Lateral Movement (high; rpc_firewall / application)]]
- [[kb/sigma/rules/2a926e6a_4b81_4011_8a96_e36cc8c04302-powershell_scripts_installed_as_services_security|PowerShell Scripts Installed as Services - Security (high; windows / security)]]
- [[kb/sigma/rules/31c51af6_e7aa_4da7_84d4_8f32cc580af2-sliver_c2_default_service_installation|Sliver C2 Default Service Installation (high; windows / system)]]
- [[kb/sigma/rules/4976aa50_8f41_45c6_8b15_ab3fc10e79ed-credential_dumping_tools_service_execution_system|Credential Dumping Tools Service Execution - System (high; windows / system)]]
- [[kb/sigma/rules/4a5f5a5e_ac01_474b_9b4e_d61298c9df1d-powershell_as_a_service_in_registry|PowerShell as a Service in Registry (high; windows / registry_set)]]
- [[kb/sigma/rules/52a85084_6989_40c3_8f32_091e12e13f09-smbexec_py_service_installation|smbexec.py Service Installation (high; windows / system)]]
- [[kb/sigma/rules/5a105d34_05fc_401e_8553_272b45c1522d-cobaltstrike_service_installations_system|CobaltStrike Service Installations - System (critical; windows / system)]]
- [[kb/sigma/rules/5bb68627_3198_40ca_b458_49f973db8752-rundll32_execution_without_parameters|Rundll32 Execution Without Parameters (high; windows / process_creation)]]
- [[kb/sigma/rules/61a7697c_cb79_42a8_a2ff_5f0cdfae0130-potential_cobaltstrike_service_installations_registry|Potential CobaltStrike Service Installations - Registry (high; windows / registry_set)]]
- [[kb/sigma/rules/6fb63b40_e02a_403e_9ffd_3bcc1d749442-metasploit_or_impacket_service_installation_via_smb_psexec|Metasploit Or Impacket Service Installation Via SMB PsExec (high; windows / security)]]
- 11 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/004a5d68_627b_452d_af3d_43bd1fc75a3b-pipe_creation_psexec_tool_execution_from_suspicious_locations|Pipe Creation - PsExec Tool Execution From Suspicious Locations (powershell; windows)]]
- [[kb/atomic/tests/1e5be8d4_605a_4acb_8709_2f80b2d8ea95-enumerate_all_systemd_services_using_systemctl|Enumerate All systemd Services Using systemctl (sh; linux)]]
- [[kb/atomic/tests/2382dee2_a75f_49aa_9378_f52df6ed3fb1-execute_a_command_as_a_service|Execute a Command as a Service (command_prompt; windows)]]
- [[kb/atomic/tests/2fc6c0ab_4f88_4eb8_ab1b_f739fc22bba7-enable_systemd_service_for_persistence_with_auto_restart|Enable systemd Service for Persistence with Auto-Restart (sh; linux)]]
- [[kb/atomic/tests/31eb7828_97d7_4067_9c1e_c6feb85edc4b-blackcat_pre_encryption_cmds_with_lateral_movement|BlackCat pre-encryption cmds with Lateral Movement (powershell; windows)]]
- [[kb/atomic/tests/6123928f_6389_4914_8d25_a5d69bd657fa-modify_existing_systemd_service_to_execute_malicious_command|Modify Existing systemd Service to Execute Malicious Command (sh; linux)]]
- [[kb/atomic/tests/6fb61988_724e_4755_a595_07743749d4e2-launchctl|Launchctl (bash; macos)]]
- [[kb/atomic/tests/6fec8560_ff64_4bbf_bc79_734fea48f7ca-masquerade_malicious_service_as_legitimate_system_service|Masquerade Malicious Service as Legitimate System Service (sh; linux)]]
- [[kb/atomic/tests/873106b7_cfed_454b_8680_fa9f6400431c-use_psexec_to_execute_a_command_on_a_remote_host|Use PsExec to execute a command on a remote host (command_prompt; windows)]]
- [[kb/atomic/tests/a1fa406e_2354_4a24_b6d6_94157e7564d4-create_systemd_service_unit_from_tmp_unusual_location|Create systemd Service Unit from /tmp (Unusual Location) (sh; linux)]]
- 7 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Subtechniques

### T1569.001: Launchctl

^t1569001-launchctl

Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input.(Citation: Launchctl Man)

Adversaries use launchctl to execute commands and programs as [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]s or [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]s. Common subcommands include: `launchctl load`,`launchctl unload`, and `launchctl start`. Adversaries can use scripts or manually run the commands `launchctl load -w "%s/Library/LaunchAgents/%s"` or `/bin/launchctl load` to execute [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]s or [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]s.(Citation: Sofacy Komplex Trojan)(Citation: 20 macOS Common Tools and Techniques)


### T1569.002: Service Execution

^t1569002-service-execution

Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (`services.exe`) is an interface to manage and manipulate services.(Citation: Microsoft Service Control Manager) The service control manager is accessible to users via GUI components as well as system utilities such as `sc.exe` and [[net|Net (S0039)]].

[[psexec|PsExec (S0029)]] can also be used to execute commands or payloads via a temporary Windows service created through the service control manager API.(Citation: Russinovich Sysinternals) Tools such as [[psexec|PsExec (S0029)]] and `sc.exe` can accept remote servers as arguments and may be used to conduct remote execution.

Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified service. This technique is the execution used in conjunction with [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]] during service persistence or privilege escalation.

### T1569.003: Systemctl

^t1569003-systemctl

Adversaries may abuse systemctl to execute commands or programs. Systemctl is the primary interface for systemd, the Linux init system and service manager. Typically invoked from a shell, Systemctl can also be integrated into scripts or applications.   

Adversaries may use systemctl to execute commands or programs as [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]s. Common subcommands include: `systemctl start`, `systemctl stop`, `systemctl enable`, `systemctl disable`, and `systemctl status`.(Citation: Red Hat Systemctl 2022)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Windows
- macOS
- Linux

