---
mitre_id: "T1082"
mitre_name: "System Information Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1"
mitre_created: "2017-05-31T21:31:04.307Z"
mitre_modified: "2025-10-24T17:48:38.277Z"
mitre_version: "3.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1082/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-DE"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-HBPI"
  - "D3-PSA"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [[T1680-local_storage_discovery|T1680: Local Storage Discovery]] which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as [[systeminfo|Systeminfo (S0096)]] can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the `systemsetup` configuration tool on macOS. Adversaries may leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather detailed system information (e.g. `show version`).(Citation: US-CERT-TA18-106A) On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: Varonis)

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.(Citation: Amazon Describe Instance)(Citation: Google Instances Resource)(Citation: Microsoft Virutal Machine API)

[[T1082-system_information_discovery|T1082: System Information Discovery]] combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.(Citation: OSX.FairyTale)(Citation: 20 macOS Common Tools and Techniques) 

## Workspace

- [[workspaces/attack/techniques/T1082-system_information_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1082-system_information_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

### Sigma Rules

- [[kb/sigma/rules/7124aebe_4cd7_4ccb_8df0_6d6b93c96795-suspicious_kernel_dump_using_dtrace|Suspicious Kernel Dump Using Dtrace (high; windows / process_creation)]]
- [[kb/sigma/rules/851fd622_b675_4d26_b803_14bc7baa517a-hacktool_winpwn_execution_scriptblock|HackTool - WinPwn Execution - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/98b53e78_ebaf_46f8_be06_421aafd176d9-hacktool_winpeas_execution|HackTool - winPEAS Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/d557dc06_62e8_4468_a8e8_7984124908ce-hacktool_winpwn_execution|HackTool - WinPwn Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/e34cfa0c_0a50_4210_9cb3_5632d08eb041-potential_gobrat_file_discovery_via_grep|Potential GobRAT File Discovery Via Grep (high; linux / process_creation)]]
- [[kb/sigma/rules/e6313acd_208c_44fc_a0ff_db85d572e90e-network_reconnaissance_activity|Network Reconnaissance Activity (high; windows / process_creation)]]
- [[kb/sigma/rules/fca949cc_79ca_446e_8064_01aa7e52ece5-hacktool_pchunter_execution|HackTool - PCHunter Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/034fe21c_3186_49dd_8d5d_128b35f181c7-linux_list_kernel_modules|Linux List Kernel Modules (sh; linux)]]
- [[kb/atomic/tests/07b18a66_6304_47d2_bad0_ef421eb2e107-winpwn_powersharppack_watson_searching_for_missing_windows_patches|WinPwn - PowerSharpPack - Watson searching for missing windows patches (powershell; windows)]]
- [[kb/atomic/tests/2040405c_eea6_4c1c_aef3_c2acc430fac9-esxi_vm_discovery_using_esxcli|ESXi - VM Discovery using ESXCLI (command_prompt; windows)]]
- [[kb/atomic/tests/224b4daf_db44_404e_b6b2_f4d1f0126ef8-windows_machineguid_discovery|Windows MachineGUID Discovery (command_prompt; windows)]]
- [[kb/atomic/tests/26a18d3d_f8bc_486b_9a33_d6df5d78a594-azure_security_scan_with_skyark|Azure Security Scan with SkyArk (powershell; azure-ad)]]
- [[kb/atomic/tests/31dad7ad_2286_4c02_ae92_274418c85fec-linux_vm_check_via_hardware|Linux VM Check via Hardware (bash; linux)]]
- [[kb/atomic/tests/3278b2f6_f733_4875_9ef4_bfed34244f0a-winpwn_morerecon|WinPwn - Morerecon (powershell; windows)]]
- [[kb/atomic/tests/327cc050_9e99_4c8e_99b5_1d15f2fb6b96-show_system_integrity_protection_status_macos|Show System Integrity Protection status (MacOS) (sh; macos)]]
- [[kb/atomic/tests/345cb8e4_d2de_4011_a580_619cf5a9e2d7-winpwn_powersploits_privesc_checks|WinPwn - Powersploits privesc checks (powershell; windows)]]
- [[kb/atomic/tests/3d256a2f_5e57_4003_8eb6_64d91b1da7ce-winpwn_itm4nprivesc|WinPwn - itm4nprivesc (powershell; windows)]]
- 30 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DE-decoy_environment|D3-DE: Decoy Environment]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools
- [[cmd|cmd (S0106)]]
- [[covenant|Covenant (S1155)]]
- [[dsquery|dsquery (S0105)]]
- [[empire|Empire (S0363)]]
- [[koadic|Koadic (S0250)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[systeminfo|Systeminfo (S0096)]]


## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Network Devices
- Windows

