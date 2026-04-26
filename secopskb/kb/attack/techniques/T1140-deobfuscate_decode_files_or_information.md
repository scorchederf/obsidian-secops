---
mitre_id: "T1140"
mitre_name: "Deobfuscate/Decode Files or Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3ccef7ae-cb5e-48f6-8302-897105fbf55c"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:48:40.925Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1140/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-AEM"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-LFP"
  - "D3-OPM"
  - "D3-PSA"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]] to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.

One such example is the use of [[certutil|certutil (S0160)]] to decode a remote access tool portable executable file that has been hidden inside a certificate file.(Citation: Malwarebytes Targeted Attack against Saudi Arabia) Another example is using the Windows `copy /b` or `type` command to reassemble binary fragments into a malicious payload.(Citation: Carbon Black Obfuscation Sept 2016)(Citation: Sentinel One Tainted Love 2023)

Sometimes a user's action may be required to open it for deobfuscation or decryption as part of [[T1204-user_execution|T1204: User Execution]]. The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.(Citation: Volexity PowerDuke November 2016)

## Workspace

- [[workspaces/attack/techniques/T1140-deobfuscate_decode_files_or_information-note|Open workspace note]]

![[workspaces/attack/techniques/T1140-deobfuscate_decode_files_or_information-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2021-05-009-certutil_with_decode_argument|CAR-2021-05-009: CertUtil With Decode Argument]]

### Sigma Rules

- [[kb/sigma/rules/09a910bf_f71f_4737_9c40_88880ba5913d-potential_base64_decoded_from_images|Potential Base64 Decoded From Images (high; macos / process_creation)]]
- [[kb/sigma/rules/1a0d4aba_7668_4365_9ce4_6d79ab088dfd-ping_hex_ip|Ping Hex IP (high; windows / process_creation)]]
- [[kb/sigma/rules/cc7abbd0_762b_41e3_8a26_57ad50d2eea3-mshta_execution_with_suspicious_file_extensions|MSHTA Execution with Suspicious File Extensions (high; windows / process_creation)]]
- [[kb/sigma/rules/ceb55fd0_726e_4656_bf4e_b585b7f7d572-suspicious_inbox_manipulation_rules|Suspicious Inbox Manipulation Rules (high; azure / riskdetection)]]
- [[kb/sigma/rules/e32d4572_9826_4738_b651_95fa63747e8a-base64_encoded_powershell_command_detected|Base64 Encoded PowerShell Command Detected (high; windows / process_creation)]]
- [[kb/sigma/rules/fdb62a13_9a81_4e5c_a38f_ea93a16f6d7c-powershell_base64_encoded_frombase64string_cmdlet|PowerShell Base64 Encoded FromBase64String Cmdlet (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/005943f9_8dd5_4349_8b46_0313c0a9f973-hex_decoding_with_shell_utilities|Hex decoding with shell utilities (sh; linux, macos)]]
- [[kb/atomic/tests/18ee2002_66e8_4518_87c5_c0ec9c8299ac-freebsd_b64encode_shebang_in_cli|FreeBSD b64encode Shebang in CLI (sh; linux)]]
- [[kb/atomic/tests/356dc0e8_684f_4428_bb94_9313998ad608-base64_decoding_with_python|Base64 decoding with Python (sh; linux, macos)]]
- [[kb/atomic/tests/3a15c372_67c1_4430_ac8e_ec06d641ce4d-linux_base64_encoded_shebang_in_cli|Linux Base64 Encoded Shebang in CLI (sh; linux, macos)]]
- [[kb/atomic/tests/6604d964_b9f6_4d4b_8ce8_499829a14d0a-base64_decoding_with_perl|Base64 decoding with Perl (sh; linux, macos)]]
- [[kb/atomic/tests/71abc534_3c05_4d0c_80f7_cbe93cb2aa94-certutil_rename_and_decode|Certutil Rename and Decode (command_prompt; windows)]]
- [[kb/atomic/tests/9f8b1c54_cb76_4d5e_bb1f_2f5c0e8f5a11-expand_cab_with_expand_exe|Expand CAB with expand.exe (command_prompt; windows)]]
- [[kb/atomic/tests/b4f6a567_a27a_41e5_b8ef_ac4b4008bb7e-base64_decoding_with_shell_utilities|Base64 decoding with shell utilities (sh; linux, macos)]]
- [[kb/atomic/tests/b6097712_c42e_4174_b8f2_4b1e1a5bbb3d-base64_decoding_with_shell_utilities_freebsd|Base64 decoding with shell utilities (freebsd) (sh; linux)]]
- [[kb/atomic/tests/c3b65cd5_ee51_4e98_b6a3_6cbdec138efc-xor_decoding_and_command_execution_using_python|XOR decoding and command execution using Python (bash; linux, macos)]]
- 1 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[certutil|certutil (S0160)]]
- [[expand|Expand (S0361)]]
- [[imminent_monitor|Imminent Monitor (S0434)]]
- [[ironnetinjector|IronNetInjector (S0581)]]
- [[pcshare|PcShare (S1050)]]


## Platforms

- ESXi
- Linux
- macOS
- Windows

