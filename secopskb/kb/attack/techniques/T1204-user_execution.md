---
mitre_id: "T1204"
mitre_name: "User Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--8c32eb4d-805f-4fc5-bf60-c4d476c131b5"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:04.940Z"
mitre_version: "1.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1204/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "IaaS"
  - "Containers"
mitre_tactic_ids:
  - "TA0002"
d3fend_ids:
  - "D3-APCA"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CSPP"
  - "D3-DA"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HD"
  - "D3-IAA"
  - "D3-LFP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RPA"
  - "D3-RTSD"
  - "D3-UA"
  - "D3-UGLPA"
  - "D3-URA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of [[T1566-phishing|T1566: Phishing]].

While [[T1204-user_execution|T1204: User Execution]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[T1534-internal_spearphishing|T1534: Internal Spearphishing]].

Adversaries may also deceive users into performing actions such as:

* Enabling [[T1219-remote_access_tools|T1219: Remote Access Tools]], allowing direct control of the system to the adversary
* Running malicious JavaScript in their browser, allowing adversaries to [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]s(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)
* Downloading and executing malware for [[T1204-user_execution|T1204: User Execution]]
* Coerceing users to copy, paste, and execute malicious code manually(Citation: Reliaquest-execution)(Citation: proofpoint-selfpwn)

For example, tech support scams can be facilitated through [[T1566-phishing|T1566: Phishing]], vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or [[T1219-remote_access_tools|T1219: Remote Access Tools]].(Citation: Telephone Attack Delivery)

## Workspace

- [[workspaces/attack/techniques/T1204-user_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1204-user_execution-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2021-05-002-batch_file_write_to_system32|CAR-2021-05-002: Batch File Write to System32]]

### Sigma Rules

- [[kb/sigma/rules/208748f7_881d_47ac_a29c_07ea84bf691d-suspicious_outlook_child_process|Suspicious Outlook Child Process (high; windows / process_creation)]]
- [[kb/sigma/rules/28208707_fe31_437f_9a7f_4b1108b94d2e-suspicious_startup_folder_persistence|Suspicious Startup Folder Persistence (high; windows / file_event)]]
- [[kb/sigma/rules/3ae9974a_eb09_4044_8e70_8980a50c12c8-suspicious_explorer_process_with_whitespace_padding_clickfix_filefix|Suspicious Explorer Process with Whitespace Padding - ClickFix/FileFix (high; windows / process_creation)]]
- [[kb/sigma/rules/438025f9_5856_4663_83f7_52f878a70a50-suspicious_microsoft_office_child_process|Suspicious Microsoft Office Child Process (high; windows / process_creation)]]
- [[kb/sigma/rules/4922a5dd_6743_4fc2_8e81_144374280997-flash_player_update_from_suspicious_location|Flash Player Update from Suspicious Location (high; proxy)]]
- [[kb/sigma/rules/4fee3d51_8069_4a4c_a0f7_924fcaff2c70-filefix_command_evidence_in_typedpaths|FileFix - Command Evidence in TypedPaths (high; windows / registry_set)]]
- [[kb/sigma/rules/69483748_1525_4a6c_95ca_90dc8d431b68-suspicious_microsoft_office_child_process_macos|Suspicious Microsoft Office Child Process - MacOS (high; macos / process_creation)]]
- [[kb/sigma/rules/7a1b4c5e_8f3d_4b9a_7c2e_1f4a5b8c6d9e-suspicious_space_characters_in_runmru_registry_path_clickfix|Suspicious Space Characters in RunMRU Registry Path - ClickFix (high; windows / registry_set)]]
- [[kb/sigma/rules/7bdde3bf_2a42_4c39_aa31_a92b3e17afac-hacktool_littlecorporal_generated_maldoc_injection|HackTool - LittleCorporal Generated Maldoc Injection (high; windows / process_access)]]
- [[kb/sigma/rules/8a582fe2_0882_4b89_a82a_da6b2dc32937-suspicious_wmiprvse_child_process|Suspicious WmiPrvSE Child Process (high; windows / process_creation)]]
- 14 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/02f35d62_9fdc_4a97_b899_a5d9a876d295-potentially_unwanted_applications_pua|Potentially Unwanted Applications (PUA) (powershell; windows)]]
- [[kb/atomic/tests/0330a5d2_a45a_4272_a9ee_e364411c4b18-maldoc_choice_flags_command_execution|Maldoc choice flags command execution (powershell; windows)]]
- [[kb/atomic/tests/22386853_f68d_4b50_a362_de235127c443-simulate_click_fix_via_downloaded_bat_file|Simulate Click-Fix via Downloaded BAT File (powershell; windows)]]
- [[kb/atomic/tests/24fd9719_7419_42dd_bce6_ab3463110b3c-mirror_blast_emulation|Mirror Blast Emulation (powershell; windows)]]
- [[kb/atomic/tests/3f3120f0_7e50_4be2_88ae_54c61230cb9f-clickfix_campaign_abuse_runmru_to_launch_mshta_via_powershell|ClickFix Campaign - Abuse RunMRU to Launch mshta via PowerShell (powershell; windows)]]
- [[kb/atomic/tests/3f3af983_118a_4fa1_85d3_ba4daa739d80-ostap_payload_download|OSTap Payload Download (command_prompt; windows)]]
- [[kb/atomic/tests/4ea1fc97_8a46_4b4e_ba48_af43d2a98052-excel_4_macro|Excel 4 Macro (powershell; windows)]]
- [[kb/atomic/tests/5202ee05_c420_4148_bf5e_fd7f7d24850c-office_generic_payload_download|Office Generic Payload Download (powershell; windows)]]
- [[kb/atomic/tests/581d7521_9c4b_420e_9695_2aec5241167f-lnk_payload_download|LNK Payload Download (powershell; windows)]]
- [[kb/atomic/tests/8bebc690_18c7_4549_bc98_210f7019efff-ostap_style_macro_execution|OSTap Style Macro Execution (powershell; windows)]]
- 4 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HD-homoglyph_detection|D3-HD: Homoglyph Detection]]
- [[D3-IAA-identifier_activity_analysis|D3-IAA: Identifier Activity Analysis]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UA-url_analysis|D3-UA: URL Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-URA-url_reputation_analysis|D3-URA: URL Reputation Analysis]]

## Subtechniques

### T1204.001: Malicious Link

^t1204001-malicious-link

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]. Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]. Links may also lead users to download files that require execution via [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]].

### T1204.002: Malicious File

^t1204002-malicious-file

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]. Adversaries may use several types of files that require a user to execute them, including .doc, .pdf, .xls, .rtf, .scr, .exe, .lnk, .pif, .cpl, .reg, and .iso.(Citation: Mandiant Trojanized Windows 10)

Adversaries may employ various forms of [[T1036-masquerading|T1036: Masquerading]] and [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]] to increase the likelihood that a user will open and successfully execute a malicious file. These methods may include using a familiar naming convention and/or password protecting the file and supplying instructions to a user on how to open it.(Citation: Password Protected Word Docs) 

While [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]] frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after [[T1534-internal_spearphishing|T1534: Internal Spearphishing]].

### T1204.003: Malicious Image

^t1204003-malicious-image

Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]], and users may then download and deploy an instance or container from the image without realizing the image is malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)

Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container from the image (ex: [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]).(Citation: Aqua Security Cloud Native Threat Report June 2021)

### T1204.004: Malicious Copy and Paste

^t1204004-malicious-copy-and-paste

An adversary may rely upon a user copying and pasting code in order to gain execution. Users may be subjected to social engineering to get them to copy and paste code directly into a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]. One such strategy is "ClickFix," in which adversaries present users with seemingly helpful solutions—such as prompts to fix errors or complete CAPTCHAs—that instead instruct the user to copy and paste malicious code.

Malicious websites, such as those used in [[T1189-drive-by_compromise|T1189: Drive-by Compromise]], may present fake error messages or CAPTCHA prompts that instruct users to open a terminal or the Windows Run Dialog box and execute an arbitrary command. These commands may be obfuscated using encoding or other techniques to conceal malicious intent. Once executed, the adversary will typically be able to establish a foothold on the victim's machine.(Citation: CloudSEK Lumma Stealer 2024)(Citation: Sekoia ClickFake 2025)(Citation: Reliaquest CAPTCHA 2024)(Citation: AhnLab LummaC2 2025)

Adversaries may also leverage phishing emails for this purpose. When a user attempts to open an attachment, they may be presented with a fake error and offered a malicious command to paste as a solution, consistent with the "ClickFix" strategy.(Citation: Proofpoint ClickFix 2024)(Citation: AhnLab Malicioys Copy Paste 2024)

Tricking a user into executing a command themselves may help to bypass email filtering, browser sandboxing, or other mitigations designed to protect users against malicious downloaded files. 

### T1204.005: Malicious Library

^t1204005-malicious-library

Adversaries may rely on a user installing a malicious library to facilitate execution. Threat actors may [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]] to package managers such as NPM and PyPi, as well as to public code repositories such as GitHub. User may install libraries without realizing they are malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that establishes persistence, steals data, or mines cryptocurrency.(Citation: Datadog Security Labs Malicious PyPi Packages 2024)(Citation: Fortinet Malicious NPM Packages 2023)

In some cases, threat actors may compromise and backdoor existing popular libraries (i.e., [[T1195-supply_chain_compromise#^t1195001-compromise-software-dependencies-and-development-tools|T1195.001: Compromise Software Dependencies and Development Tools]]). Alternatively, they may create entirely new packages and leverage behaviors such as typosquatting to encourage users to install them.

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Linux
- Windows
- macOS
- IaaS
- Containers

