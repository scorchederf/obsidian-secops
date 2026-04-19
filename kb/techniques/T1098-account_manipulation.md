---
id: T1098
name: Account Manipulation
created: 2017-05-31 21:31:12.196000+00:00
modified: 2025-10-24 17:49:10.273000+00:00
type: attack-pattern
x_mitre_version: 2.8
x_mitre_domains: enterprise-attack
---

## Tactic

- [[privilege_escalation|Privilege Escalation]]

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## Subtechniques

### T1098.001: Additional Cloud Credentials
^t1098001-additional-cloud-credentials

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may add adversary-controlled credentials to a cloud account to maintain persistent access to victim accounts and instances within the environment.

For example, adversaries may add credentials for Service Principals and Applications in addition to existing legitimate credentials in Azure / Entra ID.(Citation: Microsoft SolarWinds Customer Guidance)(Citation: Blue Cloud of Death)(Citation: Blue Cloud of Death Video) These credentials include both x509 keys and passwords.(Citation: Microsoft SolarWinds Customer Guidance) With sufficient permissions, there are a variety of ways to add credentials including the Azure Portal, Azure command line interface, and Azure or Az PowerShell modules.(Citation: Demystifying Azure AD Service Principals)

In infrastructure-as-a-service (IaaS) environments, after gaining access through [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004), adversaries may generate or import their own SSH keys using either the <code>CreateKeyPair</code> or <code>ImportKeyPair</code> API in AWS or the <code>gcloud compute os-login ssh-keys add</code> command in GCP.(Citation: GCP SSH Key Add) This allows persistent access to instances within the cloud environment without further usage of the compromised cloud accounts.(Citation: Expel IO Evil in AWS)(Citation: Expel Behind the Scenes)

Adversaries may also use the <code>CreateAccessKey</code> API in AWS or the <code>gcloud iam service-accounts keys create</code> command in GCP to add access keys to an account. Alternatively, they may use the <code>CreateLoginProfile</code> API in AWS to add a password that can be used to log into the AWS Management Console for [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538).(Citation: Permiso Scattered Spider 2023)(Citation: Lacework AI Resource Hijacking 2024) If the target account has different permissions from the requesting account, the adversary may also be able to escalate their privileges in the environment (i.e. [Cloud Accounts](https://attack.mitre.org/techniques/T1078/004)).(Citation: Rhino Security Labs AWS Privilege Escalation)(Citation: Sysdig ScarletEel 2.0) For example, in Entra ID environments, an adversary with the Application Administrator role can add a new set of credentials to their application's service principal. In doing so the adversary would be able to access the service principal’s roles and permissions, which may be different from those of the Application Administrator.(Citation: SpecterOps Azure Privilege Escalation) 

In AWS environments, adversaries with the appropriate permissions may also use the `sts:GetFederationToken` API call to create a temporary set of credentials to [Forge Web Credentials](https://attack.mitre.org/techniques/T1606) tied to the permissions of the original user account. These temporary credentials may remain valid for the duration of their lifetime even if the original account’s API credentials are deactivated.
(Citation: Crowdstrike AWS User Federation Persistence)

In Entra ID environments with the app password feature enabled, adversaries may be able to add an app password to a user account.(Citation: Mandiant APT42 Operations 2024) As app passwords are intended to be used with legacy devices that do not support multi-factor authentication (MFA), adding an app password can allow an adversary to bypass MFA requirements. Additionally, app passwords may remain valid even if the user’s primary password is reset.(Citation: Microsoft Entra ID App Passwords)

#### Properties

- id: T1098.001
- name: Additional Cloud Credentials
- created: 2020-01-19 16:10:15.008000+00:00
- modified: 2025-10-24 17:49:04.839000+00:00
- type: attack-pattern
- x_mitre_version: 2.8
- x_mitre_domains: enterprise-attack

### T1098.002: Additional Email Delegate Permissions
^t1098002-additional-email-delegate-permissions

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled email account. 

For example, the <code>Add-MailboxPermission</code> [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlet, available in on-premises Exchange and in the cloud-based service Office 365, adds permissions to a mailbox.(Citation: Microsoft - Add-MailboxPermission)(Citation: FireEye APT35 2018)(Citation: Crowdstrike Hiding in Plain Sight 2018) In Google Workspace, delegation can be enabled via the Google Admin console and users can delegate accounts via their Gmail settings.(Citation: Gmail Delegation)(Citation: Google Ensuring Your Information is Safe) 

Adversaries may also assign mailbox folder permissions through individual folder permissions or roles. In Office 365 environments, adversaries may assign the Default or Anonymous user permissions or roles to the Top of Information Store (root), Inbox, or other mailbox folders. By assigning one or both user permissions to a folder, the adversary can utilize any other account in the tenant to maintain persistence to the target user’s mail folders.(Citation: Mandiant Defend UNC2452 White Paper)

This may be used in persistent threat incidents as well as BEC (Business Email Compromise) incidents where an adversary can add [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003) to the accounts they wish to compromise. This may further enable use of additional techniques for gaining access to systems. For example, compromised business accounts are often used to send messages to other accounts in the network of the target business while creating inbox rules (ex: [Internal Spearphishing](https://attack.mitre.org/techniques/T1534)), so the messages evade spam/phishing detection mechanisms.(Citation: Bienstock, D. - Defending O365 - 2019)

#### Properties

- id: T1098.002
- name: Additional Email Delegate Permissions
- created: 2020-01-19 16:54:28.516000+00:00
- modified: 2025-10-24 17:49:32.801000+00:00
- type: attack-pattern
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

### T1098.003: Additional Cloud Roles
^t1098003-additional-cloud-roles

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Policies and Permissions)(Citation: Google Cloud IAM Policies)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: Microsoft O365 Admin Roles) With sufficient permissions, a compromised account can gain almost unlimited access to data and settings (including the ability to reset the passwords of other admins).(Citation: Expel AWS Attacker)
(Citation: Microsoft O365 Admin Roles) 

This account modification may immediately follow [Create Account](https://attack.mitre.org/techniques/T1136) or other malicious account activity. Adversaries may also modify existing [Valid Accounts](https://attack.mitre.org/techniques/T1078) that they have compromised. This could lead to privilege escalation, particularly if the roles added allow for lateral movement to additional accounts.

For example, in AWS environments, an adversary with appropriate permissions may be able to use the <code>CreatePolicyVersion</code> API to define a new version of an IAM policy or the <code>AttachUserPolicy</code> API to attach an IAM policy with additional or distinct permissions to a compromised user account.(Citation: Rhino Security Labs AWS Privilege Escalation)

In some cases, adversaries may add roles to adversary-controlled accounts outside the victim cloud tenant. This allows these external accounts to perform actions inside the victim tenant without requiring the adversary to [Create Account](https://attack.mitre.org/techniques/T1136) or modify a victim-owned account.(Citation: Invictus IR DangerDev 2024)

#### Properties

- id: T1098.003
- name: Additional Cloud Roles
- created: 2020-01-19 16:59:45.362000+00:00
- modified: 2025-10-24 17:48:35.082000+00:00
- type: attack-pattern
- x_mitre_version: 2.5
- x_mitre_domains: enterprise-attack

### T1098.004: SSH Authorized Keys
^t1098004-ssh-authorized-keys

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may modify the SSH <code>authorized_keys</code> file to maintain persistence on a victim host. Linux distributions, macOS, and ESXi hypervisors commonly use key-based authentication to secure the authentication process of SSH sessions for remote management. The <code>authorized_keys</code> file in SSH specifies the SSH keys that can be used for logging into the user account for which the file is configured. This file is usually found in the user's home directory under <code>&lt;user-home&gt;/.ssh/authorized_keys</code> (or, on ESXi, `/etc/ssh/keys-<username>/authorized_keys`).(Citation: SSH Authorized Keys) Users may edit the system’s SSH config file to modify the directives `PubkeyAuthentication` and `RSAAuthentication` to the value `yes` to ensure public key and RSA authentication are enabled, as well as modify the directive `PermitRootLogin` to the value `yes` to enable root authentication via SSH.(Citation: Broadcom ESXi SSH) The SSH config file is usually located under <code>/etc/ssh/sshd_config</code>.

Adversaries may modify SSH <code>authorized_keys</code> files directly with scripts or shell commands to add their own adversary-supplied public keys. In cloud environments, adversaries may be able to modify the SSH authorized_keys file of a particular virtual machine via the command line interface or rest API. For example, by using the Google Cloud CLI’s “add-metadata” command an adversary may add SSH keys to a user account.(Citation: Google Cloud Add Metadata)(Citation: Google Cloud Privilege Escalation) Similarly, in Azure, an adversary may update the authorized_keys file of a virtual machine via a PATCH request to the API.(Citation: Azure Update Virtual Machines) This ensures that an adversary possessing the corresponding private key may log in as an existing user via SSH.(Citation: Venafi SSH Key Abuse)(Citation: Cybereason Linux Exim Worm) It may also lead to privilege escalation where the virtual machine or instance has distinct permissions from the requesting user.

Where authorized_keys files are modified via cloud APIs or command line interfaces, an adversary may achieve privilege escalation on the target virtual machine if they add a key to a higher-privileged user. 

SSH keys can also be added to accounts on network devices, such as with the `ip ssh pubkey-chain` [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) command.(Citation: cisco_ip_ssh_pubkey_ch_cmd)

#### Properties

- id: T1098.004
- name: SSH Authorized Keys
- created: 2020-06-24 12:42:35.144000+00:00
- modified: 2025-10-24 17:48:55.005000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1098.005: Device Registration
^t1098005-device-registration

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance.

MFA systems, such as Duo or Okta, allow users to associate devices with their accounts in order to complete MFA requirements. An adversary that compromises a user’s credentials may enroll a new device in order to bypass initial MFA requirements and gain persistent access to a network.(Citation: CISA MFA PrintNightmare)(Citation: DarkReading FireEye SolarWinds) In some cases, the MFA self-enrollment process may require only a username and password to enroll the account's first device or to enroll a device to an inactive account. (Citation: Mandiant APT29 Microsoft 365 2022)

Similarly, an adversary with existing access to a network may register a device or a virtual machine to Entra ID and/or its device management system, Microsoft Intune, in order to access sensitive data or resources while bypassing conditional access policies.(Citation: AADInternals - Device Registration)(Citation: AADInternals - Conditional Access Bypass)(Citation: Microsoft DEV-0537)(Citation: Expel Atlas Lion 2025)

Devices registered in Entra ID may be able to conduct [Internal Spearphishing](https://attack.mitre.org/techniques/T1534) campaigns via intra-organizational emails, which are less likely to be treated as suspicious by the email client.(Citation: Microsoft - Device Registration) Additionally, an adversary may be able to perform a [Service Exhaustion Flood](https://attack.mitre.org/techniques/T1499/002) on an Entra ID tenant by registering a large number of devices.(Citation: AADInternals - BPRT)

#### Properties

- id: T1098.005
- name: Device Registration
- created: 2022-03-04 18:30:38.989000+00:00
- modified: 2025-05-22 21:02:06.575000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1098.006: Additional Container Cluster Roles
^t1098006-additional-container-cluster-roles

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

An adversary may add additional roles or permissions to an adversary-controlled user or service account to maintain persistent access to a container orchestration system. For example, an adversary with sufficient permissions may create a RoleBinding or a ClusterRoleBinding to bind a Role or ClusterRole to a Kubernetes account.(Citation: Kubernetes RBAC)(Citation: Aquasec Kubernetes Attack 2023) Where attribute-based access control (ABAC) is in use, an adversary with sufficient permissions may modify a Kubernetes ABAC policy to give the target account additional permissions.(Citation: Kuberentes ABAC)
 
This account modification may immediately follow [Create Account](https://attack.mitre.org/techniques/T1136) or other malicious account activity. Adversaries may also modify existing [Valid Accounts](https://attack.mitre.org/techniques/T1078) that they have compromised.  

Note that where container orchestration systems are deployed in cloud environments, as with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Azure Kubernetes Service, cloud-based  role-based access control (RBAC) assignments or ABAC policies can often be used in place of or in addition to local permission assignments.(Citation: Google Cloud Kubernetes IAM)(Citation: AWS EKS IAM Roles for Service Accounts)(Citation: Microsoft Azure Kubernetes Service Service Accounts) In these cases, this technique may be used in conjunction with [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003).

#### Properties

- id: T1098.006
- name: Additional Container Cluster Roles
- created: 2023-07-14 14:01:50.806000+00:00
- modified: 2025-04-15 21:46:31.661000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1098.007: Additional Local or Domain Groups
^t1098007-additional-local-or-domain-groups

**Parent Technique**
- [[T1098-account_manipulation|T1098: Account Manipulation]]

**Tactic**
- [[privilege_escalation|Privilege Escalation]]

An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent access to a system or domain.

On Windows, accounts may use the `net localgroup` and `net group` commands to add existing users to local and domain groups.(Citation: Microsoft Net Localgroup)(Citation: Microsoft Net Group) On Linux, adversaries may use the `usermod` command for the same purpose.(Citation: Linux Usermod)

For example, accounts may be added to the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote Desktop Users group, which allows them to leverage [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) to log into the endpoints in the future.(Citation: Microsoft RDP Logons) Adversaries may also add accounts to VPN user groups to gain future persistence on the network.(Citation: Cyber Security News) On Linux, accounts may be added to the sudoers group, allowing them to persistently leverage [Sudo and Sudo Caching](https://attack.mitre.org/techniques/T1548/003) for elevated privileges. 

In Windows environments, machine accounts may also be added to domain groups. This allows the local SYSTEM account to gain privileges on the domain.(Citation: RootDSE AD Detection 2022)

#### Properties

- id: T1098.007
- name: Additional Local or Domain Groups
- created: 2024-08-05 20:49:49.809000+00:00
- modified: 2025-09-26 18:25:02.290000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

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

## Tools

- [[mimikatz|Mimikatz]]

