---
mitre_id: "T1087"
mitre_name: "Account Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--72b74d71-8169-42aa-92e0-e7b04b9f5a08"
mitre_created: "2017-05-31T21:31:06.988Z"
mitre_modified: "2025-10-24T17:48:57.239Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1087/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [[T1078-valid_accounts|T1078: Valid Accounts]]).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List Users)(Citation: Google Cloud - IAM Servie Accounts List API) On hosts, adversaries can use default [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Workspace

- [[workspaces/attack/techniques/T1087-account_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1087-account_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]

### Sigma Rules

- [[kb/sigma/rules/02030f2f_6199_49ec_b258_ea71b07e03dc-malicious_powershell_commandlets_processcreation|Malicious PowerShell Commandlets - ProcessCreation (high; windows / process_creation)]]
- [[kb/sigma/rules/02773bed_83bf_469f_b7ff_e676e7d78bab-bloodhound_collection_files|BloodHound Collection Files (high; windows / file_event)]]
- [[kb/sigma/rules/24549159_ac1b_479c_8175_d42aea947cae-hacktool_ruler|Hacktool Ruler (high; windows / security)]]
- [[kb/sigma/rules/35b781cc_1a08_4a5a_80af_42fd7c315c6b-discovery_using_azurehound|Discovery Using AzureHound (high; azure / signinlogs)]]
- [[kb/sigma/rules/35ba1d85_724d_42a3_889f_2e2362bcaf23-ad_privileged_users_or_groups_reconnaissance|AD Privileged Users or Groups Reconnaissance (high; windows / security)]]
- [[kb/sigma/rules/38646daa_e78f_4ace_9de0_55547b2d30da-pua_seatbelt_execution|PUA - Seatbelt Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/455b9d50_15a1_4b99_853f_8d37655a4c1b-pua_suspicious_activedirectory_enumeration_via_adfind_exe|PUA - Suspicious ActiveDirectory Enumeration Via AdFind.EXE (high; windows / process_creation)]]
- [[kb/sigma/rules/4ebc877f_4612_45cb_b3a5_8e3834db36c9-webshell_hacking_activity_patterns|Webshell Hacking Activity Patterns (high; windows / process_creation)]]
- [[kb/sigma/rules/65f77b1e_8e79_45bf_bb67_5988a8ce45a5-sharphound_recon_account_discovery|SharpHound Recon Account Discovery (high; rpc_firewall / application)]]
- [[kb/sigma/rules/7d0d0329_0ef1_4e84_a9f5_49500f9d7c6c-malicious_powershell_commandlets_poshmodule|Malicious PowerShell Commandlets - PoshModule (high; windows / ps_module)]]
- 11 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/00c652e2_0750_4ca6_82ff_0204684a6fe4-enumerate_root_domain_linked_policies_discovery|Enumerate Root Domain linked policies Discovery (powershell; windows)]]
- [[kb/atomic/tests/02e8be5a_3065_4e54_8cc8_a14d138834d3-enumerate_active_directory_users_with_adsisearcher|Enumerate Active Directory Users with ADSISearcher (powershell; windows)]]
- [[kb/atomic/tests/096b6d2a_b63f_4100_8fa0_525da4cd25ca-active_directory_domain_search|Active Directory Domain Search (sh; linux)]]
- [[kb/atomic/tests/0f0b6a29_08c3_44ad_a30b_47fd996b2110-show_if_a_user_account_has_ever_logged_in_remotely|Show if a user account has ever logged in remotely (sh; linux)]]
- [[kb/atomic/tests/161dcd85_d014_4f5e_900c_d3eaae82a0f7-enumerate_logged_on_users_via_cmd_domain|Enumerate logged on users via CMD (Domain) (command_prompt; windows)]]
- [[kb/atomic/tests/319e9f6c_7a9e_432e_8c62_9385c803b6f2-enumerate_users_and_groups|Enumerate users and groups (sh; macos)]]
- [[kb/atomic/tests/394012d9_2164_4d4f_b9e5_acf30ba933fe-suspicious_laps_attributes_query_with_get_adcomputer_all_properties|Suspicious LAPS Attributes Query with Get-ADComputer all properties (powershell; windows)]]
- [[kb/atomic/tests/46f8dbe9_22a5_4770_8513_66119c5be63b-enumerate_active_directory_for_unconstrained_delegation|Enumerate Active Directory for Unconstrained Delegation (powershell; windows)]]
- [[kb/atomic/tests/51a98f96_0269_4e09_a10f_e307779a8b05-suspicious_laps_attributes_query_with_adfind_ms_mcs_admpwd|Suspicious LAPS Attributes Query with adfind ms-Mcs-AdmPwd (powershell; windows)]]
- [[kb/atomic/tests/5e2938fb_f919_47b6_8b29_2f6a1f718e99-adfind_enumerate_active_directory_exchange_ad_objects|Adfind - Enumerate Active Directory Exchange AD Objects (command_prompt; windows)]]
- 25 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

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

### T1087.001: Local Account

^t1087001-local-account

Adversaries may attempt to get a listing of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior.

Commands such as `net user` and `net localgroup` of the [[net|Net (S0039)]] utility and `id` and `groups` on macOS and Linux can list local users and groups.(Citation: Mandiant APT1)(Citation: id man page)(Citation: groups man page) On Linux, local users can also be enumerated through the use of the `/etc/passwd` file. On macOS, the `dscl . list /Users` command can be used to enumerate local accounts. On ESXi servers, the `esxcli system account list` command can list local user accounts.(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

### T1087.002: Domain Account

^t1087002-domain-account

Adversaries may attempt to get a listing of domain accounts. This information can help adversaries determine which domain accounts exist to aid in follow-on behavior such as targeting specific accounts which possess particular privileges.

Commands such as `net user /domain` and `net group /domain` of the [[net|Net (S0039)]] utility, `dscacheutil -q group` on macOS, and `ldapsearch` on Linux can list domain users and groups. [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] cmdlets including `Get-ADUser` and `Get-ADGroupMember` may enumerate members of Active Directory groups.(Citation: CrowdStrike StellarParticle January 2022)  

### T1087.003: Email Account

^t1087003-email-account

Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)

In on-premises Exchange and Exchange Online, the `Get-GlobalAddressList` PowerShell cmdlet can be used to obtain email addresses and accounts from a domain using an authenticated session.(Citation: Microsoft getglobaladdresslist)(Citation: Black Hills Attacking Exchange MailSniper, 2016)

In Google Workspace, the GAL is shared with Microsoft Outlook users through the Google Workspace Sync for Microsoft Outlook (GWSMO) service. Additionally, the Google Workspace Directory allows for users to get a listing of other users within the organization.(Citation: Google Workspace Global Access List)

### T1087.004: Cloud Account

^t1087004-cloud-account

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application.

With authenticated access there are several tools that can be used to find accounts. The `Get-MsolRoleMember` PowerShell cmdlet can be used to obtain account names given a role or permissions group in Office 365.(Citation: Microsoft msolrolemember)(Citation: GitHub Raindance) The Azure CLI (AZ CLI) also provides an interface to obtain user accounts with authenticated access to a domain. The command `az ad user list` will list all users within a domain.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018) 

The AWS command `aws iam list-users` may be used to obtain a list of users in the current account while `aws iam list-roles` can obtain IAM roles that have a specified path prefix.(Citation: AWS List Roles)(Citation: AWS List Users) In GCP, `gcloud iam service-accounts list` and `gcloud projects get-iam-policy` may be used to obtain a listing of service accounts and users in a project.(Citation: Google Cloud - IAM Servie Accounts List API)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]

## Tools

- [[shimratreporter|ShimRatReporter (S0445)]]

## Platforms

- ESXi
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

