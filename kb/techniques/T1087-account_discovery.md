---
id: T1087
name: Account Discovery
created: 2017-05-31 21:31:06.988000+00:00
modified: 2025-10-24 17:48:57.239000+00:00
type: attack-pattern
x_mitre_version: 2.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List Users)(Citation: Google Cloud - IAM Servie Accounts List API) On hosts, adversaries can use default [PowerShell](https://attack.mitre.org/techniques/T1059/001) and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Subtechniques

### T1087.001: Local Account
^t1087001-local-account

**Parent Technique**
- [[T1087-account_discovery|T1087: Account Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to get a listing of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior.

Commands such as <code>net user</code> and <code>net localgroup</code> of the [Net](https://attack.mitre.org/software/S0039) utility and <code>id</code> and <code>groups</code> on macOS and Linux can list local users and groups.(Citation: Mandiant APT1)(Citation: id man page)(Citation: groups man page) On Linux, local users can also be enumerated through the use of the <code>/etc/passwd</code> file. On macOS, the <code>dscl . list /Users</code> command can be used to enumerate local accounts. On ESXi servers, the `esxcli system account list` command can list local user accounts.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

#### Properties

- id: T1087.001
- name: Local Account
- created: 2020-02-21 21:07:55.393000+00:00
- modified: 2025-10-24 17:48:32.515000+00:00
- type: attack-pattern
- x_mitre_version: 1.5
- x_mitre_domains: enterprise-attack

### T1087.002: Domain Account
^t1087002-domain-account

**Parent Technique**
- [[T1087-account_discovery|T1087: Account Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to get a listing of domain accounts. This information can help adversaries determine which domain accounts exist to aid in follow-on behavior such as targeting specific accounts which possess particular privileges.

Commands such as <code>net user /domain</code> and <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility, <code>dscacheutil -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain users and groups. [PowerShell](https://attack.mitre.org/techniques/T1059/001) cmdlets including <code>Get-ADUser</code> and <code>Get-ADGroupMember</code> may enumerate members of Active Directory groups.(Citation: CrowdStrike StellarParticle January 2022)  

#### Properties

- id: T1087.002
- name: Domain Account
- created: 2020-02-21 21:08:26.480000+00:00
- modified: 2025-10-24 17:48:31.050000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1087.003: Email Account
^t1087003-email-account

**Parent Technique**
- [[T1087-account_discovery|T1087: Account Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)

In on-premises Exchange and Exchange Online, the <code>Get-GlobalAddressList</code> PowerShell cmdlet can be used to obtain email addresses and accounts from a domain using an authenticated session.(Citation: Microsoft getglobaladdresslist)(Citation: Black Hills Attacking Exchange MailSniper, 2016)

In Google Workspace, the GAL is shared with Microsoft Outlook users through the Google Workspace Sync for Microsoft Outlook (GWSMO) service. Additionally, the Google Workspace Directory allows for users to get a listing of other users within the organization.(Citation: Google Workspace Global Access List)

#### Properties

- id: T1087.003
- name: Email Account
- created: 2020-02-21 21:08:33.237000+00:00
- modified: 2025-10-24 17:48:44.685000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1087.004: Cloud Account
^t1087004-cloud-account

**Parent Technique**
- [[T1087-account_discovery|T1087: Account Discovery]]

**Tactic**
- [[discovery|Discovery]]

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application.

With authenticated access there are several tools that can be used to find accounts. The <code>Get-MsolRoleMember</code> PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365.(Citation: Microsoft msolrolemember)(Citation: GitHub Raindance) The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command <code>az ad user list</code> will list all users within a domain.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018) 

The AWS command <code>aws iam list-users</code> may be used to obtain a list of users in the current account while <code>aws iam list-roles</code> can obtain IAM roles that have a specified path prefix.(Citation: AWS List Roles)(Citation: AWS List Users) In GCP, <code>gcloud iam service-accounts list</code> and <code>gcloud projects get-iam-policy</code> may be used to obtain a listing of service accounts and users in a project.(Citation: Google Cloud - IAM Servie Accounts List API)

#### Properties

- id: T1087.004
- name: Cloud Account
- created: 2020-02-21 21:08:36.570000+00:00
- modified: 2025-10-24 17:49:05.745000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]

## Platforms

- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

## Tools

- [[shimratreporter|ShimRatReporter]]

