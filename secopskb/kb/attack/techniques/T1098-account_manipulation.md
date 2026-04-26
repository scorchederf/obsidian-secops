---
mitre_id: "T1098"
mitre_name: "Account Manipulation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a10641f4-87b4-45a3-a906-92a149cb2c27"
mitre_created: "2017-05-31T21:31:12.196Z"
mitre_modified: "2025-10-24T17:49:10.273Z"
mitre_version: "2.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1098/"
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
  - "TA0003"
  - "TA0004"
d3fend_ids:
  - "D3-AA"
  - "D3-AL"
  - "D3-AM"
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
  - "D3-DAM"
  - "D3-DUC"
  - "D3-MFA"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RIC"
  - "D3-RTSD"
  - "D3-RUAA"
  - "D3-UAP"
  - "D3-UGLPA"
  - "D3-ULA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [[T1078-valid_accounts|T1078: Valid Accounts]].

## Workspace

- [[workspaces/attack/techniques/T1098-account_manipulation-note|Open workspace note]]

![[workspaces/attack/techniques/T1098-account_manipulation-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## D3FEND

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]
- [[D3-AL-account_locking|D3-AL: Account Locking]]
- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
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
- [[D3-DAM-domain_account_monitoring|D3-DAM: Domain Account Monitoring]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-RUAA-restore_user_account_access|D3-RUAA: Restore User Account Access]]
- [[D3-UAP-user_account_permissions|D3-UAP: User Account Permissions]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-ULA-unlock_account|D3-ULA: Unlock Account]]

## Subtechniques

### T1098.001: Additional Cloud Credentials

^t1098001-additional-cloud-credentials

Adversaries may add adversary-controlled credentials to a cloud account to maintain persistent access to victim accounts and instances within the environment.

For example, adversaries may add credentials for Service Principals and Applications in addition to existing legitimate credentials in Azure / Entra ID.(Citation: Microsoft SolarWinds Customer Guidance)(Citation: Blue Cloud of Death)(Citation: Blue Cloud of Death Video) These credentials include both x509 keys and passwords.(Citation: Microsoft SolarWinds Customer Guidance) With sufficient permissions, there are a variety of ways to add credentials including the Azure Portal, Azure command line interface, and Azure or Az PowerShell modules.(Citation: Demystifying Azure AD Service Principals)

In infrastructure-as-a-service (IaaS) environments, after gaining access through [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]], adversaries may generate or import their own SSH keys using either the `CreateKeyPair` or `ImportKeyPair` API in AWS or the `gcloud compute os-login ssh-keys add` command in GCP.(Citation: GCP SSH Key Add) This allows persistent access to instances within the cloud environment without further usage of the compromised cloud accounts.(Citation: Expel IO Evil in AWS)(Citation: Expel Behind the Scenes)

Adversaries may also use the `CreateAccessKey` API in AWS or the `gcloud iam service-accounts keys create` command in GCP to add access keys to an account. Alternatively, they may use the `CreateLoginProfile` API in AWS to add a password that can be used to log into the AWS Management Console for [[T1538-cloud_service_dashboard|T1538: Cloud Service Dashboard]].(Citation: Permiso Scattered Spider 2023)(Citation: Lacework AI Resource Hijacking 2024) If the target account has different permissions from the requesting account, the adversary may also be able to escalate their privileges in the environment (i.e. [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]).(Citation: Rhino Security Labs AWS Privilege Escalation)(Citation: Sysdig ScarletEel 2.0) For example, in Entra ID environments, an adversary with the Application Administrator role can add a new set of credentials to their application's service principal. In doing so the adversary would be able to access the service principal’s roles and permissions, which may be different from those of the Application Administrator.(Citation: SpecterOps Azure Privilege Escalation) 

In AWS environments, adversaries with the appropriate permissions may also use the `sts:GetFederationToken` API call to create a temporary set of credentials to [[T1606-forge_web_credentials|T1606: Forge Web Credentials]] tied to the permissions of the original user account. These temporary credentials may remain valid for the duration of their lifetime even if the original account’s API credentials are deactivated.
(Citation: Crowdstrike AWS User Federation Persistence)

In Entra ID environments with the app password feature enabled, adversaries may be able to add an app password to a user account.(Citation: Mandiant APT42 Operations 2024) As app passwords are intended to be used with legacy devices that do not support multi-factor authentication (MFA), adding an app password can allow an adversary to bypass MFA requirements. Additionally, app passwords may remain valid even if the user’s primary password is reset.(Citation: Microsoft Entra ID App Passwords)

### T1098.002: Additional Email Delegate Permissions

^t1098002-additional-email-delegate-permissions

Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled email account. 

For example, the `Add-MailboxPermission` [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] cmdlet, available in on-premises Exchange and in the cloud-based service Office 365, adds permissions to a mailbox.(Citation: Microsoft - Add-MailboxPermission)(Citation: FireEye APT35 2018)(Citation: Crowdstrike Hiding in Plain Sight 2018) In Google Workspace, delegation can be enabled via the Google Admin console and users can delegate accounts via their Gmail settings.(Citation: Gmail Delegation)(Citation: Google Ensuring Your Information is Safe) 

Adversaries may also assign mailbox folder permissions through individual folder permissions or roles. In Office 365 environments, adversaries may assign the Default or Anonymous user permissions or roles to the Top of Information Store (root), Inbox, or other mailbox folders. By assigning one or both user permissions to a folder, the adversary can utilize any other account in the tenant to maintain persistence to the target user’s mail folders.(Citation: Mandiant Defend UNC2452 White Paper)

This may be used in persistent threat incidents as well as BEC (Business Email Compromise) incidents where an adversary can add [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]] to the accounts they wish to compromise. This may further enable use of additional techniques for gaining access to systems. For example, compromised business accounts are often used to send messages to other accounts in the network of the target business while creating inbox rules (ex: [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]), so the messages evade spam/phishing detection mechanisms.(Citation: Bienstock, D. - Defending O365 - 2019)

### T1098.003: Additional Cloud Roles

^t1098003-additional-cloud-roles

An adversary may add additional roles or permissions to an adversary-controlled cloud account to maintain persistent access to a tenant. For example, adversaries may update IAM policies in cloud-based environments or add a new global administrator in Office 365 environments.(Citation: AWS IAM Policies and Permissions)(Citation: Google Cloud IAM Policies)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: Microsoft O365 Admin Roles) With sufficient permissions, a compromised account can gain almost unlimited access to data and settings (including the ability to reset the passwords of other admins).(Citation: Expel AWS Attacker)
(Citation: Microsoft O365 Admin Roles) 

This account modification may immediately follow [[T1136-create_account|T1136: Create Account]] or other malicious account activity. Adversaries may also modify existing [[T1078-valid_accounts|T1078: Valid Accounts]] that they have compromised. This could lead to privilege escalation, particularly if the roles added allow for lateral movement to additional accounts.

For example, in AWS environments, an adversary with appropriate permissions may be able to use the `CreatePolicyVersion` API to define a new version of an IAM policy or the `AttachUserPolicy` API to attach an IAM policy with additional or distinct permissions to a compromised user account.(Citation: Rhino Security Labs AWS Privilege Escalation)

In some cases, adversaries may add roles to adversary-controlled accounts outside the victim cloud tenant. This allows these external accounts to perform actions inside the victim tenant without requiring the adversary to [[T1136-create_account|T1136: Create Account]] or modify a victim-owned account.(Citation: Invictus IR DangerDev 2024)

### T1098.004: SSH Authorized Keys

^t1098004-ssh-authorized-keys

Adversaries may modify the SSH `authorized_keys` file to maintain persistence on a victim host. Linux distributions, macOS, and ESXi hypervisors commonly use key-based authentication to secure the authentication process of SSH sessions for remote management. The `authorized_keys` file in SSH specifies the SSH keys that can be used for logging into the user account for which the file is configured. This file is usually found in the user's home directory under `&lt;user-home&gt;/.ssh/authorized_keys` (or, on ESXi, `/etc/ssh/keys-<username>/authorized_keys`).(Citation: SSH Authorized Keys) Users may edit the system’s SSH config file to modify the directives `PubkeyAuthentication` and `RSAAuthentication` to the value `yes` to ensure public key and RSA authentication are enabled, as well as modify the directive `PermitRootLogin` to the value `yes` to enable root authentication via SSH.(Citation: Broadcom ESXi SSH) The SSH config file is usually located under `/etc/ssh/sshd_config`.

Adversaries may modify SSH `authorized_keys` files directly with scripts or shell commands to add their own adversary-supplied public keys. In cloud environments, adversaries may be able to modify the SSH authorized_keys file of a particular virtual machine via the command line interface or rest API. For example, by using the Google Cloud CLI’s “add-metadata” command an adversary may add SSH keys to a user account.(Citation: Google Cloud Add Metadata)(Citation: Google Cloud Privilege Escalation) Similarly, in Azure, an adversary may update the authorized_keys file of a virtual machine via a PATCH request to the API.(Citation: Azure Update Virtual Machines) This ensures that an adversary possessing the corresponding private key may log in as an existing user via SSH.(Citation: Venafi SSH Key Abuse)(Citation: Cybereason Linux Exim Worm) It may also lead to privilege escalation where the virtual machine or instance has distinct permissions from the requesting user.

Where authorized_keys files are modified via cloud APIs or command line interfaces, an adversary may achieve privilege escalation on the target virtual machine if they add a key to a higher-privileged user. 

SSH keys can also be added to accounts on network devices, such as with the `ip ssh pubkey-chain` [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] command.(Citation: cisco_ip_ssh_pubkey_ch_cmd)

### T1098.005: Device Registration

^t1098005-device-registration

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance.

MFA systems, such as Duo or Okta, allow users to associate devices with their accounts in order to complete MFA requirements. An adversary that compromises a user’s credentials may enroll a new device in order to bypass initial MFA requirements and gain persistent access to a network.(Citation: CISA MFA PrintNightmare)(Citation: DarkReading FireEye SolarWinds) In some cases, the MFA self-enrollment process may require only a username and password to enroll the account's first device or to enroll a device to an inactive account. (Citation: Mandiant APT29 Microsoft 365 2022)

Similarly, an adversary with existing access to a network may register a device or a virtual machine to Entra ID and/or its device management system, Microsoft Intune, in order to access sensitive data or resources while bypassing conditional access policies.(Citation: AADInternals - Device Registration)(Citation: AADInternals - Conditional Access Bypass)(Citation: Microsoft DEV-0537)(Citation: Expel Atlas Lion 2025)

Devices registered in Entra ID may be able to conduct [[T1534-internal_spearphishing|T1534: Internal Spearphishing]] campaigns via intra-organizational emails, which are less likely to be treated as suspicious by the email client.(Citation: Microsoft - Device Registration) Additionally, an adversary may be able to perform a [[T1499-endpoint_denial_of_service#^t1499002-service-exhaustion-flood|T1499.002: Service Exhaustion Flood]] on an Entra ID tenant by registering a large number of devices.(Citation: AADInternals - BPRT)

### T1098.006: Additional Container Cluster Roles

^t1098006-additional-container-cluster-roles

An adversary may add additional roles or permissions to an adversary-controlled user or service account to maintain persistent access to a container orchestration system. For example, an adversary with sufficient permissions may create a RoleBinding or a ClusterRoleBinding to bind a Role or ClusterRole to a Kubernetes account.(Citation: Kubernetes RBAC)(Citation: Aquasec Kubernetes Attack 2023) Where attribute-based access control (ABAC) is in use, an adversary with sufficient permissions may modify a Kubernetes ABAC policy to give the target account additional permissions.(Citation: Kuberentes ABAC)
 
This account modification may immediately follow [[T1136-create_account|T1136: Create Account]] or other malicious account activity. Adversaries may also modify existing [[T1078-valid_accounts|T1078: Valid Accounts]] that they have compromised.  

Note that where container orchestration systems are deployed in cloud environments, as with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Azure Kubernetes Service, cloud-based  role-based access control (RBAC) assignments or ABAC policies can often be used in place of or in addition to local permission assignments.(Citation: Google Cloud Kubernetes IAM)(Citation: AWS EKS IAM Roles for Service Accounts)(Citation: Microsoft Azure Kubernetes Service Service Accounts) In these cases, this technique may be used in conjunction with [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]].

### T1098.007: Additional Local or Domain Groups

^t1098007-additional-local-or-domain-groups

An adversary may add additional local or domain groups to an adversary-controlled account to maintain persistent access to a system or domain.

On Windows, accounts may use the `net localgroup` and `net group` commands to add existing users to local and domain groups.(Citation: Microsoft Net Localgroup)(Citation: Microsoft Net Group) On Linux, adversaries may use the `usermod` command for the same purpose.(Citation: Linux Usermod)

For example, accounts may be added to the local administrators group on Windows devices to maintain elevated privileges. They may also be added to the Remote Desktop Users group, which allows them to leverage [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]] to log into the endpoints in the future.(Citation: Microsoft RDP Logons) Adversaries may also add accounts to VPN user groups to gain future persistence on the network.(Citation: Cyber Security News) On Linux, accounts may be added to the sudoers group, allowing them to persistently leverage [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]] for elevated privileges. 

In Windows environments, machine accounts may also be added to domain groups. This allows the local SYSTEM account to gain privileges on the domain.(Citation: RootDSE AD Detection 2022)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Tools

- [[mimikatz|Mimikatz (S0002)]]

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

