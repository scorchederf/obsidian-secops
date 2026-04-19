---
id: T1136
name: Create Account
created: 2017-12-14 16:46:06.044000+00:00
modified: 2025-10-24 17:49:30.136000+00:00
type: attack-pattern
x_mitre_version: 2.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June 2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

## Subtechniques

### T1136.001: Local Account

^t1136001-local-account

**Parent Technique**
- [[T1136-create_account|T1136: Create Account]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. 

For example, with a sufficient level of access, the Windows <code>net user /add</code> command can be used to create a local account.  In Linux, the `useradd` command can be used, while on macOS systems, the <code>dscl -create</code> command can be used. Local accounts may also be added to network devices, often via common [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) commands such as <code>username</code>, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility.(Citation: cisco_username_cmd)(Citation: Kubernetes Service Accounts Security)

Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network.(Citation: Cyber Security News)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

### T1136.002: Domain Account

^t1136002-domain-account

**Parent Technique**
- [[T1136-create_account|T1136: Create Account]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover user, administrator, and service accounts. With a sufficient level of access, the <code>net user /add /domain</code> command can be used to create a domain account.(Citation: Savill 1999)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

### T1136.003: Cloud Account

^t1136003-cloud-account

**Parent Technique**
- [[T1136-create_account|T1136: Create Account]]

**Tactic**
- [[persistence|Persistence]]

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: AWS Create IAM User)(Citation: GCP Create Cloud Identity Users)(Citation: Microsoft Azure AD Users)

In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources permissions to perform various activities in the environment.(Citation: Microsoft Entra ID Service Principals) In GCP, service accounts can also be linked to specific resources, as well as be impersonated by other accounts for [Temporary Elevated Cloud Access](https://attack.mitre.org/techniques/T1548/005).(Citation: GCP Service Accounts) While AWS has no specific concept of service accounts, resources can be directly granted permission to assume roles.(Citation: AWS Instance Profiles)(Citation: AWS Lambda Execution Role)

Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection.

Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access to additional resources - for example, by adding [Additional Cloud Credentials](https://attack.mitre.org/techniques/T1098/001) or assigning [Additional Cloud Roles](https://attack.mitre.org/techniques/T1098/003).

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]

## Platforms

- Windows
- IaaS
- Linux
- macOS
- Network Devices
- Containers
- SaaS
- Office Suite
- Identity Provider
- ESXi

