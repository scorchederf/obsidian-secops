---
mitre_id: "T1555"
mitre_name: "Credentials from Password Stores"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3fc9b85a-2862-4363-a64d-d692e3ffbee0"
mitre_created: "2020-02-11T18:48:28.456Z"
mitre_modified: "2025-10-24T17:48:41.974Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1555/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-DI"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RD"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Workspace

- [[workspaces/attack/techniques/T1555-credentials_from_password_stores-note|Open workspace note]]

![[workspaces/attack/techniques/T1555-credentials_from_password_stores-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Subtechniques

### T1555.001: Keychain

^t1555001-keychain

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. 

Keychains can be viewed and edited through the Keychain Access application or using the command-line utility `security`. Keychain files are located in `~/Library/Keychains/`, `/Library/Keychains/`, and `/Network/Library/Keychains/`.(Citation: Keychain Services Apple)(Citation: Keychain Decryption Passware)(Citation: OSX Keychain Schaumann)

Adversaries may gather user credentials from Keychain storage/memory. For example, the command `security dump-keychain –d` will dump all Login Keychain credentials from `~/Library/Keychains/login.keychain-db`. Adversaries may also directly read Login Keychain credentials from the `~/Library/Keychains/login.keychain` file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.(Citation: External to DA, the OS X Way)(Citation: Empire Keychain Decrypt)  

### T1555.002: Securityd Memory

^t1555002-securityd-memory

An adversary with root access may gather credentials by reading `securityd`’s memory. `securityd` is a service/daemon responsible for implementing security protocols such as encryption and authorization.(Citation: Apple Dev SecurityD) A privileged adversary may be able to scan through `securityd`'s memory to find the correct sequence of keys to decrypt the user’s logon keychain. This may provide the adversary with various plaintext passwords, such as those for users, WiFi, mail, browsers, certificates, secure notes, etc.(Citation: OS X Keychain)(Citation: OSX Keydnap malware)

In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords.(Citation: OS X Keychain)(Citation: External to DA, the OS X Way) Apple’s `securityd` utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.(Citation: OS X Keychain)

### T1555.003: Credentials from Web Browsers

^t1555003-credentials-from-web-browsers

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.(Citation: Talos Olympic Destroyer 2018) Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers.

For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, `AppData\Local\Google\Chrome\User Data\Default\Login Data` and executing a SQL query: `SELECT action_url, username_value, password_value FROM logins;`. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function `CryptUnprotectData`, which uses the victim’s cached logon credentials as the decryption key.(Citation: Microsoft CryptUnprotectData April 2018)
 
Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc.(Citation: Proofpoint Vega Credential Stealer May 2018)(Citation: FireEye HawkEye Malware July 2017) Windows stores Internet Explorer and Microsoft Edge credentials in Credential Lockers managed by the [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]].

Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials.(Citation: GitHub Mimikittenz July 2016)

After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

### T1555.004: Windows Credential Manager

^t1555004-windows-credential-manager

Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults).(Citation: Microsoft Credential Manager store)(Citation: Microsoft Credential Locker)

The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]], Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker.

Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named `Policy.vpol`, typically located in the same folder as the credentials.(Citation: passcape Windows Vault)(Citation: Malwarebytes The Windows Vault)

Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. `vaultcmd.exe` is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as `CredEnumerateA`, may also be absued to list credentials managed by the Credential Manager.(Citation: Microsoft CredEnumerate)(Citation: Delpy Mimikatz Crendential Manager)

Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running `rundll32.exe keymgr.dll KRShowKeyMgr` then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI.

Password recovery tools may also obtain plain text passwords from the Credential Manager.(Citation: Malwarebytes The Windows Vault)

### T1555.005: Password Managers

^t1555005-password-managers

Adversaries may acquire user credentials from third-party password managers.(Citation: ise Password Manager February 2019) Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk.(Citation: ise Password Manager February 2019)

Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory.(Citation: FoxIT Wocao December 2019)(Citation: Github KeeThief) Adversaries may extract credentials from memory via [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]].(Citation: NVD CVE-2019-3610)
 Adversaries may also try brute forcing via [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]] to obtain the master password of a password manager.(Citation: Cyberreason Anchor December 2019)

### T1555.006: Cloud Secrets Management Stores

^t1555006-cloud-secrets-management-stores

Adversaries may acquire credentials from cloud-native secret management solutions such as AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, and Terraform Vault.  

Secrets managers support the secure centralized management of passwords, API keys, and other credential material. Where secrets managers are in use, cloud services can dynamically acquire credentials via API requests rather than accessing secrets insecurely stored in plain text files or environment variables.  

If an adversary is able to gain sufficient privileges in a cloud environment – for example, by obtaining the credentials of high-privileged [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]] or compromising a service that has permission to retrieve secrets – they may be able to request secrets from the secrets manager. This can be accomplished via commands such as `get-secret-value` in AWS, `gcloud secrets describe` in GCP, and `az key vault secret show` in Azure.(Citation: Permiso Scattered Spider 2023)(Citation: Sysdig ScarletEel 2.0 2023)(Citation: AWS Secrets Manager)(Citation: Google Cloud Secrets)(Citation: Microsoft Azure Key Vault)

**Note:** this technique is distinct from [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]] in that the credentials are being directly requested from the cloud secrets manager, rather than through the medium of the instance metadata API.

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1051-update_software|M1051: Update Software]]

## Tools
- [[lazagne|LaZagne (S0349)]]
- [[mimikatz|Mimikatz (S0002)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]


## Platforms

- IaaS
- Linux
- macOS
- Windows

