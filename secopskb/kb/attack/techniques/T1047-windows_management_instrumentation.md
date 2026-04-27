---
mitre_id: "T1047"
mitre_name: "Windows Management Instrumentation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--01a5a209-b94c-450b-b7f9-946497d91055"
mitre_created: "2017-05-31T21:30:44.329Z"
mitre_modified: "2025-10-24T17:48:19.670Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1047/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
d3fend_ids:
  - "D3-ANAA"
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CSPP"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-PSA"
  - "D3-RTSD"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI 1-3) WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by [[T1021-remote_services|T1021: Remote Services]] such as [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]] and [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]].(Citation: WMI 1-3) Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.(Citation: WMI 1-3) (Citation: Mandiant WMI)

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [[TA0007-discovery|TA0007: Discovery]] as well as [[TA0002-execution|TA0002: Execution]] of commands and payloads.(Citation: Mandiant WMI) For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]).(Citation: WMI 6)

**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] as the primary WMI interface.(Citation: WMI 7,8) In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.(Citation: WMI 7,8)

## Workspace

- [[workspaces/attack/techniques/T1047-windows_management_instrumentation-note|Open workspace note]]

![[workspaces/attack/techniques/T1047-windows_management_instrumentation-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2014-11-007-remote_windows_management_instrumentation_wmi_over_rpc|CAR-2014-11-007: Remote Windows Management Instrumentation (WMI) over RPC]]
- [[kb/car/analytics/CAR-2014-12-001-remotely_launched_executables_via_wmi|CAR-2014-12-001: Remotely Launched Executables via WMI]]
- [[kb/car/analytics/CAR-2016-03-002-create_remote_process_via_wmic|CAR-2016-03-002: Create Remote Process via WMIC]]

### Sigma Rules

- [[kb/sigma/rules/058f4380_962d_40a5_afce_50207d36d7e2-hacktool_crackmapexec_execution_patterns|HackTool - CrackMapExec Execution Patterns (high; windows / process_creation)]]
- [[kb/sigma/rules/10c14723_61c7_4c75_92ca_9af245723ad2-hacktool_potential_impacket_lateral_movement_activity|HackTool - Potential Impacket Lateral Movement Activity (high; windows / process_creation)]]
- [[kb/sigma/rules/3c89a1e8_0fba_449e_8f1b_8409d6267ec8-suspicious_process_created_via_wmic_exe|Suspicious Process Created Via Wmic.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/42a993dd_bb3e_48c8_b372_4d6684c4106c-hacktool_crackmapexec_execution|HackTool - CrackMapExec Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/438025f9_5856_4663_83f7_52f878a70a50-suspicious_microsoft_office_child_process|Suspicious Microsoft Office Child Process (high; windows / process_creation)]]
- [[kb/sigma/rules/51cbac1e_eee3_4a90_b1b7_358efb81fa0a-potential_windows_defender_tampering_via_wmic_exe|Potential Windows Defender Tampering Via Wmic.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/52cad028_0ff0_4854_8f67_d25dfcbc78b4-html_help_hh_exe_suspicious_child_process|HTML Help HH.EXE Suspicious Child Process (high; windows / process_creation)]]
- [[kb/sigma/rules/614a7e17_5643_4d89_b6fe_f9df1a79641c-wmiprvse_wbemcomn_dll_hijack_file|Wmiprvse Wbemcomn DLL Hijack - File (critical; windows / file_event)]]
- [[kb/sigma/rules/68050b10_e477_4377_a99b_3721b422d6ef-remote_dcom_wmi_lateral_movement|Remote DCOM/WMI Lateral Movement (high; rpc_firewall / application)]]
- [[kb/sigma/rules/7707a579_e0d8_4886_a853_ce47e4575aaa-wmiprvse_wbemcomn_dll_hijack|Wmiprvse Wbemcomn DLL Hijack (high; windows / image_load)]]
- 11 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/00738d2a_4651_4d76_adf2_c43a41dfb243-wmi_execute_rundll32|WMI Execute rundll32 (command_prompt; windows)]]
- [[kb/atomic/tests/0fd48ef7_d890_4e93_a533_f7dedd5191d3-wmi_reconnaissance_list_remote_services|WMI Reconnaissance List Remote Services (command_prompt; windows)]]
- [[kb/atomic/tests/10447c83_fc38_462a_a936_5102363b1c43-create_a_process_using_obfuscated_win32_process|Create a Process using obfuscated Win32_Process (powershell; windows)]]
- [[kb/atomic/tests/5750aa16_0e59_4410_8b9a_8a47ca2788e2-wmi_reconnaissance_processes|WMI Reconnaissance Processes (command_prompt; windows)]]
- [[kb/atomic/tests/718aebaa_d0e0_471a_8241_c5afa69c7414-wmi_reconnaissance_software|WMI Reconnaissance Software (command_prompt; windows)]]
- [[kb/atomic/tests/7db7a7f9_9531_4840_9b30_46220135441c-create_a_process_using_wmi_query_and_an_encoded_command|Create a Process using WMI Query and an Encoded Command (command_prompt; windows)]]
- [[kb/atomic/tests/9c8ef159_c666_472f_9874_90c8d60d136b-wmi_execute_remote_process|WMI Execute Remote Process (command_prompt; windows)]]
- [[kb/atomic/tests/b3bdfc91_b33e_4c6d_a5c8_d64bee0276b3-wmi_execute_local_process|WMI Execute Local Process (command_prompt; windows)]]
- [[kb/atomic/tests/c107778c_dcf5_47c5_af2e_1d058a3df3ea-wmi_reconnaissance_users|WMI Reconnaissance Users (command_prompt; windows)]]
- [[kb/atomic/tests/c510d25b_1667_467d_8331_a56d3e9bc4ff-application_uninstall_using_wmic|Application uninstall using WMIC (command_prompt; windows)]]

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-wbemtest_exe|wbemtest.exe (Execute)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## D3FEND

- [[D3-ANAA-administrative_network_activity_analysis|D3-ANAA: Administrative Network Activity Analysis]]
- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[covenant|Covenant (S1155)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[impacket|Impacket (S0357)]]
- [[koadic|Koadic (S0250)]]
- [[poshc2|PoshC2 (S0378)]]
- [[powersploit|PowerSploit (S0194)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Windows

