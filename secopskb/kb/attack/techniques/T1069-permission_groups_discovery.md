---
mitre_id: "T1069"
mitre_name: "Permission Groups Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--15dbf668-795c-41e6-8219-f0447c0e64ce"
mitre_created: "2017-05-31T21:30:55.471Z"
mitre_modified: "2025-10-24T17:48:26.378Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1069/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "IaaS"
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Office Suite"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting.(Citation: CrowdStrike BloodHound April 2018)

## Workspace

- [[workspaces/attack/techniques/T1069-permission_groups_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1069-permission_groups_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2016-03-001-host_discovery_commands|CAR-2016-03-001: Host Discovery Commands]]
- [[kb/car/analytics/CAR-2020-11-006-local_permission_group_discovery|CAR-2020-11-006: Local Permission Group Discovery]]

### Sigma Rules

- [[kb/sigma/rules/02030f2f_6199_49ec_b258_ea71b07e03dc-malicious_powershell_commandlets_processcreation|Malicious PowerShell Commandlets - ProcessCreation (high; windows / process_creation)]]
- [[kb/sigma/rules/02773bed_83bf_469f_b7ff_e676e7d78bab-bloodhound_collection_files|BloodHound Collection Files (high; windows / file_event)]]
- [[kb/sigma/rules/7d0d0329_0ef1_4e84_a9f5_49500f9d7c6c-malicious_powershell_commandlets_poshmodule|Malicious PowerShell Commandlets - PoshModule (high; windows / ps_module)]]
- [[kb/sigma/rules/89819aa4_bbd6_46bc_88ec_c7f7fe30efa6-malicious_powershell_commandlets_scriptblock|Malicious PowerShell Commandlets - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/968eef52_9cff_4454_8992_1e74b9cbad6c-reconnaissance_activity|Reconnaissance Activity (high; windows / security)]]
- [[kb/sigma/rules/9a132afa_654e_11eb_ae93_0242ac130002-pua_adfind_suspicious_execution|PUA - AdFind Suspicious Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/b2317cfa_4a47_4ead_b3ff_297438c0bc2d-hacktool_sharpview_execution|HackTool - SharpView Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/df55196f_f105_44d3_a675_e9dfb6cc2f2b-renamed_adfind_execution|Renamed AdFind Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/ef61af62_bc74_4f58_b49b_626448227652-suspicious_active_directory_database_snapshot_via_adexplorer|Suspicious Active Directory Database Snapshot Via ADExplorer (high; windows / process_creation)]]
- [[kb/sigma/rules/f376c8a7_a2d0_4ddc_aa0c_16c17236d962-hacktool_bloodhound_sharphound_execution|HackTool - Bloodhound/Sharphound Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/007d7aa4_8c4d_4f55_ba6a_7c965d51219c-permission_groups_discovery_for_containers_local_groups|Permission Groups Discovery for Containers- Local Groups (sh; containers)]]
- [[kb/atomic/tests/0afb5163_8181_432e_9405_4322710c0c37-elevated_group_enumeration_using_net_group_domain|Elevated group enumeration using net group (Domain) (command_prompt; windows)]]
- [[kb/atomic/tests/1f454dd6_e134_44df_bebb_67de70fb6cd8-basic_permission_groups_discovery_windows_local|Basic Permission Groups Discovery Windows (Local) (command_prompt; windows)]]
- [[kb/atomic/tests/22cf8cb9_adb1_4e8c_80ca_7c723dfc8784-active_directory_enumeration_with_ldifde|Active Directory Enumeration with LDIFDE (command_prompt; windows)]]
- [[kb/atomic/tests/3d1fcd2a_e51c_4cbe_8d84_9a843bad8dc8-enumerate_active_directory_groups_with_get_adgroup|Enumerate Active Directory Groups with Get-AdGroup (powershell; windows)]]
- [[kb/atomic/tests/43fa81fb_34bb_4b5f_867b_03c7dbe0e3d8-get_aduser_enumeration_using_useraccountcontrol_flags_as_rep_roasting|Get-ADUser Enumeration using UserAccountControl flags (AS-REP Roasting) (powershell; windows)]]
- [[kb/atomic/tests/46352f40_f283_4fe5_b56d_d9a71750e145-get_domaingroupmember_with_powerview|Get-DomainGroupMember with PowerView (powershell; windows)]]
- [[kb/atomic/tests/48ddc687_82af_40b7_8472_ff1e742e8274-adfind_query_active_directory_groups|Adfind - Query Active Directory Groups (command_prompt; windows)]]
- [[kb/atomic/tests/5a8a181c_2c8e_478d_a943_549305a01230-get_domaingroup_with_powerview|Get-DomainGroup with PowerView (powershell; windows)]]
- [[kb/atomic/tests/64fdb43b_5259_467a_b000_1b02c00e510a-find_local_admins_via_group_policy_powerview|Find Local Admins via Group Policy (PowerView) (powershell; windows)]]
- 12 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Subtechniques

### T1069.001: Local Groups

^t1069001-local-groups

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

Commands such as `net localgroup` of the [[net|Net (S0039)]] utility, `dscl . -list /Groups` on macOS, and `groups` on Linux can list local groups.

### T1069.002: Domain Groups

^t1069002-domain-groups

Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as domain administrators.

Commands such as `net group /domain` of the [[net|Net (S0039)]] utility,  `dscacheutil -q group` on macOS, and `ldapsearch` on Linux can list domain-level groups.

### T1069.003: Cloud Groups

^t1069003-cloud-groups

Adversaries may attempt to find cloud groups and permission settings. The knowledge of cloud permission groups can help adversaries determine the particular roles of users and groups within an environment, as well as which users are associated with a particular group.

With authenticated access there are several tools that can be used to find permissions groups. The `Get-MsolRole` PowerShell cmdlet can be used to obtain roles and permissions groups for Exchange and Office 365 accounts (Citation: Microsoft Msolrole)(Citation: GitHub Raindance).

Azure CLI (AZ CLI) and the Google Cloud Identity Provider API also provide interfaces to obtain permissions groups. The command `az ad user get-member-groups` will list groups associated to a user account for Azure while the API endpoint `GET https://cloudidentity.googleapis.com/v1/groups` lists group resources available to a user for Google.(Citation: Microsoft AZ CLI)(Citation: Black Hills Red Teaming MS AD Azure, 2018)(Citation: Google Cloud Identity API Documentation) In AWS, the commands `ListRolePolicies` and `ListAttachedRolePolicies` allow users to enumerate the policies attached to a role.(Citation: Palo Alto Unit 42 Compromised Cloud Compute Credentials 2022)

Adversaries may attempt to list ACLs for objects to determine the owner and other accounts with access to the object, for example, via the AWS `GetBucketAcl` API (Citation: AWS Get Bucket ACL). Using this information an adversary can target accounts with permissions to a given object or leverage accounts they have already compromised to access the object.

## Tools

- [[shimratreporter|ShimRatReporter (S0445)]]

## Platforms

- Containers
- IaaS
- Identity Provider
- Linux
- macOS
- Office Suite
- SaaS
- Windows

