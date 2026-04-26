---
mitre_id: "T1110"
mitre_name: "Brute Force"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a93494bb-4b80-4ea1-8695-3236a49916fd"
mitre_created: "2017-05-31T21:31:22.767Z"
mitre_modified: "2025-10-24T17:49:12.218Z"
mitre_version: "2.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1110/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "ESXi"
  - "IaaS"
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-AEM"
  - "D3-ANAA"
  - "D3-ANCI"
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CCSA"
  - "D3-CDP"
  - "D3-CH"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CSPP"
  - "D3-CTS"
  - "D3-DUC"
  - "D3-MFA"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OPM"
  - "D3-OTP"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-PR"
  - "D3-PWA"
  - "D3-RIC"
  - "D3-RTSD"
  - "D3-SPP"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained.(Citation: TrendMicro Pawn Storm Dec 2020) Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism.(Citation: Dragos Crashoverride 2018) Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.

Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to [[T1078-valid_accounts|T1078: Valid Accounts]] within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as [[T1003-os_credential_dumping|T1003: OS Credential Dumping]], [[T1087-account_discovery|T1087: Account Discovery]], or [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]. Adversaries may also combine brute forcing activity with behaviors such as [[T1133-external_remote_services|T1133: External Remote Services]] as part of Initial Access. 

If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies.(Citation: ReliaQuest Health Care Social Engineering Campaign 2024)

## Workspace

- [[workspaces/attack/techniques/T1110-brute_force-note|Open workspace note]]

![[workspaces/attack/techniques/T1110-brute_force-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/28ecba0a_c743_4690_ad29_9a8f6f25a6f9-password_spray_activity|Password Spray Activity (high; azure / riskdetection)]]
- [[kb/sigma/rules/39b31e81_5f5f_4898_9c0e_2160cfc0f9bf-hacktool_hashcat_password_cracker_execution|HackTool - Hashcat Password Cracker Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/42a993dd_bb3e_48c8_b372_4d6684c4106c-hacktool_crackmapexec_execution|HackTool - CrackMapExec Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/53bb4f7f_48a8_4475_ac30_5a82ddfdf6fc-potential_mfa_bypass_using_legacy_client_authentication|Potential MFA Bypass Using Legacy Client Authentication (high; azure / signinlogs)]]
- [[kb/sigma/rules/60f6535a_760f_42a9_be3f_c9a0a025906e-use_of_legacy_authentication_protocols|Use of Legacy Authentication Protocols (high; azure / signinlogs)]]
- [[kb/sigma/rules/78d5cab4_557e_454f_9fb9_a222bd0d5edc-external_remote_smb_logon_from_public_ip|External Remote SMB Logon from Public IP (high; windows / security)]]
- [[kb/sigma/rules/aaafa146_074c_11eb_adc1_0242ac120002-hacktool_hydra_password_bruteforce_execution|HackTool - Hydra Password Bruteforce Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/b4a6d707_9430_4f5f_af68_0337f52d5c42-sign_in_failure_due_to_conditional_access_requirements_not_met|Sign-in Failure Due to Conditional Access Requirements Not Met (high; azure / signinlogs)]]
- [[kb/sigma/rules/c42a3073_30fb_48ae_8c99_c23ada84b103-hack_tool_user_agent|Hack Tool User Agent (high; proxy)]]

### Atomic Tests

- [[kb/atomic/tests/09480053_2f98_4854_be6e_71ae5f672224-brute_force_credentials_of_single_active_directory_domain_users_via_smb|Brute Force Credentials of single Active Directory domain users via SMB (command_prompt; windows)]]
- [[kb/atomic/tests/263ae743_515f_4786_ac7d_41ef3a0d4b2b-password_spray_domainpasswordspray|Password Spray (DomainPasswordSpray) (powershell; windows)]]
- [[kb/atomic/tests/4097bc00_5eeb_4d56_aaf9_287d60351d95-sudo_brute_force_redhat|SUDO Brute Force - Redhat (bash; linux)]]
- [[kb/atomic/tests/4852c630_87a9_409b_bb5e_5dc12c9ebcde-brute_force_credential_stuffing_using_kerbrute_tool|Brute Force:Credential Stuffing using Kerbrute Tool (powershell; windows)]]
- [[kb/atomic/tests/4f08197a_2a8a_472d_9589_cd2895ef22ad-ssh_credential_stuffing_from_linux|SSH Credential Stuffing From Linux (bash; linux)]]
- [[kb/atomic/tests/59dbeb1a_79a7_4c2a_baf4_46d0f4c761c4-password_brute_user_using_kerbrute_tool|Password Brute User using Kerbrute Tool (powershell; windows)]]
- [[kb/atomic/tests/5a51ef57_299e_4d62_8e11_2d440df55e69-brute_force_credentials_of_single_azure_ad_user|Brute Force Credentials of single Azure AD user (powershell; azure-ad)]]
- [[kb/atomic/tests/5ccf4bbd_7bf6_43fc_83ac_d9e38aff1d82-winpwn_domainpasswordspray_attacks|WinPwn - DomainPasswordSpray Attacks (powershell; windows)]]
- [[kb/atomic/tests/6d27df5d_69d4_4c91_bc33_5983ffe91692-password_cracking_with_hashcat|Password Cracking with Hashcat (command_prompt; windows)]]
- [[kb/atomic/tests/90bc2e54_6c84_47a5_9439_0a2a92b4b175-password_spray_all_domain_users|Password Spray all Domain Users (command_prompt; windows)]]
- 12 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-ANAA-administrative_network_activity_analysis|D3-ANAA: Administrative Network Activity Analysis]]
- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CDP-change_default_password|D3-CDP: Change Default Password]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-OTP-one-time_password|D3-OTP: One-time Password]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-PR-password_rotation|D3-PR: Password Rotation]]
- [[D3-PWA-password_authentication|D3-PWA: Password Authentication]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SPP-strong_password_policy|D3-SPP: Strong Password Policy]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1110.001: Password Guessing

^t1110001-password-guessing

Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords to attempt access to accounts. Without knowledge of the password for an account, an adversary may opt to systematically guess the password using a repetitive or iterative mechanism. An adversary may guess login credentials without prior knowledge of system or environment passwords during an operation by using a list of common passwords. Password guessing may or may not take into account the target's policies on password complexity or use policies that may lock accounts out after a number of failed attempts.

Guessing passwords can be a risky option because it could cause numerous authentication failures and account lockouts, depending on the organization's login failure policies. (Citation: Cylance Cleaver)

Typically, management services over commonly used ports are used when guessing passwords. Commonly targeted services include the following:

* SSH (22/TCP)
* Telnet (23/TCP)
* FTP (21/TCP)
* NetBIOS / SMB / Samba (139/TCP & 445/TCP)
* LDAP (389/TCP)
* Kerberos (88/TCP)
* RDP / Terminal Services (3389/TCP)
* HTTP/HTTP Management Services (80/TCP & 443/TCP)
* MSSQL (1433/TCP)
* Oracle (1521/TCP)
* MySQL (3306/TCP)
* VNC (5900/TCP)
* SNMP (161/UDP and 162/TCP/UDP)

In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT TA18-068A 2018). Further, adversaries may abuse network device interfaces (such as `wlanAPI`) to brute force accessible wifi-router(s) via wireless authentication protocols.(Citation: Trend Micro Emotet 2020)

In default environments, LDAP and Kerberos connection attempts are less likely to trigger events over SMB, which creates Windows "logon failure" event ID 4625.

### T1110.002: Password Cracking

^t1110002-password-cracking

Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, when credential material such as password hashes are obtained. [[T1003-os_credential_dumping|T1003: OS Credential Dumping]] can be used to obtain password hashes, this may only get an adversary so far when [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]] is not an option. Further,  adversaries may leverage [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]] in order to obtain hashed credentials for network devices.(Citation: US-CERT-TA18-106A) 

Techniques to systematically guess the passwords used to compute hashes are available, or the adversary may use a pre-computed rainbow table to crack hashes. Cracking hashes is usually done on adversary-controlled systems outside of the target network.(Citation: Wikipedia Password cracking) The resulting plaintext password resulting from a successfully cracked hash may be used to log into systems, resources, and services in which the account has access.

### T1110.003: Password Spraying

^t1110003-password-spraying

Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the domain. Logins are attempted with that password against many different accounts on a network to avoid account lockouts that would normally occur when brute forcing a single account with many passwords. (Citation: BlackHillsInfosec Password Spraying)

Typically, management services over commonly used ports are used when password spraying. Commonly targeted services include the following:

* SSH (22/TCP)
* Telnet (23/TCP)
* FTP (21/TCP)
* NetBIOS / SMB / Samba (139/TCP & 445/TCP)
* LDAP (389/TCP)
* Kerberos (88/TCP)
* RDP / Terminal Services (3389/TCP)
* HTTP/HTTP Management Services (80/TCP & 443/TCP)
* MSSQL (1433/TCP)
* Oracle (1521/TCP)
* MySQL (3306/TCP)
* VNC (5900/TCP)

In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT TA18-068A 2018)

In order to avoid detection thresholds, adversaries may deliberately throttle password spraying attempts to avoid triggering security alerting. Additionally, adversaries may leverage LDAP and Kerberos authentication attempts, which are less likely to trigger high-visibility events such as Windows "logon failure" event ID 4625 that is commonly triggered by failed SMB connection attempts.(Citation: Microsoft Storm-0940)  

### T1110.004: Credential Stuffing

^t1110004-credential-stuffing

Adversaries may use credentials obtained from breach dumps of unrelated accounts to gain access to target accounts through credential overlap. Occasionally, large numbers of username and password pairs are dumped online when a website or service is compromised and the user account credentials accessed. The information may be useful to an adversary attempting to compromise accounts by taking advantage of the tendency for users to use the same passwords across personal and business accounts.

Credential stuffing is a risky option because it could cause numerous authentication failures and account lockouts, depending on the organization's login failure policies.

Typically, management services over commonly used ports are used when stuffing credentials. Commonly targeted services include the following:

* SSH (22/TCP)
* Telnet (23/TCP)
* FTP (21/TCP)
* NetBIOS / SMB / Samba (139/TCP & 445/TCP)
* LDAP (389/TCP)
* Kerberos (88/TCP)
* RDP / Terminal Services (3389/TCP)
* HTTP/HTTP Management Services (80/TCP & 443/TCP)
* MSSQL (1433/TCP)
* Oracle (1521/TCP)
* MySQL (3306/TCP)
* VNC (5900/TCP)

In addition to management services, adversaries may "target single sign-on (SSO) and cloud-based applications utilizing federated authentication protocols," as well as externally facing email applications, such as Office 365.(Citation: US-CERT TA18-068A 2018)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1036-account_use_policies|M1036: Account Use Policies]]

## Tools
- [[crackmapexec|CrackMapExec (S0488)]]
- [[poshc2|PoshC2 (S0378)]]


## Platforms

- Containers
- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- SaaS
- Windows

