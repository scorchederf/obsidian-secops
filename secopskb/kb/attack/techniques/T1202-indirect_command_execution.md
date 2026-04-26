---
mitre_id: "T1202"
mitre_name: "Indirect Command Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3b0e52ce-517a-4614-a523-1bd5deef6c5e"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:40.495Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1202/"
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
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking [[cmd|cmd (S0106)]]. For example, [[forfiles|Forfiles (S0193)]], the Program Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well as other utilities may invoke the execution of programs and commands from a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]], Run window, or via scripts.(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)(Citation: Secure Team - Scriptrunner.exe)(Citation: SS64)(Citation: Bleeping Computer - Scriptrunner.exe) Adversaries may also abuse the `ssh.exe` binary to execute malicious commands via the `ProxyCommand` and `LocalCommand` options, which can be invoked via the `-o` flag or by modifying the SSH config file.(Citation: Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot)

Adversaries may abuse these features for [[TA0005-defense_evasion|TA0005: Defense Evasion]], specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of [[cmd|cmd (S0106)]] or file extensions more commonly associated with malicious payloads.

## Workspace

- [[workspaces/attack/techniques/T1202-indirect_command_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1202-indirect_command_execution-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/1775e15e_b61b_4d14_a1a3_80981298085a-rundll32_execution_without_commandline_parameters|Rundll32 Execution Without CommandLine Parameters (high; windows / process_creation)]]
- [[kb/sigma/rules/1f1a8509_2cbb_44f5_8751_8e1571518ce2-suspicious_splwow64_without_params|Suspicious Splwow64 Without Params (high; windows / process_creation)]]
- [[kb/sigma/rules/2433a154_bb3d_42e4_86c3_a26bdac91c45-renamed_pingcastle_binary_execution|Renamed PingCastle Binary Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/258fc8ce_8352_443a_9120_8a11e4857fa5-potential_arbitrary_command_execution_using_msdt_exe|Potential Arbitrary Command Execution Using Msdt.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/264982dc_dbad_4dce_b707_1e0d3e0f73d9-renamed_nircmd_exe_execution|Renamed NirCmd.EXE Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/340a090b_c4e9_412e_bb36_b4b16fe96f9b-renamed_zoho_dctask64_execution|Renamed ZOHO Dctask64 Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/4ae3e30b_b03f_43aa_87e3_b622f4048eed-potential_arbitrary_file_download_using_office_application|Potential Arbitrary File Download Using Office Application (high; windows / process_creation)]]
- [[kb/sigma/rules/55f0a3a1_846e_40eb_8273_677371b8d912-outlook_enableunsafeclientmailrules_setting_enabled|Outlook EnableUnsafeClientMailRules Setting Enabled (high; windows / process_creation)]]
- [[kb/sigma/rules/6f1a11aa_4b8a_4b7f_9e13_4d3e4ff0e0d4-wsl_kali_linux_usage|WSL Kali-Linux Usage (high; windows / process_creation)]]
- [[kb/sigma/rules/7530b96f_ad8e_431d_a04d_ac85cc461fdc-custom_file_open_handler_executes_powershell|Custom File Open Handler Executes PowerShell (high; windows / registry_set)]]
- 8 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/0fd14730_6226_4f5e_8d67_43c65f1be940-indirect_command_execution_scriptrunner_exe|Indirect Command Execution - Scriptrunner.exe (powershell; windows)]]
- [[kb/atomic/tests/8b34a448_40d9_4fc3_a8c8_4bb286faf7dc-indirect_command_execution_forfiles_exe|Indirect Command Execution - forfiles.exe (command_prompt; windows)]]
- [[kb/atomic/tests/cecfea7a_5f03_4cdd_8bc8_6f7c22862440-indirect_command_execution_pcalua_exe|Indirect Command Execution - pcalua.exe (command_prompt; windows)]]
- [[kb/atomic/tests/cf3391e0_b482_4b02_87fc_ca8362269b29-indirect_command_execution_conhost_exe|Indirect Command Execution - conhost.exe (command_prompt; windows)]]
- [[kb/atomic/tests/de323a93_2f18_4bd5_ba60_d6fca6aeff76-indirect_command_execution_runmru_dialog|Indirect Command Execution - RunMRU Dialog (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Tools

- [[forfiles|Forfiles (S0193)]]

## Platforms

- Windows

