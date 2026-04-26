---
mitre_id: "T1106"
mitre_name: "Native API"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--391d824f-0ef1-47a0-b0ee-c59a75e27670"
mitre_created: "2017-05-31T21:31:17.472Z"
mitre_modified: "2025-10-24T17:48:39.785Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1106/"
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
  - "TA0002"
d3fend_ids:
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes.(Citation: NT API Windows)(Citation: Linux Kernel API) These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]], the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.

Native API functions (such as `NtCreateProcess`) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries.(Citation: OutFlank System Calls)(Citation: CyberBit System Calls)(Citation: MDSec System Calls) For example, functions such as the Windows API `CreateProcess()` or GNU `fork()` will allow programs and scripts to start other processes.(Citation: Microsoft CreateProcess)(Citation: GNU Fork) This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.(Citation: Microsoft Win32)(Citation: LIBC)(Citation: GLIBC)

Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.(Citation: Microsoft NET)(Citation: Apple Core Services)(Citation: MACOS Cocoa)(Citation: macOS Foundation)

Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks.(Citation: Redops Syscalls) Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]].

## Workspace

- [[workspaces/attack/techniques/T1106-native_api-note|Open workspace note]]

![[workspaces/attack/techniques/T1106-native_api-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/03d83090_8cba_44a0_b02f_0b756a050306-potential_winapi_calls_via_powershell_scripts|Potential WinAPI Calls Via PowerShell Scripts (high; windows / ps_script)]]
- [[kb/sigma/rules/09706624_b7f6_455d_9d02_adee024cee1d-hacktool_cobaltstrike_bof_injection_pattern|HackTool - CobaltStrike BOF Injection Pattern (high; windows / process_access)]]
- [[kb/sigma/rules/808146b2_9332_4d78_9416_d7e47012d83d-bpfdoor_abnormal_process_id_or_lock_file_accessed|BPFDoor Abnormal Process ID or Lock File Accessed (high; linux / auditd)]]
- [[kb/sigma/rules/851fd622_b675_4d26_b803_14bc7baa517a-hacktool_winpwn_execution_scriptblock|HackTool - WinPwn Execution - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/95022b85_ff2a_49fa_939a_d7b8f56eeb9b-hacktool_redmimicry_winnti_playbook_execution|HackTool - RedMimicry Winnti Playbook Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/b1bd3a59_c1fd_4860_9f40_4dd161a7d1f5-hacktool_handlekatz_duplicating_lsass_handle|HackTool - HandleKatz Duplicating LSASS Handle (high; windows / process_access)]]
- [[kb/sigma/rules/ba3f5c1b_6272_4119_9dbd_0bc8d21c2702-potential_winapi_calls_via_commandline|Potential WinAPI Calls Via CommandLine (high; windows / process_creation)]]
- [[kb/sigma/rules/d557dc06_62e8_4468_a8e8_7984124908ce-hacktool_winpwn_execution|HackTool - WinPwn Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/e32f92d1_523e_49c3_9374_bdb13b46a3ba-suspicious_mshta_exe_execution_patterns|Suspicious Mshta.EXE Execution Patterns (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/7ec5b74e_8289_4ff2_a162_b6f286a33abd-winpwn_get_system_shell_bind_system_shell_using_createprocess_technique|WinPwn - Get SYSTEM shell - Bind System Shell using CreateProcess technique (powershell; windows)]]
- [[kb/atomic/tests/99be2089_c52d_4a4a_b5c3_261ee42c8b62-execution_through_api_createprocess|Execution through API - CreateProcess (command_prompt; windows)]]
- [[kb/atomic/tests/ae56083f_28d0_417d_84da_df4242da1f7c-run_shellcode_via_syscall_in_go|Run Shellcode via Syscall in Go (powershell; windows)]]
- [[kb/atomic/tests/ce4e76e6_de70_4392_9efe_b281fc2b4087-winpwn_get_system_shell_pop_system_shell_using_createprocess_technique|WinPwn - Get SYSTEM shell - Pop System Shell using CreateProcess technique (powershell; windows)]]
- [[kb/atomic/tests/e1f93a06_1649_4f07_89a8_f57279a7d60e-winpwn_get_system_shell_pop_system_shell_using_namedpipe_impersonation_technique|WinPwn - Get SYSTEM shell - Pop System Shell using NamedPipe Impersonation technique (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## D3FEND

- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Mitigations

- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[bloodhound|BloodHound (S0521)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[donut|Donut (S0695)]]
- [[empire|Empire (S0363)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[pcshare|PcShare (S1050)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Linux
- macOS
- Windows

