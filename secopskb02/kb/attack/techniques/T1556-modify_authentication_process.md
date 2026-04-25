---
mitre_id: "T1556"
mitre_name: "Modify Authentication Process"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f4c1826f-a322-41cd-9557-562100848c84"
mitre_created: "2020-02-11T19:01:56.887Z"
mitre_modified: "2025-10-24T17:49:36.944Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1556/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "IaaS"
  - "SaaS"
  - "Office Suite"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
  - "TA0005"
  - "TA0003"
d3fend_ids:
  - "D3-ABPI"
  - "D3-AM"
  - "D3-CF"
  - "D3-CI"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-HR"
  - "D3-HS"
  - "D3-KBPI"
  - "D3-LFP"
  - "D3-NTPM"
  - "D3-PLA"
  - "D3-PS"
  - "D3-PSA"
  - "D3-PSMD"
  - "D3-PT"
  - "D3-RC"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCF"
  - "D3-SFA"
  - "D3-WSAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may modify authentication mechanisms and processes to access user credentials or enable otherwise unwarranted access to accounts. The authentication process is handled by mechanisms, such as the Local Security Authentication Server (LSASS) process and the Security Accounts Manager (SAM) on Windows, pluggable authentication modules (PAM) on Unix-based systems, and authorization plugins on MacOS systems, responsible for gathering, storing, and validating credentials. By modifying an authentication process, an adversary may be able to authenticate to a service or system without using [[T1078-valid_accounts|T1078: Valid Accounts]].

Adversaries may maliciously modify a part of this process to either reveal credentials or bypass authentication mechanisms. Compromised credentials or access may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop.

## Workspace

- [[workspaces/attack/techniques/T1556-modify_authentication_process-note|Open workspace note]]

![[workspaces/attack/techniques/T1556-modify_authentication_process-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]
- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-ABPI-application-based_process_isolation|D3-ABPI: Application-based Process Isolation]]
- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-HR-host_reboot|D3-HR: Host Reboot]]
- [[D3-HS-host_shutdown|D3-HS: Host Shutdown]]
- [[D3-KBPI-kernel-based_process_isolation|D3-KBPI: Kernel-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-NTPM-network_traffic_policy_mapping|D3-NTPM: Network Traffic Policy Mapping]]
- [[D3-PLA-process_lineage_analysis|D3-PLA: Process Lineage Analysis]]
- [[D3-PS-process_suspension|D3-PS: Process Suspension]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-PSMD-process_self-modification_detection|D3-PSMD: Process Self-Modification Detection]]
- [[D3-PT-process_termination|D3-PT: Process Termination]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-WSAM-web_session_access_mediation|D3-WSAM: Web Session Access Mediation]]

## Subtechniques

### T1556.001: Domain Controller Authentication

^t1556001-domain-controller-authentication

Adversaries may patch the authentication process on a domain controller to bypass the typical authentication mechanisms and enable access to accounts. 

Malware may be used to inject false credentials into the authentication process on a domain controller with the intent of creating a backdoor used to access any user’s account and/or credentials (ex: [Skeleton Key](https://attack.mitre.org/software/S0007)). Skeleton key works through a patch on an enterprise domain controller authentication process (LSASS) with credentials that adversaries may use to bypass the standard authentication system. Once patched, an adversary can use the injected password to successfully authenticate as any domain user account (until the the skeleton key is erased from memory by a reboot of the domain controller). Authenticated access may enable unfettered access to hosts and/or resources within single-factor authentication environments.(Citation: Dell Skeleton)

### T1556.002: Password Filter DLL

^t1556002-password-filter-dll

Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process to acquire user credentials as they are validated. 

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as DLLs containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts. Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation. 

Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made.(Citation: Carnal Ownage Password Filters Sept 2013)

### T1556.003: Pluggable Authentication Modules

^t1556003-pluggable-authentication-modules

Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide authentication for many services. The most common authentication module is `pam_unix.so`, which retrieves, sets, and verifies account authentication information in `/etc/passwd` and `/etc/shadow`.(Citation: Apple PAM)(Citation: Man Pam_Unix)(Citation: Red Hat PAM)

Adversaries may modify components of the PAM system to create backdoors. PAM components, such as `pam_unix.so`, can be patched to accept arbitrary adversary supplied values as legitimate credentials.(Citation: PAM Backdoor)

Malicious modifications to the PAM system may also be abused to steal credentials. Adversaries may infect PAM resources with code to harvest user credentials, since the values exchanged with PAM components may be plain-text since PAM does not store passwords.(Citation: PAM Creds)(Citation: Apple PAM)

### T1556.004: Network Device Authentication

^t1556004-network-device-authentication

Adversaries may use [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]] to hard code a password in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.

[[T1601-modify_system_image|T1601: Modify System Image]] may include implanted code to the operating system for network devices to provide access for adversaries using a specific password.  The modification includes a specific password which is implanted in the operating system image via the patch.  Upon authentication attempts, the inserted code will first check to see if the user input is the password. If so, access is granted. Otherwise, the implanted code will pass the credentials on for verification of potentially valid credentials.(Citation: Mandiant - Synful Knock)

### T1556.005: Reversible Encryption

^t1556005-reversible-encryption

An adversary may abuse Active Directory authentication encryption properties to gain access to credentials on Windows systems. The `AllowReversiblePasswordEncryption` property specifies whether reversible password encryption for an account is enabled or disabled. By default this property is disabled (instead storing user credentials as the output of one-way hashing functions) and should not be enabled unless legacy or other software require it.(Citation: store_pwd_rev_enc)

If the property is enabled and/or a user changes their password after it is enabled, an adversary may be able to obtain the plaintext of passwords created/changed after the property was enabled. To decrypt the passwords, an adversary needs four components:

1. Encrypted password (`G$RADIUSCHAP`) from the Active Directory user-structure `userParameters`
2. 16 byte randomly-generated value (`G$RADIUSCHAPKEY`) also from `userParameters`
3. Global LSA secret (`G$MSRADIUSCHAPKEY`)
4. Static key hardcoded in the Remote Access Subauthentication DLL (`RASSFM.DLL`)

With this information, an adversary may be able to reproduce the encryption key and subsequently decrypt the encrypted password value.(Citation: how_pwd_rev_enc_1)(Citation: how_pwd_rev_enc_2)

An adversary may set this property at various scopes through Local Group Policy Editor, user properties, Fine-Grained Password Policy (FGPP), or via the ActiveDirectory [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] module. For example, an adversary may implement and apply a FGPP to users or groups if the Domain Functional Level is set to "Windows Server 2008" or higher.(Citation: dump_pwd_dcsync) In PowerShell, an adversary may make associated changes to user settings using commands similar to `Set-ADUser -AllowReversiblePasswordEncryption $true`.

### T1556.006: Multi-Factor Authentication

^t1556006-multi-factor-authentication

Adversaries may disable or modify multi-factor authentication (MFA) mechanisms to enable persistent access to compromised accounts.

Once adversaries have gained access to a network by either compromising an account lacking MFA or by employing an MFA bypass method such as [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]], adversaries may leverage their access to modify or completely disable MFA defenses. This can be accomplished by abusing legitimate features, such as excluding users from Azure AD Conditional Access Policies, registering a new yet vulnerable/adversary-controlled MFA method, or by manually patching MFA programs and configuration files to bypass expected functionality.(Citation: Mandiant APT42)(Citation: Azure AD Conditional Access Exclusions)

For example, modifying the Windows hosts file (`C:\windows\system32\drivers\etc\hosts`) to redirect MFA calls to localhost instead of an MFA server may cause the MFA process to fail. If a "fail open" policy is in place, any otherwise successful authentication attempt may be granted access without enforcing MFA. (Citation: Russians Exploit Default MFA Protocol - CISA March 2022) 

Depending on the scope, goals, and privileges of the adversary, MFA defenses may be disabled for individual accounts or for all accounts tied to a larger group, such as all domain accounts in a victim's network environment.(Citation: Russians Exploit Default MFA Protocol - CISA March 2022) 

### T1556.007: Hybrid Identity

^t1556007-hybrid-identity

Adversaries may patch, modify, or otherwise backdoor cloud authentication processes that are tied to on-premises user identities in order to bypass typical authentication mechanisms, access credentials, and enable persistent access to accounts.  

Many organizations maintain hybrid user and device identities that are shared between on-premises and cloud-based environments. These can be maintained in a number of ways. For example, Microsoft Entra ID includes three options for synchronizing identities between Active Directory and Entra ID(Citation: Azure AD Hybrid Identity):

* Password Hash Synchronization (PHS), in which a privileged on-premises account synchronizes user password hashes between Active Directory and Entra ID, allowing authentication to Entra ID to take place entirely in the cloud 
* Pass Through Authentication (PTA), in which Entra ID authentication attempts are forwarded to an on-premises PTA agent, which validates the credentials against Active Directory 
* Active Directory Federation Services (AD FS), in which a trust relationship is established between Active Directory and Entra ID 

AD FS can also be used with other SaaS and cloud platforms such as AWS and GCP, which will hand off the authentication process to AD FS and receive a token containing the hybrid users’ identity and privileges. 

By modifying authentication processes tied to hybrid identities, an adversary may be able to establish persistent privileged access to cloud resources. For example, adversaries who compromise an on-premises server running a PTA agent may inject a malicious DLL into the `AzureADConnectAuthenticationAgentService` process that authorizes all attempts to authenticate to Entra ID, as well as records user credentials.(Citation: Azure AD Connect for Read Teamers)(Citation: AADInternals Azure AD On-Prem to Cloud) In environments using AD FS, an adversary may edit the `Microsoft.IdentityServer.Servicehost` configuration file to load a malicious DLL that generates authentication tokens for any user with any set of claims, thereby bypassing multi-factor authentication and defined AD FS policies.(Citation: MagicWeb)

In some cases, adversaries may be able to modify the hybrid identity authentication process from the cloud. For example, adversaries who compromise a Global Administrator account in an Entra ID tenant may be able to register a new PTA agent via the web console, similarly allowing them to harvest credentials and log into the Entra ID environment as any user.(Citation: Mandiant Azure AD Backdoors)

### T1556.008: Network Provider DLL

^t1556008-network-provider-dll

Adversaries may register malicious network provider dynamic link libraries (DLLs) to capture cleartext user credentials during the authentication process. Network provider DLLs allow Windows to interface with specific network protocols and can also support add-on credential management functions.(Citation: Network Provider API) During the logon process, Winlogon (the interactive logon module) sends credentials to the local `mpnotify.exe` process via RPC. The `mpnotify.exe` process then shares the credentials in cleartext with registered credential managers when notifying that a logon event is happening.(Citation: NPPSPY - Huntress)(Citation: NPPSPY Video)(Citation: NPLogonNotify) 

Adversaries can configure a malicious network provider DLL to receive credentials from `mpnotify.exe`.(Citation: NPPSPY) Once installed as a credential manager (via the Registry), a malicious DLL can receive and save credentials each time a user logs onto a Windows workstation or domain via the `NPLogonNotify()` function.(Citation: NPLogonNotify)

Adversaries may target planting malicious network provider DLLs on systems known to have increased logon activity and/or administrator logon activity, such as servers and domain controllers.(Citation: NPPSPY - Huntress)

### T1556.009: Conditional Access Policies

^t1556009-conditional-access-policies

Adversaries may disable or modify conditional access policies to enable persistent access to compromised accounts. Conditional access policies are additional verifications used by identity providers and identity and access management systems to determine whether a user should be granted access to a resource.

For example, in Entra ID, Okta, and JumpCloud, users can be denied access to applications based on their IP address, device enrollment status, and use of multi-factor authentication.(Citation: Microsoft Conditional Access)(Citation: JumpCloud Conditional Access Policies)(Citation: Okta Conditional Access Policies) In some cases, identity providers may also support the use of risk-based metrics to deny sign-ins based on a variety of indicators. In AWS and GCP, IAM policies can contain `condition` attributes that verify arbitrary constraints such as the source IP, the date the request was made, and the nature of the resources or regions being requested.(Citation: AWS IAM Conditions)(Citation: GCP IAM Conditions) These measures help to prevent compromised credentials from resulting in unauthorized access to data or resources, as well as limit user permissions to only those required. 

By modifying conditional access policies, such as adding additional trusted IP ranges, removing [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]] requirements, or allowing additional [[T1535-unused_unsupported_cloud_regions|T1535: Unused/Unsupported Cloud Regions]], adversaries may be able to ensure persistent access to accounts and circumvent defensive measures.

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]
- [[M1025-privileged_process_integrity|M1025: Privileged Process Integrity]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[silenttrinity|SILENTTRINITY (S0692)]]

## Platforms

- Windows
- Linux
- macOS
- Network Devices
- IaaS
- SaaS
- Office Suite
- Identity Provider

