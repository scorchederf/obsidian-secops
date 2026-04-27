---
mitre_id: "T1482"
mitre_name: "Domain Trust Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--767dbf9e-df3f-45cb-8998-4903ab5f80c0"
mitre_created: "2019-02-14T16:15:05.974Z"
mitre_modified: "2025-10-24T17:48:58.061Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1482/"
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
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain.(Citation: Microsoft Trusts) Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct [[T1134-access_token_manipulation#^t1134005-sid-history-injection|T1134.005: SID-History Injection]], [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]], and [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]].(Citation: AdSecurity Forging Trust Tickets)(Citation: Harmj0y Domain Trusts) Domain trusts can be enumerated using the `DSEnumerateDomainTrusts()` Win32 API call, .NET methods, and LDAP.(Citation: Harmj0y Domain Trusts) The Windows utility [[nltest|Nltest (S0359)]] is known to be used by adversaries to enumerate domain trusts.(Citation: Microsoft Operation Wilysupply)

## Workspace

- [[workspaces/attack/techniques/T1482-domain_trust_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1482-domain_trust_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/02030f2f_6199_49ec_b258_ea71b07e03dc-malicious_powershell_commandlets_processcreation|Malicious PowerShell Commandlets - ProcessCreation (high; windows / process_creation)]]
- [[kb/sigma/rules/02773bed_83bf_469f_b7ff_e676e7d78bab-bloodhound_collection_files|BloodHound Collection Files (high; windows / file_event)]]
- [[kb/sigma/rules/69ca006d_b9a9_47f5_80ff_ecd4d25d481a-hacktool_trufflesnout_execution|HackTool - TruffleSnout Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/7d0d0329_0ef1_4e84_a9f5_49500f9d7c6c-malicious_powershell_commandlets_poshmodule|Malicious PowerShell Commandlets - PoshModule (high; windows / ps_module)]]
- [[kb/sigma/rules/89819aa4_bbd6_46bc_88ec_c7f7fe30efa6-malicious_powershell_commandlets_scriptblock|Malicious PowerShell Commandlets - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/9a132afa_654e_11eb_ae93_0242ac130002-pua_adfind_suspicious_execution|PUA - AdFind Suspicious Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/b2317cfa_4a47_4ead_b3ff_297438c0bc2d-hacktool_sharpview_execution|HackTool - SharpView Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/df55196f_f105_44d3_a675_e9dfb6cc2f2b-renamed_adfind_execution|Renamed AdFind Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/ef61af62_bc74_4f58_b49b_626448227652-suspicious_active_directory_database_snapshot_via_adexplorer|Suspicious Active Directory Database Snapshot Via ADExplorer (high; windows / process_creation)]]
- [[kb/sigma/rules/f376c8a7_a2d0_4ddc_aa0c_16c17236d962-hacktool_bloodhound_sharphound_execution|HackTool - Bloodhound/Sharphound Execution (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/15fe436d_e771_4ff3_b655_2dca9ba52834-adfind_enumerate_active_directory_trusts|Adfind - Enumerate Active Directory Trusts (command_prompt; windows)]]
- [[kb/atomic/tests/2e22641d_0498_48d2_b9ff_c71e496ccdbe-windows_discover_domain_trusts_with_nltest|Windows - Discover domain trusts with nltest (command_prompt; windows)]]
- [[kb/atomic/tests/4700a710_c821_4e17_a3ec_9e4c81d6845f-windows_discover_domain_trusts_with_dsquery|Windows - Discover domain trusts with dsquery (command_prompt; windows)]]
- [[kb/atomic/tests/58ed10e8_0738_4651_8408_3a3e9a526279-get_foresttrust_with_powerview|Get-ForestTrust with PowerView (powershell; windows)]]
- [[kb/atomic/tests/c58fbc62_8a62_489e_8f2d_3565d7d96f30-powershell_enumerate_domains_and_forests|Powershell enumerate domains and forests (powershell; windows)]]
- [[kb/atomic/tests/d1c73b96_ab87_4031_bad8_0e1b3b8bf3ec-adfind_enumerate_active_directory_ous|Adfind - Enumerate Active Directory OUs (command_prompt; windows)]]
- [[kb/atomic/tests/ea1b4f2d_5b82_4006_b64f_f2845608a3bf-trufflesnout_listing_ad_infrastructure|TruffleSnout - Listing AD Infrastructure (command_prompt; windows)]]
- [[kb/atomic/tests/f974894c_5991_4b19_aaf5_7cc2fe298c5d-get_domaintrust_with_powerview|Get-DomainTrust with PowerView (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1047-audit|M1047: Audit]]

## Tools
- [[adfind|AdFind (S0552)]]
- [[bloodhound|BloodHound (S0521)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[dsquery|dsquery (S0105)]]
- [[empire|Empire (S0363)]]
- [[nltest|Nltest (S0359)]]
- [[poshc2|PoshC2 (S0378)]]
- [[powersploit|PowerSploit (S0194)]]
- [[rubeus|Rubeus (S1071)]]


## Platforms

- Windows

