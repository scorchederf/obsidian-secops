---
mitre_id: "T1136"
mitre_name: "Create Account"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e01be9c5-e763-4caf-aeb7-000b416aef67"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:49:30.136Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1136/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Containers"
  - "SaaS"
  - "Office Suite"
  - "Identity Provider"
  - "ESXi"
mitre_tactic_ids:
  - "TA0003"
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

Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June 2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

## Workspace

- [[workspaces/attack/techniques/T1136-create_account-note|Open workspace note]]

![[workspaces/attack/techniques/T1136-create_account-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

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

### T1136.001: Local Account

^t1136001-local-account

Adversaries may create a local account to maintain access to victim systems. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service. 

For example, with a sufficient level of access, the Windows `net user /add` command can be used to create a local account.  In Linux, the `useradd` command can be used, while on macOS systems, the `dscl -create` command can be used. Local accounts may also be added to network devices, often via common [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `username`, to ESXi servers via `esxcli system account add`, or to Kubernetes clusters using the `kubectl` utility.(Citation: cisco_username_cmd)(Citation: Kubernetes Service Accounts Security)

Adversaries may also create new local accounts on network firewall management consoles – for example, by exploiting a vulnerable firewall management system, threat actors may be able to establish super-admin accounts that could be used to modify firewall rules and gain further access to the network.(Citation: Cyber Security News)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

### T1136.002: Domain Account

^t1136002-domain-account

Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover user, administrator, and service accounts. With a sufficient level of access, the `net user /add /domain` command can be used to create a domain account.(Citation: Savill 1999)

Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

### T1136.003: Cloud Account

^t1136003-cloud-account

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles)(Citation: Microsoft Support O365 Add Another Admin, October 2019)(Citation: AWS Create IAM User)(Citation: GCP Create Cloud Identity Users)(Citation: Microsoft Azure AD Users)

In addition to user accounts, cloud accounts may be associated with services. Cloud providers handle the concept of service accounts in different ways. In Azure, service accounts include service principals and managed identities, which can be linked to various resources such as OAuth applications, serverless functions, and virtual machines in order to grant those resources permissions to perform various activities in the environment.(Citation: Microsoft Entra ID Service Principals) In GCP, service accounts can also be linked to specific resources, as well as be impersonated by other accounts for [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]].(Citation: GCP Service Accounts) While AWS has no specific concept of service accounts, resources can be directly granted permission to assume roles.(Citation: AWS Instance Profiles)(Citation: AWS Lambda Execution Role)

Adversaries may create accounts that only have access to specific cloud services, which can reduce the chance of detection.

Once an adversary has created a cloud account, they can then manipulate that account to ensure persistence and allow access to additional resources - for example, by adding [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]] or assigning [[T1098-account_manipulation#^t1098003-additional-cloud-roles|T1098.003: Additional Cloud Roles]].

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

