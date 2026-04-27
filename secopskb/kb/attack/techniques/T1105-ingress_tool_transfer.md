---
mitre_id: "T1105"
mitre_name: "Ingress Tool Transfer"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e6919abc-99f9-4c6c-95a5-14761e7b2add"
mitre_created: "2017-05-31T21:31:16.408Z"
mitre_modified: "2025-10-24T17:49:32.714Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1105/"
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
  - "Network Devices"
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

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [[ftp|ftp (S0095)]]. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]). 

On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [[certutil|certutil (S0160)]], and [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] commands such as `IEX(New-Object Net.WebClient).downloadString()` and `Invoke-WebRequest`. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.(Citation: t1105_lolbas)  A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).(Citation: Google Cloud Threat Intelligence COSCMICENERGY 2023)

Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [[T1204-user_execution|T1204: User Execution]] (typically after interacting with [[T1566-phishing|T1566: Phishing]] lures).(Citation: T1105: Trellix_search-ms)

Files can also be transferred using various [[T1102-web_service|T1102: Web Service]]s as well as native or otherwise present tools on the victim system.(Citation: PTSecurity Cobalt Dec 2016) In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.(Citation: Dropbox Malware Sync)

## Workspace

- [[workspaces/attack/techniques/T1105-ingress_tool_transfer-note|Open workspace note]]

![[workspaces/attack/techniques/T1105-ingress_tool_transfer-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-07-001-suspicious_arguments|CAR-2013-07-001: Suspicious Arguments]]
- [[kb/car/analytics/CAR-2021-05-005-bitsadmin_download_file|CAR-2021-05-005: BITSAdmin Download File]]
- [[kb/car/analytics/CAR-2021-05-006-certutil_download_with_urlcache_and_split_arguments|CAR-2021-05-006: CertUtil Download With URLCache and Split Arguments]]
- [[kb/car/analytics/CAR-2021-05-007-certutil_download_with_verifyctl_and_split_arguments|CAR-2021-05-007: CertUtil Download With VerifyCtl and Split Arguments]]

### Sigma Rules

- [[kb/sigma/rules/00d49ed5_4491_4271_a8db_650a4ef6f8c1-suspicious_download_from_office_domain|Suspicious Download from Office Domain (high; windows / process_creation)]]
- [[kb/sigma/rules/0dba975d_a193_4ed1_a067_424df57570d1-uncommon_network_connection_initiated_by_certutil_exe|Uncommon Network Connection Initiated By Certutil.EXE (high; windows / network_connection)]]
- [[kb/sigma/rules/0e8cfe08_02c9_4815_a2f8_0d157b7ed33e-file_download_with_headless_browser|File Download with Headless Browser (high; windows / process_creation)]]
- [[kb/sigma/rules/13e6fe51_d478_4c7e_b0f2_6da9b400a829-suspicious_file_downloaded_from_direct_ip_via_certutil_exe|Suspicious File Downloaded From Direct IP Via Certutil.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/1cf465a1_2609_4c15_9b66_c32dbe4bfd67-legitimate_application_writing_files_in_uncommon_location|Legitimate Application Writing Files In Uncommon Location (high; windows / file_event)]]
- [[kb/sigma/rules/21dd6d38_2b18_4453_9404_a0fe4a0cc288-curl_download_and_execute_combination|Curl Download And Execute Combination (high; windows / process_creation)]]
- [[kb/sigma/rules/25eabf56_22f0_4915_a1ed_056b8dae0a68-suspicious_dropbox_api_usage|Suspicious Dropbox API Usage (high; windows / network_connection)]]
- [[kb/sigma/rules/2ddef153_167b_4e89_86b6_757a9e65dcac-file_download_via_bitsadmin_to_a_suspicious_target_folder|File Download Via Bitsadmin To A Suspicious Target Folder (high; windows / process_creation)]]
- [[kb/sigma/rules/3aff0be0_7802_4a7e_a4fa_c60c74bc5e1d-lolbas_onedrivestandaloneupdater_exe_proxy_download|Lolbas OneDriveStandaloneUpdater.exe Proxy Download (high; windows / registry_set)]]
- [[kb/sigma/rules/42a5f1e7_9603_4f6d_97ae_3f37d130d794-suspicious_file_downloaded_from_file_sharing_website_via_certutil_exe|Suspicious File Downloaded From File-Sharing Website Via Certutil.EXE (high; windows / process_creation)]]
- 20 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/0139dba1_f391_405e_a4f5_f3989f2c88ef-sftp_remote_file_copy_pull|sftp remote file copy (pull) (sh; linux, macos)]]
- [[kb/atomic/tests/0fc6e977_cb12_44f6_b263_2824ba917409-rsync_remote_file_copy_push|rsync remote file copy (push) (sh; linux, macos)]]
- [[kb/atomic/tests/1a02df58_09af_4064_a765_0babe1a0d1e2-download_a_file_with_imewdbld_exe|Download a file with IMEWDBLD.exe (powershell; windows)]]
- [[kb/atomic/tests/205e676e_0401_4bae_83a5_94b8c5daeb22-windows_push_file_using_sftp_exe|Windows push file using sftp.exe (powershell; windows)]]
- [[kb/atomic/tests/2a4b0d29_e5dd_4b66_b729_07423ba1cd9d-windows_push_file_using_scp_exe|Windows push file using scp.exe (powershell; windows)]]
- [[kb/atomic/tests/2b080b99_0deb_4d51_af0f_833d37c4ca6a-curl_download_file|Curl Download File (command_prompt; windows)]]
- [[kb/atomic/tests/2ca61766_b456_4fcf_a35a_1233685e1cad-ostap_worming_activity|OSTAP Worming Activity (command_prompt; windows)]]
- [[kb/atomic/tests/3180f7d5_52c0_4493_9ea0_e3431a84773f-rsync_remote_file_copy_pull|rsync remote file copy (pull) (sh; linux, macos)]]
- [[kb/atomic/tests/3d25f1f2_55cb_4a41_a523_d17ad4cfba19-windows_pull_file_using_sftp_exe|Windows pull file using sftp.exe (powershell; windows)]]
- [[kb/atomic/tests/3dd6a6cf_9c78_462c_bd75_e9b54fc8925b-download_a_file_with_onedrive_standalone_updater|Download a file with OneDrive Standalone Updater (powershell; windows)]]
- 29 more in the generated source index

### LOLBAS Entries

- [[kb/lolbas/entries/honorablementions-gfxdownloadwrapper_exe|GfxDownloadWrapper.exe (Download)]]
- [[kb/lolbas/entries/osbinaries-appinstaller_exe|AppInstaller.exe (Download)]]
- [[kb/lolbas/entries/osbinaries-bitsadmin_exe|Bitsadmin.exe (ADS, Download, Copy, Execute)]]
- [[kb/lolbas/entries/osbinaries-certoc_exe|CertOC.exe (Execute, Download)]]
- [[kb/lolbas/entries/osbinaries-certreq_exe|CertReq.exe (Download, Upload)]]
- [[kb/lolbas/entries/osbinaries-certutil_exe|Certutil.exe (Download, ADS, Encode, Decode)]]
- [[kb/lolbas/entries/osbinaries-cmd_exe|Cmd.exe (ADS, Download, Upload)]]
- [[kb/lolbas/entries/osbinaries-cmdl32_exe|cmdl32.exe (Download)]]
- [[kb/lolbas/entries/osbinaries-configsecuritypolicy_exe|ConfigSecurityPolicy.exe (Upload, Download)]]
- [[kb/lolbas/entries/osbinaries-desktopimgdownldr_exe|Desktopimgdownldr.exe (Download)]]
- 48 more in the generated source index

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

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[bitsadmin|BITSAdmin (S0190)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[carrotball|CARROTBALL (S0465)]]
- [[certutil|certutil (S0160)]]
- [[cmd|cmd (S0106)]]
- [[cspy_downloader|CSPY Downloader (S0527)]]
- [[donut|Donut (S0695)]]
- [[empire|Empire (S0363)]]
- [[esentutl|esentutl (S0404)]]
- [[ftp|ftp (S0095)]]
- [[koadic|Koadic (S0250)]]
- [[mcmd|MCMD (S0500)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[remcos|Remcos (S0332)]]
- [[remoteutilities|RemoteUtilities (S0592)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

