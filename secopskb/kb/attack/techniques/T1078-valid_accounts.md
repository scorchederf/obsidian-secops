---
mitre_id: "T1078"
mitre_name: "Valid Accounts"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b17a1a56-e99c-403c-8948-561df0cffe81"
mitre_created: "2017-05-31T21:31:00.645Z"
mitre_modified: "2025-10-24T17:49:14.095Z"
mitre_version: "2.8"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1078/"
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
  - "TA0005"
  - "TA0003"
  - "TA0004"
  - "TA0001"
d3fend_ids:
  - "D3-AA"
  - "D3-AL"
  - "D3-AM"
  - "D3-CDP"
  - "D3-DAM"
  - "D3-LAM"
  - "D3-RUAA"
  - "D3-UAP"
  - "D3-ULA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop.(Citation: volexity_0day_sophos_FW) Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.

In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account.(Citation: CISA MFA PrintNightmare)

The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise.(Citation: TechNet Credential Theft)

## Workspace

- [[workspaces/attack/techniques/T1078-valid_accounts-note|Open workspace note]]

![[workspaces/attack/techniques/T1078-valid_accounts-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]
- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]
- [[D3-AL-account_locking|D3-AL: Account Locking]]
- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CDP-change_default_password|D3-CDP: Change Default Password]]
- [[D3-DAM-domain_account_monitoring|D3-DAM: Domain Account Monitoring]]
- [[D3-LAM-local_account_monitoring|D3-LAM: Local Account Monitoring]]
- [[D3-RUAA-restore_user_account_access|D3-RUAA: Restore User Account Access]]
- [[D3-UAP-user_account_permissions|D3-UAP: User Account Permissions]]
- [[D3-ULA-unlock_account|D3-ULA: Unlock Account]]

## Subtechniques

### T1078.001: Default Accounts

^t1078001-default-accounts

Adversaries may obtain and abuse credentials of a default account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Default accounts are those that are built-into an OS, such as the Guest or Administrator accounts on Windows systems. Default accounts also include default factory/provider set accounts on other types of systems, software, or devices, including the root user account in AWS, the root user account in ESXi, and the default service account in Kubernetes.(Citation: Microsoft Local Accounts Feb 2019)(Citation: AWS Root User)(Citation: Threat Matrix for Kubernetes)

Default accounts are not limited to client machines; rather, they also include accounts that are preset for equipment such as network devices and computer applications, whether they are internal, open source, or commercial. Appliances that come preset with a username and password combination pose a serious threat to organizations that do not change it post installation, as they are easy targets for an adversary. Similarly, adversaries may also utilize publicly disclosed or stolen [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]] or credential materials to legitimately connect to remote environments via [[T1021-remote_services|T1021: Remote Services]].(Citation: Metasploit SSH Module)

Default accounts may be created on a system after initial setup by connecting or integrating it with another application. For example, when an ESXi server is connected to a vCenter server, a default privileged account called `vpxuser` is created on the ESXi server. If a threat actor is able to compromise this account’s credentials (for example, via [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]] on the vCenter host), they will then have access to the ESXi server.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Pentera vCenter Information Disclosure)

### T1078.002: Domain Accounts

^t1078002-domain-accounts

Adversaries may obtain and abuse credentials of a domain account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion.(Citation: TechNet Credential Theft) Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover users, administrators, and services.(Citation: Microsoft AD Accounts)

Adversaries may compromise domain accounts, some with a high level of privileges, through various means such as [[T1003-os_credential_dumping|T1003: OS Credential Dumping]] or password reuse, allowing access to privileged resources of the domain.

### T1078.003: Local Accounts

^t1078003-local-accounts

Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service.

Local Accounts may also be abused to elevate privileges and harvest credentials through [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]. Password reuse may allow the abuse of local accounts across a set of machines on a network for the purposes of Privilege Escalation and Lateral Movement. 

### T1078.004: Cloud Accounts

^t1078004-cloud-accounts

Valid accounts in cloud environments may allow adversaries to perform actions to achieve Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application. Cloud Accounts can exist solely in the cloud; alternatively, they may be hybrid-joined between on-premises systems and the cloud through syncing or federation with other identity sources such as Windows Active Directory.(Citation: AWS Identity Federation)(Citation: Google Federating GC)(Citation: Microsoft Deploying AD Federation)

Service or user accounts may be targeted by adversaries through [[T1110-brute_force|T1110: Brute Force]], [[T1566-phishing|T1566: Phishing]], or various other means to gain access to the environment. Federated or synced accounts may be a pathway for the adversary to affect both on-premises systems and cloud environments - for example, by leveraging shared credentials to log onto [[T1021-remote_services|T1021: Remote Services]]. High privileged cloud accounts, whether federated, synced, or cloud-only, may also allow pivoting to on-premises environments by leveraging SaaS-based [[T1072-software_deployment_tools|T1072: Software Deployment Tools]] to run commands on hybrid-joined devices.

An adversary may create long lasting [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]] on a compromised cloud account to maintain persistence in the environment. Such credentials may also be used to bypass security controls such as multi-factor authentication. 

Cloud accounts may also be able to assume [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]] or other privileges through various means within the environment. Misconfigurations in role assignments or role assumption policies may allow an adversary to use these mechanisms to leverage permissions outside the intended scope of the account. Such over privileged accounts may be used to harvest sensitive data from online storage accounts and databases through [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]] or other methods. For example, in Azure environments, adversaries may target Azure Managed Identities, which allow associated Azure resources to request access tokens. By compromising a resource with an attached Managed Identity, such as an Azure VM, adversaries may be able to [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]s to move laterally across the cloud environment.(Citation: SpecterOps Managed Identity 2022)

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1036-account_use_policies|M1036: Account Use Policies]]

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

