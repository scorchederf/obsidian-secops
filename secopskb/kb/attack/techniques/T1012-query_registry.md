---
mitre_id: "T1012"
mitre_name: "Query Registry"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c32f7008-9fea-41f7-8366-5eb9b74bd896"
mitre_created: "2017-05-31T21:30:25.584Z"
mitre_modified: "2025-10-24T17:49:20.660Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1012/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-DI"
  - "D3-RD"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SCP"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [[reg|Reg (S0075)]] utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [[T1012-query_registry|T1012: Query Registry]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Workspace

- [[workspaces/attack/techniques/T1012-query_registry-note|Open workspace note]]

![[workspaces/attack/techniques/T1012-query_registry-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-03-001-reg_exe_called_from_command_shell|CAR-2013-03-001: Reg.exe called from Command Shell]]
- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2020-05-003-rare_lolbas_command_lines|CAR-2020-05-003: Rare LolBAS Command Lines]]

### Sigma Rules

- [[kb/sigma/rules/82880171_b475_4201_b811_e9c826cd5eaa-exports_critical_registry_keys_to_a_file|Exports Critical Registry Keys To a File (high; windows / process_creation)]]
- [[kb/sigma/rules/9a4ff3b8_6187_4fd2_8e8b_e0eae1129495-syskey_registry_keys_access|SysKey Registry Keys Access (high; windows / security)]]
- [[kb/sigma/rules/f8748f2c_89dc_4d95_afb0_5a2dfdbad332-sam_registry_hive_handle_request|SAM Registry Hive Handle Request (high; windows / security)]]
- [[kb/sigma/rules/fca949cc_79ca_446e_8064_01aa7e52ece5-hacktool_pchunter_execution|HackTool - PCHunter Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0434d081_bb32_42ce_bcbb_3548e4f2628f-query_registry_with_powershell_cmdlets|Query Registry with Powershell cmdlets (powershell; windows)]]
- [[kb/atomic/tests/0d80d088_a84c_4353_af1a_fc8b439f1564-enumerate_com_objects_in_registry_with_powershell|Enumerate COM Objects in Registry with Powershell (powershell; windows)]]
- [[kb/atomic/tests/5c784969_1d43_4ac7_8c3d_ed6d025ed10d-check_software_inventory_logging_sil_status_via_registry|Check Software Inventory Logging (SIL) status via Registry (command_prompt; windows)]]
- [[kb/atomic/tests/6fb4c4c5_f949_4fd2_8af5_ddbc61595223-reg_query_for_alwaysinstallelevated_status|Reg query for AlwaysInstallElevated status (command_prompt; windows)]]
- [[kb/atomic/tests/8f7578c4_9863_4d83_875c_a565573bbdf0-query_registry|Query Registry (command_prompt; windows)]]
- [[kb/atomic/tests/96257079_cdc1_4aba_8705_3146e94b6dce-inspect_systemstartoptions_value_in_registry|Inspect SystemStartOptions Value in Registry (command_prompt; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SCP-system_configuration_permissions|D3-SCP: System Configuration Permissions]]

## Tools
- [[pcshare|PcShare (S1050)]]
- [[powersploit|PowerSploit (S0194)]]
- [[reg|Reg (S0075)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Windows

