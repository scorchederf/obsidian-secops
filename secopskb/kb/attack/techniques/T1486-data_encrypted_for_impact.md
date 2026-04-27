---
mitre_id: "T1486"
mitre_name: "Data Encrypted for Impact"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b80d107d-fa0d-4b60-9684-b0433e8bdba0"
mitre_created: "2019-03-15T13:59:30.390Z"
mitre_modified: "2025-10-24T17:49:16.589Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1486/"
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
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
d3fend_ids:
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
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.(Citation: US-CERT Ransomware 2016)(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017)(Citation: US-CERT SamSam 2018)

In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as [[T1222-file_and_directory_permissions_modification|T1222: File and Directory Permissions Modification]] or [[T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]], in order to unlock and/or gain access to manipulate these files.(Citation: CarbonBlack Conti July 2020) In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR.(Citation: US-CERT NotPetya 2017) Adversaries may also encrypt virtual machines hosted on ESXi or other hypervisors.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021) 

To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like [[T1078-valid_accounts|T1078: Valid Accounts]], [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], and [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]].(Citation: FireEye WannaCry 2017)(Citation: US-CERT NotPetya 2017) Encryption malware may also leverage [[T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]], such as changing victim wallpapers or ESXi server login messages, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing").(Citation: NHS Digital Egregor Nov 2020)(Citation: Varonis)

In cloud environments, storage objects within compromised accounts may also be encrypted.(Citation: Rhino S3 Ransomware Part 1) For example, in AWS environments, adversaries may leverage services such as AWS’s Server-Side Encryption with Customer Provided Keys (SSE-C) to encrypt data.(Citation: Halcyon AWS Ransomware 2025)

## Workspace

- [[workspaces/attack/techniques/T1486-data_encrypted_for_impact-note|Open workspace note]]

![[workspaces/attack/techniques/T1486-data_encrypted_for_impact-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/0e0255bf_2548_47b8_9582_c0955c9283f5-suspicious_reg_add_bitlocker|Suspicious Reg Add BitLocker (high; windows / process_creation)]]
- [[kb/sigma/rules/1279262f_1464_422f_ac0d_5b545320c526-aws_kms_imported_key_material_usage|AWS KMS Imported Key Material Usage (high; aws / cloudtrail)]]
- [[kb/sigma/rules/4c6ca276_d4d0_4a8c_9e4c_d69832f8671f-antivirus_ransomware_detection|Antivirus Ransomware Detection (critical; antivirus)]]
- [[kb/sigma/rules/b48492dc_c5ef_4572_8dff_32bc241c15c8-load_of_rstrtmgr_dll_by_a_suspicious_process|Load Of RstrtMgr.DLL By A Suspicious Process (high; windows / image_load)]]
- [[kb/sigma/rules/caf02a0a_1e1c_4552_9b48_5e070bd88d11-suspicious_creation_txt_file_in_user_desktop|Suspicious Creation TXT File in User Desktop (high; windows / file_event)]]
- [[kb/sigma/rules/ec0722a3_eb5c_4a56_8ab2_bf6f20708592-renamed_gpg_exe_execution|Renamed Gpg.EXE Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/08cbf59f_85da_4369_a5f4_049cffd7709f-encrypt_files_using_ccrypt_freebsd_linux|Encrypt files using ccrypt (FreeBSD/Linux) (sh; linux)]]
- [[kb/atomic/tests/142752dc_ca71_443b_9359_cf6f497315f1-encrypt_files_using_openssl_freebsd_linux|Encrypt files using openssl (FreeBSD/Linux) (sh; linux)]]
- [[kb/atomic/tests/1a01f6b8_b1e8_418e_bbe3_78a6f822759e-encrypt_files_using_openssl_utility_macos|Encrypt files using openssl utility - macOS (sh; macos)]]
- [[kb/atomic/tests/44b68e11_9da2_4d45_a0d9_893dabd60f30-data_encrypt_using_diskcryptor|Data Encrypt Using DiskCryptor (command_prompt; windows)]]
- [[kb/atomic/tests/4541e2c2_33c8_44b1_be79_9161440f1718-data_encrypted_with_gpg4win|Data Encrypted with GPG4Win (powershell; windows)]]
- [[kb/atomic/tests/53e6735a_4727_44cc_b35b_237682a151ad-encrypt_files_using_7z_freebsd_linux|Encrypt files using 7z (FreeBSD/Linux) (sh; linux)]]
- [[kb/atomic/tests/645f0f5a_ef09_48d8_b9bc_f0e24c642d72-encrypt_files_using_7z_utility_macos|Encrypt files using 7z utility - macOS (sh; macos)]]
- [[kb/atomic/tests/649349c7_9abf_493b_a7a2_b1aa4d141528-purelocker_ransom_note|PureLocker Ransom Note (command_prompt; windows)]]
- [[kb/atomic/tests/7b8ce084_3922_4618_8d22_95f996173765-encrypt_files_using_gpg_freebsd_linux|Encrypt files using gpg (FreeBSD/Linux) (sh; linux)]]
- [[kb/atomic/tests/ab3f793f_2dcc_4da5_9c71_34988307263f-akira_ransomware_drop_files_with_akira_extension_and_ransomnote|Akira Ransomware drop Files with .akira Extension and Ransomnote (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## D3FEND

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

## Mitigations

- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1053-data_backup|M1053: Data Backup]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Windows

