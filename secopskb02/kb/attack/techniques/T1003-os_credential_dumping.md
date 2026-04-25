---
mitre_id: "T1003"
mitre_name: "OS Credential Dumping"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0a3ead4e-6d47-4ccb-854c-a6a4f9d96b22"
mitre_created: "2017-05-31T21:30:19.735Z"
mitre_modified: "2025-10-24T17:48:22.201Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1003/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-ABPI"
  - "D3-AEM"
  - "D3-ANAA"
  - "D3-ANCI"
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CCSA"
  - "D3-CF"
  - "D3-CH"
  - "D3-CM"
  - "D3-CQ"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CSPP"
  - "D3-CTS"
  - "D3-DF"
  - "D3-DI"
  - "D3-DUC"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-HR"
  - "D3-HS"
  - "D3-KBPI"
  - "D3-LFP"
  - "D3-MFA"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OPM"
  - "D3-PHDURA"
  - "D3-PLA"
  - "D3-PMAD"
  - "D3-PS"
  - "D3-PSA"
  - "D3-PSMD"
  - "D3-PT"
  - "D3-RD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RIC"
  - "D3-RTSD"
  - "D3-SCF"
  - "D3-SFA"
  - "D3-UGLPA"
  - "D3-WSAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password. Credentials can be obtained from OS caches, memory, or structures.(Citation: Brining MimiKatz to Unix) Credentials can then be used to perform [[TA0008-lateral_movement|TA0008: Lateral Movement]] and access restricted information.

Several of the tools mentioned in associated sub-techniques may be used by both adversaries and professional security testers. Additional custom tools likely exist as well.


## Workspace

- [[workspaces/attack/techniques/T1003-os_credential_dumping-note|Open workspace note]]

![[workspaces/attack/techniques/T1003-os_credential_dumping-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-ABPI-application-based_process_isolation|D3-ABPI: Application-based Process Isolation]]
- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]
- [[D3-ANAA-administrative_network_activity_analysis|D3-ANAA: Administrative Network Activity Analysis]]
- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-HR-host_reboot|D3-HR: Host Reboot]]
- [[D3-HS-host_shutdown|D3-HS: Host Shutdown]]
- [[D3-KBPI-kernel-based_process_isolation|D3-KBPI: Kernel-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OPM-operational_process_monitoring|D3-OPM: Operational Process Monitoring]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-PS-process_suspension|D3-PS: Process Suspension]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-PT-process_termination|D3-PT: Process Termination]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-WSAM-web_session_access_mediation|D3-WSAM: Web Session Access Mediation]]

## Subtechniques

### T1003.001: LSASS Memory

^t1003001-lsass-memory

Adversaries may attempt to access credential material stored in the process memory of the Local Security Authority Subsystem Service (LSASS). After a user logs on, the system generates and stores a variety of credential materials in LSASS process memory. These credential materials can be harvested by an administrative user or SYSTEM and used to conduct [[TA0008-lateral_movement|TA0008: Lateral Movement]] using [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]].

As well as in-memory techniques, the LSASS process memory can be dumped from the target host and analyzed on a local system.

For example, on the target host use procdump:

* `procdump -ma lsass.exe lsass_dump`

Locally, mimikatz can be run using:

* `sekurlsa::Minidump lsassdump.dmp`
* `sekurlsa::logonPasswords`

Built-in Windows tools such as `comsvcs.dll` can also be used:

* `rundll32.exe C:\Windows\System32\comsvcs.dll MiniDump PID  lsass.dmp full`(Citation: Volexity Exchange Marauder March 2021)(Citation: Symantec Attacks Against Government Sector)

Similar to [[T1546-event_triggered_execution#^t1546012-image-file-execution-options-injection|T1546.012: Image File Execution Options Injection]], the silent process exit mechanism can be abused to create a memory dump of `lsass.exe` through Windows Error Reporting (`WerFault.exe`).(Citation: Deep Instinct LSASS)

Windows Security Support Provider (SSP) DLLs are loaded into LSASS process at system start. Once loaded into the LSA, SSP DLLs have access to encrypted and plaintext passwords that are stored in Windows, such as any logged-on user's Domain password or smart card PINs. The SSP configuration is stored in two Registry keys: `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` and `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages`. An adversary may modify these Registry keys to add new SSPs, which will be loaded the next time the system boots, or when the AddSecurityPackage Windows API function is called.(Citation: Graeber 2014)

The following SSPs can be used to access credentials:

* Msv: Interactive logons, batch logons, and service logons are done through the MSV authentication package.
* Wdigest: The Digest Authentication protocol is designed for use with Hypertext Transfer Protocol (HTTP) and Simple Authentication Security Layer (SASL) exchanges.(Citation: TechNet Blogs Credential Protection)
* Kerberos: Preferred for mutual client-server domain authentication in Windows 2000 and later.
* CredSSP:  Provides SSO and Network Level Authentication for Remote Desktop Services.(Citation: TechNet Blogs Credential Protection)


### T1003.002: Security Account Manager

^t1003002-security-account-manager

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the `net user` command. Enumerating the SAM database requires SYSTEM level access.

A number of tools can be used to retrieve the SAM file through in-memory techniques:

* pwdumpx.exe
* [[gsecdump|gsecdump (S0008)]]
* [[mimikatz|Mimikatz (S0002)]]
* secretsdump.py

Alternatively, the SAM can be extracted from the Registry with Reg:

* `reg save HKLM\sam sam`
* `reg save HKLM\system system`

Creddump7 can then be used to process the SAM database locally to retrieve hashes.(Citation: GitHub Creddump7)

Notes: 

* RID 500 account is the local, built-in administrator.
* RID 501 is the guest account.
* User accounts start with a RID of 1,000+.


### T1003.003: NTDS

^t1003003-ntds

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in `%SystemRoot%\NTDS\Ntds.dit` of a domain controller.(Citation: Wikipedia Active Directory)

In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information.(Citation: Metcalf 2015)

The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes.

* Volume Shadow Copy
* secretsdump.py
* Using the in-built Windows tool, ntdsutil.exe
* Invoke-NinjaCopy


### T1003.004: LSA Secrets

^t1003004-lsa-secrets

Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury Windows Credentials) LSA secrets are stored in the registry at `HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets`. LSA secrets can also be dumped from memory.(Citation: ired Dumping LSA Secrets)

[[reg|Reg (S0075)]] can be used to extract from the Registry. [[mimikatz|Mimikatz (S0002)]] can be used to extract secrets from memory.(Citation: ired Dumping LSA Secrets)

### T1003.005: Cached Domain Credentials

^t1003005-cached-domain-credentials

Adversaries may attempt to access cached domain credentials used to allow authentication to occur in the event a domain controller is unavailable.(Citation: Microsoft - Cached Creds)

On Windows Vista and newer, the hash format is DCC2 (Domain Cached Credentials version 2) hash, also known as MS-Cache v2 hash.(Citation: PassLib mscache) The number of default cached credentials varies and can be altered per system. This hash does not allow pass-the-hash style attacks, and instead requires [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]] to recover the plaintext password.(Citation: ired mscache)

On Linux systems, Active Directory credentials can be accessed through caches maintained by software like System Security Services Daemon (SSSD) or Quest Authentication Services (formerly VAS). Cached credential hashes are typically located at `/var/lib/sss/db/cache.[domain].ldb` for SSSD or `/var/opt/quest/vas/authcache/vas_auth.vdb` for Quest. Adversaries can use utilities, such as `tdbdump`, on these database files to dump the cached hashes and use [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]] to obtain the plaintext password.(Citation: Brining MimiKatz to Unix) 

With SYSTEM or sudo access, the tools/utilities such as [[mimikatz|Mimikatz (S0002)]], [[reg|Reg (S0075)]], and secretsdump.py for Windows or Linikatz for Linux can be used to extract the cached credentials.(Citation: Brining MimiKatz to Unix)

Note: Cached credentials for Windows Vista are derived using PBKDF2.(Citation: PassLib mscache)

### T1003.006: DCSync

^t1003006-dcsync

Adversaries may attempt to access credentials and other sensitive information by abusing a Windows Domain Controller's application programming interface (API)(Citation: Microsoft DRSR Dec 2017) (Citation: Microsoft GetNCCChanges) (Citation: Samba DRSUAPI) (Citation: Wine API samlib.dll) to simulate the replication process from a remote domain controller using a technique called DCSync.

Members of the Administrators, Domain Admins, and Enterprise Admin groups or computer accounts on the domain controller are able to run DCSync to pull password data(Citation: ADSecurity Mimikatz DCSync) from Active Directory, which may include current and historical hashes of potentially useful accounts such as KRBTGT and Administrators. The hashes can then in turn be used to create a [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]] for use in [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]](Citation: Harmj0y Mimikatz and DCSync) or change an account's password as noted in [[T1098-account_manipulation|T1098: Account Manipulation]].(Citation: InsiderThreat ChangeNTLM July 2017)

DCSync functionality has been included in the "lsadump" module in [[mimikatz|Mimikatz (S0002)]].(Citation: GitHub Mimikatz lsadump Module) Lsadump also includes NetSync, which performs DCSync over a legacy replication protocol.(Citation: Microsoft NRPC Dec 2017)

### T1003.007: Proc Filesystem

^t1003007-proc-filesystem

Adversaries may gather credentials from the proc filesystem or `/proc`. The proc filesystem is a pseudo-filesystem used as an interface to kernel data structures for Linux based systems managing virtual memory. For each process, the `/proc/<PID>/maps` file shows how memory is mapped within the process’s virtual address space. And `/proc/<PID>/mem`, exposed for debugging purposes, provides access to the process’s virtual address space.(Citation: Picus Labs Proc cump 2022)(Citation: baeldung Linux proc map 2022)

When executing with root privileges, adversaries can search these memory locations for all processes on a system that contain patterns indicative of credentials. Adversaries may use regex patterns, such as `grep -E "^[0-9a-f-]* r" /proc/"$pid"/maps | cut -d' ' -f 1`, to look for fixed strings in memory structures or cached hashes.(Citation: atomic-red proc file system) When running without privileged access, processes can still view their own virtual memory locations. Some services or programs may save credentials in clear text inside the process’s memory.(Citation: MimiPenguin GitHub May 2017)(Citation: Polop Linux PrivEsc Gitbook)

If running as or with the permissions of a web browser, a process can search the `/maps` & `/mem` locations for common website credential patterns (that can also be used to find adjacent memory within the same structure) in which hashes or cleartext credentials may be located.

### T1003.008: /etc/passwd and /etc/shadow

^t1003008--etc-passwd-and--etc-shadow

Adversaries may attempt to dump the contents of `/etc/passwd` and `/etc/shadow` to enable offline password cracking. Most modern Linux operating systems use a combination of `/etc/passwd` and `/etc/shadow` to store user account information, including password hashes in `/etc/shadow`. By default, `/etc/shadow` is only readable by the root user.(Citation: Linux Password and Shadow File Formats)

Linux stores user information such as user ID, group ID, home directory path, and login shell in `/etc/passwd`. A "user" on the system may belong to a person or a service. All password hashes are stored in `/etc/shadow` - including entries for users with no passwords and users with locked or disabled accounts.(Citation: Linux Password and Shadow File Formats)

Adversaries may attempt to read or dump the `/etc/passwd` and `/etc/shadow` files on Linux systems via command line utilities such as the `cat` command.(Citation: Arctic Wolf) Additionally, the Linux utility `unshadow` can be used to combine the two files in a format suited for password cracking utilities such as John the Ripper - for example, via the command `/usr/bin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db`(Citation: nixCraft - John the Ripper). Since the user information stored in `/etc/passwd` are linked to the password hashes in `/etc/shadow`, an adversary would need to have access to both.

## Mitigations

- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1017-user_training|M1017: User Training]]
- [[M1025-privileged_process_integrity|M1025: Privileged Process Integrity]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1043-credential_access_protection|M1043: Credential Access Protection]]

## Platforms

- Linux
- macOS
- Windows

