---
mitre_id: "T1219"
mitre_name: "Remote Access Tools"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4061e78c-1284-44b4-9116-73e4ac3912f7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:42.154Z"
mitre_version: "3.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1219/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0011"
d3fend_ids:
  - "D3-APCA"
  - "D3-CSPP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RPA"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

An adversary may use legitimate remote access tools to establish an interactive command and control channel within a network. Remote access tools create a session between two trusted hosts through a graphical interface, a command line interaction, a protocol tunnel via development or management software, or hardware-level access such as KVM (Keyboard, Video, Mouse) over IP solutions. Desktop support software (usually graphical interface) and remote management software (typically command line interface) allow a user to control a computer remotely as if they are a local user inheriting the user or software permissions. This software is commonly used for troubleshooting, software installation, and system management.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy) Adversaries may similarly abuse response features included in EDR and other defensive tools that enable remote access.

Remote access tools may be installed and used post-compromise as an alternate communications channel for redundant access or to establish an interactive remote desktop session with the target system. It may also be used as a malware component to establish a reverse connection or back-connect to a service or adversary-controlled system.

Installation of many remote access tools may also include persistence (e.g., the software's installation routine creates a [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]). Remote access modules/features may also exist as part of otherwise existing software (e.g., Google Chrome’s Remote Desktop).(Citation: Google Chrome Remote Desktop)(Citation: Chrome Remote Desktop)

## Workspace

- [[workspaces/attack/techniques/T1219-remote_access_tools-note|Open workspace note]]

![[workspaces/attack/techniques/T1219-remote_access_tools-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/065b00ca_5d5c_4557_ac95_64a6d0b64d86-remote_access_tool_anydesk_execution_from_suspicious_folder|Remote Access Tool - Anydesk Execution From Suspicious Folder (high; windows / process_creation)]]
- [[kb/sigma/rules/114e7f1c_f137_48c8_8f54_3088c24ce4b9-remote_access_tool_anydesk_silent_installation|Remote Access Tool - AnyDesk Silent Installation (high; windows / process_creation)]]
- [[kb/sigma/rules/238527ad_3c2c_4e4f_a1f6_92fd63adb864-antivirus_exploitation_framework_detection|Antivirus Exploitation Framework Detection (critical; antivirus)]]
- [[kb/sigma/rules/2cf29f11_e356_4f61_98c0_1bdb9393d6da-renamed_visual_studio_code_tunnel_execution|Renamed Visual Studio Code Tunnel Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/2d367498_5112_4ae5_a06a_96e7bc33a211-suspicious_binary_writes_via_anydesk|Suspicious Binary Writes Via AnyDesk (high; windows / file_event)]]
- [[kb/sigma/rules/3ab79e90_9fab_4cdf_a7b2_6522bc742adb-hacktool_remotekrbrelay_smb_relay_secrets_dump_module_indicators|HackTool - RemoteKrbRelay SMB Relay Secrets Dump Module Indicators (high; windows / file_event)]]
- [[kb/sigma/rules/4bc90587_e6ca_4b41_be0b_ed4d04e4ed0c-suspicious_velociraptor_child_process|Suspicious Velociraptor Child Process (high; windows / process_creation)]]
- [[kb/sigma/rules/52753ea4_b3a0_4365_910d_36cff487b789-hijack_legit_rdp_session_to_move_laterally|Hijack Legit RDP Session to Move Laterally (high; windows / file_event)]]
- [[kb/sigma/rules/6e22722b_dfb1_4508_a911_49ac840b40f8-suspicious_mstsc_exe_execution_with_local_rdp_file|Suspicious Mstsc.EXE Execution With Local RDP File (high; windows / process_creation)]]
- [[kb/sigma/rules/87261fb2_69d0_42fe_b9de_88c6b5f65a43-atera_agent_installation|Atera Agent Installation (high; windows / application)]]
- 4 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/0ae9e327_3251_465a_a53b_485d4e3f58fa-ammyy_admin_software_execution|Ammyy Admin Software Execution (powershell; windows)]]
- [[kb/atomic/tests/19acf63b_55c4_4b6a_8552_00a8865105c8-ultraviewer_rat_execution|UltraViewer - RAT Execution (powershell; windows)]]
- [[kb/atomic/tests/1aea6d15_70f1_4b4e_8b02_397b5d5ffe75-microsoft_app_quick_assist_execution|Microsoft App Quick Assist Execution (powershell; windows)]]
- [[kb/atomic/tests/1b72b3bd_72f8_4b63_a30b_84e91b9c3578-gotoassist_files_detected_test_on_windows|GoToAssist Files Detected Test on Windows (powershell; windows)]]
- [[kb/atomic/tests/3e1858ee_3550_401c_86ec_5e70ed79295b-splashtop_streamer_execution|Splashtop Streamer Execution (powershell; windows)]]
- [[kb/atomic/tests/42e51815_a6cc_4c75_b970_3f0ff54b610e-ultravnc_execution|UltraVNC Execution (powershell; windows)]]
- [[kb/atomic/tests/4a18cc4e_416f_4966_9a9d_75731c4684c0-screenconnect_application_download_and_install_on_windows|ScreenConnect Application Download and Install on Windows (powershell; windows)]]
- [[kb/atomic/tests/6b8b7391_5c0a_4f8c_baee_78d8ce0ce330-anydesk_files_detected_test_on_windows|AnyDesk Files Detected Test on Windows (powershell; windows)]]
- [[kb/atomic/tests/8ca3b96d_8983_4a7f_b125_fc98cc0a2aa0-teamviewer_files_detected_test_on_windows|TeamViewer Files Detected Test on Windows (powershell; windows)]]
- [[kb/atomic/tests/b025c580_029e_4023_888d_a42710d76934-splashtop_execution|Splashtop Execution (powershell; windows)]]
- 5 more in the generated source index

### LOLBAS Entries

- [[kb/lolbas/entries/honorablementions-code_exe|code.exe (Execute)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1219.001: IDE Tunneling

^t1219001-ide-tunneling

Adversaries may abuse Integrated Development Environment (IDE) software with remote development features to establish an interactive command and control channel on target systems within a network. IDE tunneling combines SSH, port forwarding, file sharing, and debugging into a single secure connection, letting developers work on remote systems as if they were local. Unlike SSH and port forwarding, IDE tunneling encapsulates an entire session and may use proprietary tunneling protocols alongside SSH, allowing adversaries to blend in with legitimate development workflows. Some IDEs, like Visual Studio Code, also provide CLI tools (e.g., `code tunnel`) that adversaries may use to programmatically establish tunnels and generate web-accessible URLs for remote access. These tunnels can be authenticated through accounts such as GitHub, enabling the adversary to control the compromised system via a legitimate developer portal.(Citation: sentinelone operationDigitalEye Dec 2024)(Citation: Unit42 Chinese VSCode 06 September 2024)(Citation: Thornton tutorial VSCode shell September 2023)

Additionally, adversaries may use IDE tunneling for persistence. Some IDEs, such as Visual Studio Code and JetBrains, support automatic reconnection. Adversaries may configure the IDE to auto-launch at startup, re-establishing the tunnel upon execution. Compromised developer machines may also be exploited as jump hosts to move further into the network.

IDE tunneling tools may be built-in or installed as [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]].

### T1219.002: Remote Desktop Software

^t1219002-remote-desktop-software

An adversary may use legitimate desktop support software to establish an interactive command and control channel to target systems within networks. Desktop support software provides a graphical interface for remotely controlling another computer, transmitting the display output, keyboard input, and mouse control between devices using various protocols. Desktop support software, such as `VNC`, `Team Viewer`, `AnyDesk`, `ScreenConnect`, `LogMein`, `AmmyyAdmin`, and other remote monitoring and management (RMM) tools, are commonly used as legitimate technical support software and may be allowed by application control within a target environment.(Citation: Symantec Living off the Land)(Citation: CrowdStrike 2015 Global Threat Report)(Citation: CrySyS Blog TeamSpy) 
 
Remote access modules/features may also exist as part of otherwise existing software such as Zoom or Google Chrome’s Remote Desktop.(Citation: Google Chrome Remote Desktop)(Citation: Chrome Remote Desktop) 

### T1219.003: Remote Access Hardware

^t1219003-remote-access-hardware

An adversary may use legitimate remote access hardware to establish an interactive command and control channel to target systems within networks. These services, including IP-based keyboard, video, or mouse (KVM) devices such as TinyPilot and PiKVM, are commonly used as legitimate tools and may be allowed by peripheral device policies within a target environment.  

Remote access hardware may be physically installed and used post-compromise as an alternate communications channel for redundant access or as a way to establish an interactive remote session with the target system. Using hardware-based remote access tools may allow threat actors to bypass software security solutions and gain more control over the compromised device(s).(Citation: Palo Alto Unit 42 North Korean IT Workers 2024)(Citation: Google Cloud Threat Intelligence DPRK IT Workers 2024)

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

