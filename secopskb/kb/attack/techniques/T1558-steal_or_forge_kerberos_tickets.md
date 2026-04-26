---
mitre_id: "T1558"
mitre_name: "Steal or Forge Kerberos Tickets"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3fc01293-ef5e-41c6-86ce-61f10706b64a"
mitre_created: "2020-02-11T19:12:46.830Z"
mitre_modified: "2025-10-24T17:48:41.885Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1558/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-ANCI"
  - "D3-APCA"
  - "D3-CCSA"
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
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RIC"
  - "D3-RTA"
  - "D3-RTSD"
  - "D3-TB"
  - "D3-TBA"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]. Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants: client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in `klist` utility can be used to list and analyze cached Kerberos tickets.(Citation: Microsoft Klist)


## Workspace

- [[workspaces/attack/techniques/T1558-steal_or_forge_kerberos_tickets-note|Open workspace note]]

![[workspaces/attack/techniques/T1558-steal_or_forge_kerberos_tickets-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/12827a56_61a4_476a_a9cb_f3068f191073-hacktool_krbrelayup_execution|HackTool - KrbRelayUp Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/12e6d621_194f_4f59_90cc_1959e21e69f7-register_new_logon_process_by_rubeus|Register new Logon Process by Rubeus (high; windows / security)]]
- [[kb/sigma/rules/3245cd30_e015_40ff_a31d_5cadd5f377ec-hacktool_rubeus_execution_scriptblock|HackTool - Rubeus Execution - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/5a44727c_3b85_4713_8c44_4401d5499629-replay_attack_detected|Replay Attack Detected (high; windows / security)]]
- [[kb/sigma/rules/6daac7fc_77d1_449a_a71a_e6b4d59a0e54-user_couldn_t_call_a_privileged_service_lsaregisterlogonprocess|User Couldn't Call a Privileged Service 'LsaRegisterLogonProcess' (high; windows / security)]]
- [[kb/sigma/rules/78cc2dd2_7d20_4d32_93ff_057084c38b93-antivirus_password_dumper_detection|Antivirus Password Dumper Detection (critical; antivirus)]]
- [[kb/sigma/rules/7ec2c172_dceb_4c10_92c9_87c1881b7e18-hacktool_rubeus_execution|HackTool - Rubeus Execution (critical; windows / process_creation)]]
- [[kb/sigma/rules/9e099d99_44c2_42b6_a6d8_54c3545cab29-hacktool_mimikatz_kirbi_file_creation|HackTool - Mimikatz Kirbi File Creation (critical; windows / file_event)]]
- [[kb/sigma/rules/a7664b14_75fb_4a50_a223_cb9bc0afbacf-hacktool_remotekrbrelay_execution|HackTool - RemoteKrbRelay Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/a861d835_af37_4930_bcd6_5b178bfb54df-suspicious_kerberos_ticket_request_via_powershell_script_scriptblock|Suspicious Kerberos Ticket Request via PowerShell Script - ScriptBlock (high; windows / ps_script)]]
- 2 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/14625569_6def_4497_99ac_8e7817105b55-rubeus_kerberoast|Rubeus kerberoast (powershell; windows)]]
- [[kb/atomic/tests/29094950_2c96_4cbd_b5e4_f7c65079678f-winpwn_powersharppack_kerberoasting_using_rubeus|WinPwn - PowerSharpPack - Kerberoasting Using Rubeus (powershell; windows)]]
- [[kb/atomic/tests/385e59aa_113e_4711_84d9_f637aef01f2c-crafting_active_directory_silver_tickets_with_mimikatz|Crafting Active Directory silver tickets with mimikatz (powershell; windows)]]
- [[kb/atomic/tests/3f987809_3681_43c8_bcd8_b3ff3a28533a-request_for_service_tickets|Request for service tickets (powershell; windows)]]
- [[kb/atomic/tests/615bd568_2859_41b5_9aed_61f6a88e48dd-rubeus_asreproast|Rubeus asreproast (powershell; windows)]]
- [[kb/atomic/tests/78d10e20_c874_45f2_a9df_6fea0120ec27-winpwn_kerberoasting|WinPwn - Kerberoasting (powershell; windows)]]
- [[kb/atomic/tests/8c385f88_4d47_4c9a_814d_93d9deec8c71-winpwn_powersharppack_kerberoasting_using_rubeus|WinPwn - PowerSharpPack - Kerberoasting Using Rubeus (powershell; windows)]]
- [[kb/atomic/tests/902f4ed2_1aba_4133_90f2_cff6d299d6da-request_all_tickets_via_powershell|Request All Tickets via PowerShell (powershell; windows)]]
- [[kb/atomic/tests/9726592a_dabc_4d4d_81cd_44070008b3af-crafting_active_directory_golden_tickets_with_mimikatz|Crafting Active Directory golden tickets with mimikatz (powershell; windows)]]
- [[kb/atomic/tests/988539bc_2ed7_4e62_aec6_7c5cf6680863-request_a_single_ticket_via_powershell|Request A Single Ticket via PowerShell (powershell; windows)]]
- 3 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
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
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-RTA-rpc_traffic_analysis|D3-RTA: RPC Traffic Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-TB-token_binding|D3-TB: Token Binding]]
- [[D3-TBA-token-based_authentication|D3-TBA: Token-based Authentication]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1558.001: Golden Ticket

^t1558001-golden-ticket

Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also known as a golden ticket.(Citation: AdSecurity Kerberos GT Aug 2015) Golden tickets enable adversaries to generate authentication material for any account in Active Directory.(Citation: CERT-EU Golden Ticket Protection) 

Using a golden ticket, adversaries are then able to request ticket granting service (TGS) tickets, which enable access to specific resources. Golden tickets require adversaries to interact with the Key Distribution Center (KDC) in order to obtain TGS.(Citation: ADSecurity Detecting Forged Tickets)

The KDC service runs all on domain controllers that are part of an Active Directory domain. KRBTGT is the Kerberos Key Distribution Center (KDC) service account and is responsible for encrypting and signing all Kerberos tickets.(Citation: ADSecurity Kerberos and KRBTGT) The KRBTGT password hash may be obtained using [[T1003-os_credential_dumping|T1003: OS Credential Dumping]] and privileged access to a domain controller.

### T1558.002: Silver Ticket

^t1558002-silver-ticket

Adversaries who have the password hash of a target service account (e.g. SharePoint, MSSQL) may forge Kerberos ticket granting service (TGS) tickets, also known as silver tickets. Kerberos TGS tickets are also known as service tickets.(Citation: ADSecurity Silver Tickets)

Silver tickets are more limited in scope in than golden tickets in that they only enable adversaries to access a particular resource (e.g. MSSQL) and the system that hosts the resource; however, unlike golden tickets, adversaries with the ability to forge silver tickets are able to create TGS tickets without interacting with the Key Distribution Center (KDC), potentially making detection more difficult.(Citation: ADSecurity Detecting Forged Tickets)

Password hashes for target services may be obtained using [[T1003-os_credential_dumping|T1003: OS Credential Dumping]] or [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]].

### T1558.003: Kerberoasting

^t1558003-kerberoasting

Adversaries may abuse a valid Kerberos ticket-granting ticket (TGT) or sniff network traffic to obtain a ticket-granting service (TGS) ticket that may be vulnerable to [[T1110-brute_force|T1110: Brute Force]].(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) 

Service principal names (SPNs) are used to uniquely identify each instance of a Windows service. To enable authentication, Kerberos requires that SPNs be associated with at least one service logon account (an account specifically tasked with running a service(Citation: Microsoft Detecting Kerberoasting Feb 2018)).(Citation: Microsoft SPN)(Citation: Microsoft SetSPN)(Citation: SANS Attacking Kerberos Nov 2014)(Citation: Harmj0y Kerberoast Nov 2016)

Adversaries possessing a valid Kerberos ticket-granting ticket (TGT) may request one or more Kerberos ticket-granting service (TGS) service tickets for any SPN from a domain controller (DC).(Citation: Empire InvokeKerberoast Oct 2016)(Citation: AdSecurity Cracking Kerberos Dec 2015) Portions of these tickets may be encrypted with the RC4 algorithm, meaning the Kerberos 5 TGS-REP etype 23 hash of the service account associated with the SPN is used as the private key and is thus vulnerable to offline [[T1110-brute_force|T1110: Brute Force]] attacks that may expose plaintext credentials.(Citation: AdSecurity Cracking Kerberos Dec 2015)(Citation: Empire InvokeKerberoast Oct 2016) (Citation: Harmj0y Kerberoast Nov 2016)

This same behavior could be executed using service tickets captured from network traffic.(Citation: AdSecurity Cracking Kerberos Dec 2015)

Cracked hashes may enable [[TA0003-persistence|TA0003: Persistence]], [[TA0004-privilege_escalation|TA0004: Privilege Escalation]], and [[TA0008-lateral_movement|TA0008: Lateral Movement]] via access to [[T1078-valid_accounts|T1078: Valid Accounts]].(Citation: SANS Attacking Kerberos Nov 2014)

### T1558.004: AS-REP Roasting

^t1558004-as-rep-roasting

Adversaries may reveal credentials of accounts that have disabled Kerberos preauthentication by [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]] Kerberos messages.(Citation: Harmj0y Roasting AS-REPs Jan 2017) 

Preauthentication offers protection against offline [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]. When enabled, a user requesting access to a resource initiates communication with the Domain Controller (DC) by sending an Authentication Server Request (AS-REQ) message with a timestamp that is encrypted with the hash of their password. If and only if the DC is able to successfully decrypt the timestamp with the hash of the user’s password, it will then send an Authentication Server Response (AS-REP) message that contains the Ticket Granting Ticket (TGT) to the user. Part of the AS-REP message is signed with the user’s password.(Citation: Microsoft Kerberos Preauth 2014)

For each account found without preauthentication, an adversary may send an AS-REQ message without the encrypted timestamp and receive an AS-REP message with TGT data which may be encrypted with an insecure algorithm such as RC4. The recovered encrypted data may be vulnerable to offline [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]] attacks similarly to [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]] and expose plaintext credentials. (Citation: Harmj0y Roasting AS-REPs Jan 2017)(Citation: Stealthbits Cracking AS-REP Roasting Jun 2019) 

An account registered to a domain, with or without special privileges, can be abused to list all domain accounts that have preauthentication disabled by utilizing Windows tools like [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] with an LDAP filter. Alternatively, the adversary may send an AS-REQ message for each user. If the DC responds without errors, the account does not require preauthentication and the AS-REP message will already contain the encrypted data. (Citation: Harmj0y Roasting AS-REPs Jan 2017)(Citation: Stealthbits Cracking AS-REP Roasting Jun 2019)

Cracked hashes may enable [[TA0003-persistence|TA0003: Persistence]], [[TA0004-privilege_escalation|TA0004: Privilege Escalation]], and [[TA0008-lateral_movement|TA0008: Lateral Movement]] via access to [[T1078-valid_accounts|T1078: Valid Accounts]].(Citation: SANS Attacking Kerberos Nov 2014)

### T1558.005: Ccache Files

^t1558005-ccache-files


Adversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication and allows for access to multiple services without the user having to re-enter credentials. 

The `/etc/krb5.conf` configuration file and the `KRB5CCNAME` environment variable are used to set the storage location for ccache entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically, users interact with ticket storage using `kinit`, which obtains a Ticket-Granting-Ticket (TGT) for the principal; `klist`, which lists obtained tickets currently held in the credentials cache; and other built-in binaries.(Citation: Kerberos GNU/Linux)(Citation: Binary Defense Kerberos Linux)

Adversaries can collect tickets from ccache files stored on disk and authenticate as the current user without their password to perform [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]] attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]. Tools like Kekeo can also be used by adversaries to convert ccache files to Windows format for further [[TA0008-lateral_movement|TA0008: Lateral Movement]]. On macOS, adversaries may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets via lower-level APIs.(Citation: SpectorOps Bifrost Kerberos macOS 2019)(Citation: Linux Kerberos Tickets)(Citation: Brining MimiKatz to Unix)(Citation: Kekeo) 

## Mitigations

- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1043-credential_access_protection|M1043: Credential Access Protection]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Windows
- Linux
- macOS

