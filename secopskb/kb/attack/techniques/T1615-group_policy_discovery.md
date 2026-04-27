---
mitre_id: "T1615"
mitre_name: "Group Policy Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1b20efbf-8063-4fc3-a07d-b575318a301b"
mitre_created: "2021-08-06T13:10:12.916Z"
mitre_modified: "2025-10-24T17:48:28.148Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1615/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-AM"
  - "D3-CI"
  - "D3-NTPM"
  - "D3-RC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path `\<DOMAIN>\SYSVOL\<DOMAIN>\Policies\`.(Citation: TechNet Group Policy Basics)(Citation: ADSecurity GPO Persistence 2016)

Adversaries may use commands such as `gpresult` or various publicly available PowerShell functions, such as `Get-DomainGPO` and `Get-DomainGPOLocalGroup`, to gather information on Group Policy settings.(Citation: Microsoft gpresult)(Citation: Github PowerShell Empire) Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. [[T1484-domain_or_tenant_policy_modification|T1484: Domain or Tenant Policy Modification]]) for their benefit.

## Workspace

- [[workspaces/attack/techniques/T1615-group_policy_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1615-group_policy_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/07aa184a_870d_413d_893a_157f317f6f58-suspicious_reconnaissance_activity_via_gathernetworkinfo_vbs|Suspicious Reconnaissance Activity Via GatherNetworkInfo.VBS (high; windows / process_creation)]]
- [[kb/sigma/rules/c484e533_ee16_4a93_b6ac_f0ea4868b2f1-hacktool_sharpup_privesc_tool_execution|HackTool - SharpUp PrivEsc Tool Execution (critical; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/0976990f_53b1_4d3f_a185_6df5be429d3b-display_group_policy_information_via_gpresult|Display group policy information via gpresult (command_prompt; windows)]]
- [[kb/atomic/tests/4e524c4e_0e02_49aa_8df5_93f3f7959b9f-get_domaingpo_to_display_group_policy_information_via_powerview|Get-DomainGPO to display group policy information via PowerView (powershell; windows)]]
- [[kb/atomic/tests/52778a8f_a10b_41a4_9eae_52ddb74072bf-msft_get_gpo_cmdlet|MSFT Get-GPO Cmdlet (powershell; windows)]]
- [[kb/atomic/tests/7230d01a_0a72_4bd5_9d7f_c6d472bc6a59-winpwn_gporemoteaccesspolicy|WinPwn - GPORemoteAccessPolicy (powershell; windows)]]
- [[kb/atomic/tests/bc25c04b_841e_4965_855f_d1f645d7ab73-winpwn_gpoaudit|WinPwn - GPOAudit (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CI-configuration_inventory|D3-CI: Configuration Inventory]]
- [[D3-NTPM-network_traffic_policy_mapping|D3-NTPM: Network Traffic Policy Mapping]]
- [[D3-RC-restore_configuration|D3-RC: Restore Configuration]]

## Tools
- [[bloodhound|BloodHound (S0521)]]
- [[empire|Empire (S0363)]]


## Platforms

- Windows

