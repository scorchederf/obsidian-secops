---
mitre_id: "T1127"
mitre_name: "Trusted Developer Utilities Proxy Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ff25900d-76d5-449b-a351-8824e62fc81b"
mitre_created: "2017-05-31T21:31:39.262Z"
mitre_modified: "2025-10-24T17:49:40.055Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1127/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-AVE"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RS"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation: Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them.(Citation: Microsoft Smart App Control) However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]] to run their malicious code, adversaries may bypass Smart App Control protections.(Citation: Elastic Security Labs)

## Workspace

- [[workspaces/attack/techniques/T1127-trusted_developer_utilities_proxy_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1127-trusted_developer_utilities_proxy_execution-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2020-11-008-msbuild_and_msxsl|CAR-2020-11-008: MSBuild and msxsl]]

### Sigma Rules

- [[kb/sigma/rules/50e54b8d_ad73_43f8_96a1_5191685b17a4-silenttrinity_stager_msbuild_activity|Silenttrinity Stager Msbuild Activity (high; windows / network_connection)]]
- [[kb/sigma/rules/6640f31c_01ad_49b5_beb5_83498a5cd8bd-potential_arbitrary_code_execution_via_node_exe|Potential Arbitrary Code Execution Via Node.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/9ccba514_7cb6_4c5c_b377_700758f2f120-suspicious_child_process_of_aspnetcompiler|Suspicious Child Process of AspNetCompiler (high; windows / process_creation)]]
- [[kb/sigma/rules/9f50fe98_fe5c_4a2d_86c7_fad7f63ed622-potentially_suspicious_asp_net_compilation_via_aspnetcompiler|Potentially Suspicious ASP.NET Compilation Via AspNetCompiler (high; windows / process_creation)]]
- [[kb/sigma/rules/a9e416a8_e613_4f8b_88b8_a7d1d1af2f61-suspicious_use_of_csharp_interactive_console|Suspicious Use of CSharp Interactive Console (high; windows / process_creation)]]
- [[kb/sigma/rules/c15e99a3_c474_48ab_b9a7_84549a7a9d16-remote_thread_creation_ttdinject_exe_proxy|Remote Thread Creation Ttdinject.exe Proxy (high; windows / create_remote_thread)]]
- [[kb/sigma/rules/d047726b_c71c_4048_a99b_2e2f50dc107d-kavremover_dropped_binary_lolbin_usage|Kavremover Dropped Binary LOLBIN Usage (high; windows / process_creation)]]
- [[kb/sigma/rules/e890acee_d488_420e_8f20_d9b19b3c3d43-suspicious_file_created_by_arcsoc_exe|Suspicious File Created by ArcSOC.exe (high; windows / file_event)]]

### Atomic Tests

- [[kb/atomic/tests/1ec1c269_d6bd_49e7_b71b_a461f7fa7bc8-lolbin_jsc_exe_compile_javascript_to_exe|Lolbin Jsc.exe compile javascript to exe (command_prompt; windows)]]
- [[kb/atomic/tests/3fc9fea2_871d_414d_8ef6_02e85e322b80-lolbin_jsc_exe_compile_javascript_to_dll|Lolbin Jsc.exe compile javascript to dll (command_prompt; windows)]]
- [[kb/atomic/tests/58742c0f_cb01_44cd_a60b_fb26e8871c93-msbuild_bypass_using_inline_tasks_c|MSBuild Bypass Using Inline Tasks (C#) (command_prompt; windows)]]
- [[kb/atomic/tests/ab042179_c0c5_402f_9bc8_42741f5ce359-msbuild_bypass_using_inline_tasks_vb|MSBuild Bypass Using Inline Tasks (VB) (command_prompt; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Subtechniques

### T1127.001: MSBuild

^t1127001-msbuild

Adversaries may use MSBuild to proxy execution of code through a trusted Windows utility. MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It handles XML formatted project files that define requirements for loading and building various platforms and configurations.(Citation: MSDN MSBuild)

Adversaries can abuse MSBuild to proxy execution of malicious code. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# or Visual Basic code to be inserted into an XML project file.(Citation: MSDN MSBuild)(Citation: Microsoft MSBuild Inline Tasks 2017) MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application control defenses that are configured to allow MSBuild.exe execution.(Citation: LOLBAS Msbuild)

### T1127.002: ClickOnce

^t1127002-clickonce

Adversaries may use ClickOnce applications (.appref-ms and .application files) to proxy execution of code through a trusted Windows utility.(Citation: Burke/CISA ClickOnce BlackHat) ClickOnce is a deployment that enables a user to create self-updating Windows-based .NET applications (i.e, .XBAP, .EXE, or .DLL) that install and run from a file share or web page with minimal user interaction. The application launches as a child process of DFSVC.EXE, which is responsible for installing, launching, and updating the application.(Citation: SpectorOps Medium ClickOnce)

Because ClickOnce applications receive only limited permissions, they do not require administrative permissions to install.(Citation: Microsoft Learn ClickOnce) As such, adversaries may abuse ClickOnce to proxy execution of malicious code without needing to escalate privileges.

ClickOnce may be abused in a number of ways. For example, an adversary may rely on [[T1204-user_execution|T1204: User Execution]]. When a user visits a malicious website, the .NET malware is disguised as legitimate software and a ClickOnce popup is displayed for installation.(Citation: NetSPI ClickOnce)

Adversaries may also abuse ClickOnce to execute malware via a [[T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]] script using the command `rundll32.exe dfshim.dll,ShOpenVerbApplication1`.(Citation: LOLBAS /Dfsvc.exe)

Additionally, an adversary can move the ClickOnce application file to a remote user’s startup folder for continued malicious code deployment (i.e., [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]).(Citation: Burke/CISA ClickOnce BlackHat)(Citation: Burke/CISA ClickOnce Paper)

### T1127.003: JamPlus

^t1127003-jamplus

Adversaries may use `JamPlus` to proxy the execution of a malicious script. `JamPlus` is a build utility tool for code and data build systems. It works with several popular compilers and can be used for generating workspaces in code editors such as Visual Studio.(Citation: JamPlus manual)

Adversaries may abuse the `JamPlus` build utility to execute malicious scripts via a `.jam` file, which describes the build process and required dependencies. Because the malicious script is executed from a reputable developer tool, it may subvert application control security systems such as Smart App Control.(Citation: Cyble)(Citation: Elastic Security Labs)

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Windows

