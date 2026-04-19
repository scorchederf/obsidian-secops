---
id: T1555
name: Credentials from Password Stores
created: 2020-02-11 18:48:28.456000+00:00
modified: 2025-10-24 17:48:41.974000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding the credentials. There are also specific applications and services that store passwords to make them easier for users to manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Properties

- id: T1555
- name: Credentials from Password Stores
- created: 2020-02-11 18:48:28.456000+00:00
- modified: 2025-10-24 17:48:41.974000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1555.001: Keychain

^t1555001-keychain

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may acquire credentials from Keychain. Keychain (or Keychain Services) is the macOS credential management system that stores account names, passwords, private keys, certificates, sensitive application data, payment data, and secure notes. There are three types of Keychains: Login Keychain, System Keychain, and Local Items (iCloud) Keychain. The default Keychain is the Login Keychain, which stores user passwords and information. The System Keychain stores items accessed by the operating system, such as items shared among users on a host. The Local Items (iCloud) Keychain is used for items synced with Apple’s iCloud service. 

Keychains can be viewed and edited through the Keychain Access application or using the command-line utility <code>security</code>. Keychain files are located in <code>~/Library/Keychains/</code>, <code>/Library/Keychains/</code>, and <code>/Network/Library/Keychains/</code>.(Citation: Keychain Services Apple)(Citation: Keychain Decryption Passware)(Citation: OSX Keychain Schaumann)

Adversaries may gather user credentials from Keychain storage/memory. For example, the command <code>security dump-keychain –d</code> will dump all Login Keychain credentials from <code>~/Library/Keychains/login.keychain-db</code>. Adversaries may also directly read Login Keychain credentials from the <code>~/Library/Keychains/login.keychain</code> file. Both methods require a password, where the default password for the Login Keychain is the current user’s password to login to the macOS host.(Citation: External to DA, the OS X Way)(Citation: Empire Keychain Decrypt)  

#### Properties

- id: T1555.001
- name: Keychain
- created: 2020-02-12 18:55:24.728000+00:00
- modified: 2025-10-24 17:48:29.756000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1555.002: Securityd Memory

^t1555002-securityd-memory

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

An adversary with root access may gather credentials by reading `securityd`’s memory. `securityd` is a service/daemon responsible for implementing security protocols such as encryption and authorization.(Citation: Apple Dev SecurityD) A privileged adversary may be able to scan through `securityd`'s memory to find the correct sequence of keys to decrypt the user’s logon keychain. This may provide the adversary with various plaintext passwords, such as those for users, WiFi, mail, browsers, certificates, secure notes, etc.(Citation: OS X Keychain)(Citation: OSX Keydnap malware)

In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords.(Citation: OS X Keychain)(Citation: External to DA, the OS X Way) Apple’s `securityd` utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.(Citation: OS X Keychain)

#### Properties

- id: T1555.002
- name: Securityd Memory
- created: 2020-02-12 18:56:31.051000+00:00
- modified: 2025-10-24 17:48:28.055000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1555.003: Credentials from Web Browsers

^t1555003-credentials-from-web-browsers

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.(Citation: Talos Olympic Destroyer 2018) Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future. Web browsers typically store the credentials in an encrypted format within a credential store; however, methods exist to extract plaintext credentials from web browsers.

For example, on Windows systems, encrypted credentials may be obtained from Google Chrome by reading a database file, <code>AppData\Local\Google\Chrome\User Data\Default\Login Data</code> and executing a SQL query: <code>SELECT action_url, username_value, password_value FROM logins;</code>. The plaintext password can then be obtained by passing the encrypted credentials to the Windows API function <code>CryptUnprotectData</code>, which uses the victim’s cached logon credentials as the decryption key.(Citation: Microsoft CryptUnprotectData April 2018)
 
Adversaries have executed similar procedures for common web browsers such as FireFox, Safari, Edge, etc.(Citation: Proofpoint Vega Credential Stealer May 2018)(Citation: FireEye HawkEye Malware July 2017) Windows stores Internet Explorer and Microsoft Edge credentials in Credential Lockers managed by the [Windows Credential Manager](https://attack.mitre.org/techniques/T1555/004).

Adversaries may also acquire credentials by searching web browser process memory for patterns that commonly match credentials.(Citation: GitHub Mimikittenz July 2016)

After acquiring credentials from web browsers, adversaries may attempt to recycle the credentials across different systems and/or accounts in order to expand access. This can result in significantly furthering an adversary's objective in cases where credentials gained from web browsers overlap with privileged accounts (e.g. domain administrator).

#### Properties

- id: T1555.003
- name: Credentials from Web Browsers
- created: 2020-02-12 18:57:36.041000+00:00
- modified: 2025-10-24 17:48:49.577000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1555.004: Windows Credential Manager

^t1555004-windows-credential-manager

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may acquire credentials from the Windows Credential Manager. The Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos in Credential Lockers (previously known as Windows Vaults).(Citation: Microsoft Credential Manager store)(Citation: Microsoft Credential Locker)

The Windows Credential Manager separates website credentials from application or network credentials in two lockers. As part of [Credentials from Web Browsers](https://attack.mitre.org/techniques/T1555/003), Internet Explorer and Microsoft Edge website credentials are managed by the Credential Manager and are stored in the Web Credentials locker. Application and network credentials are stored in the Windows Credentials locker.

Credential Lockers store credentials in encrypted `.vcrd` files, located under `%Systemdrive%\Users\\[Username]\AppData\Local\Microsoft\\[Vault/Credentials]\`. The encryption key can be found in a file named <code>Policy.vpol</code>, typically located in the same folder as the credentials.(Citation: passcape Windows Vault)(Citation: Malwarebytes The Windows Vault)

Adversaries may list credentials managed by the Windows Credential Manager through several mechanisms. <code>vaultcmd.exe</code> is a native Windows executable that can be used to enumerate credentials stored in the Credential Locker through a command-line interface. Adversaries may also gather credentials by directly reading files located inside of the Credential Lockers. Windows APIs, such as <code>CredEnumerateA</code>, may also be absued to list credentials managed by the Credential Manager.(Citation: Microsoft CredEnumerate)(Citation: Delpy Mimikatz Crendential Manager)

Adversaries may also obtain credentials from credential backups. Credential backups and restorations may be performed by running <code>rundll32.exe keymgr.dll KRShowKeyMgr</code> then selecting the “Back up...” button on the “Stored User Names and Passwords” GUI.

Password recovery tools may also obtain plain text passwords from the Credential Manager.(Citation: Malwarebytes The Windows Vault)

#### Properties

- id: T1555.004
- name: Windows Credential Manager
- created: 2020-11-23 15:35:53.793000+00:00
- modified: 2025-10-24 17:49:26.444000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1555.005: Password Managers

^t1555005-password-managers

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may acquire user credentials from third-party password managers.(Citation: ise Password Manager February 2019) Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk.(Citation: ise Password Manager February 2019)

Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory.(Citation: FoxIT Wocao December 2019)(Citation: Github KeeThief) Adversaries may extract credentials from memory via [Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212).(Citation: NVD CVE-2019-3610)
 Adversaries may also try brute forcing via [Password Guessing](https://attack.mitre.org/techniques/T1110/001) to obtain the master password of a password manager.(Citation: Cyberreason Anchor December 2019)

#### Properties

- id: T1555.005
- name: Password Managers
- created: 2021-01-22 16:08:40.629000+00:00
- modified: 2025-10-24 17:48:36.347000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1555.006: Cloud Secrets Management Stores

^t1555006-cloud-secrets-management-stores

**Parent Technique**
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may acquire credentials from cloud-native secret management solutions such as AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, and Terraform Vault.  

Secrets managers support the secure centralized management of passwords, API keys, and other credential material. Where secrets managers are in use, cloud services can dynamically acquire credentials via API requests rather than accessing secrets insecurely stored in plain text files or environment variables.  

If an adversary is able to gain sufficient privileges in a cloud environment – for example, by obtaining the credentials of high-privileged [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004) or compromising a service that has permission to retrieve secrets – they may be able to request secrets from the secrets manager. This can be accomplished via commands such as `get-secret-value` in AWS, `gcloud secrets describe` in GCP, and `az key vault secret show` in Azure.(Citation: Permiso Scattered Spider 2023)(Citation: Sysdig ScarletEel 2.0 2023)(Citation: AWS Secrets Manager)(Citation: Google Cloud Secrets)(Citation: Microsoft Azure Key Vault)

**Note:** this technique is distinct from [Cloud Instance Metadata API](https://attack.mitre.org/techniques/T1552/005) in that the credentials are being directly requested from the cloud secrets manager, rather than through the medium of the instance metadata API.

#### Properties

- id: T1555.006
- name: Cloud Secrets Management Stores
- created: 2023-09-25 12:41:26.501000+00:00
- modified: 2025-04-15 22:03:00.834000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- IaaS
- Linux
- macOS
- Windows

## Tools

- [[S0002-mimikatz|S0002: Mimikatz]]
- [[S0192-pupy|S0192: Pupy]]
- [[S0262-quasarrat|S0262: QuasarRAT]]
- [[S0349-lazagne|S0349: LaZagne]]
- [[S0378-poshc2|S0378: PoshC2]]

