---
mitre_id: "T1046"
mitre_name: "Network Service Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e3a12395-188d-4051-9a16-ea8e14d07b88"
mitre_created: "2017-05-31T21:30:43.915Z"
mitre_modified: "2025-10-24T17:49:31.494Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1046/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
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

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as `dns-sd -B _ssh._tcp .`) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Workspace

- [[workspaces/attack/techniques/T1046-network_service_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1046-network_service_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-04-002-quick_execution_of_a_series_of_suspicious_commands|CAR-2013-04-002: Quick execution of a series of suspicious commands]]
- [[kb/car/analytics/CAR-2021-01-001-identifying_port_scanning_activity|CAR-2021-01-001: Identifying Port Scanning Activity]]

### Sigma Rules

- [[kb/sigma/rules/68b8547b_107f_43f3_97fb_900a7d63c190-opencanary_nmap_null_scan|OpenCanary - NMAP NULL Scan (high; opencanary / application)]]
- [[kb/sigma/rules/851fd622_b675_4d26_b803_14bc7baa517a-hacktool_winpwn_execution_scriptblock|HackTool - WinPwn Execution - ScriptBlock (high; windows / ps_script)]]
- [[kb/sigma/rules/974be8d2_283e_4033_ab08_7505b84204d0-opencanary_host_port_scan_syn_scan|OpenCanary - Host Port Scan (SYN Scan) (high; opencanary / application)]]
- [[kb/sigma/rules/98b53e78_ebaf_46f8_be06_421aafd176d9-hacktool_winpeas_execution|HackTool - winPEAS Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/d557dc06_62e8_4468_a8e8_7984124908ce-hacktool_winpwn_execution|HackTool - WinPwn Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/d7553d7b_f485_479c_b192_cdac6edd83a4-opencanary_nmap_xmas_scan|OpenCanary - NMAP XMAS Scan (high; opencanary / application)]]
- [[kb/sigma/rules/e8a677fd_248c_4eab_94df_de2f6f645884-opencanary_nmap_os_scan|OpenCanary - NMAP OS Scan (high; opencanary / application)]]
- [[kb/sigma/rules/eae8c0c8_e5da_450a_9d7d_66aa56cd26b6-opencanary_nmap_fin_scan|OpenCanary - NMAP FIN Scan (high; opencanary / application)]]

### Atomic Tests

- [[kb/atomic/tests/05df2a79_dba6_4088_a804_9ca0802ca8e4-port_scanning_24_subnet_with_powershell|Port-Scanning /24 Subnet with PowerShell (powershell; windows)]]
- [[kb/atomic/tests/06eaafdb_8982_426e_8a31_d572da633caa-network_service_discovery_for_containers|Network Service Discovery for Containers (sh; containers)]]
- [[kb/atomic/tests/0d5a2b03_3a26_45e4_96ae_89485b4d1f97-port_scan_using_nmap_port_range|Port Scan using nmap (Port range) (sh; linux, macos)]]
- [[kb/atomic/tests/1cca5640_32a9_46e6_b8e0_fabbe2384a73-winpwn_bluekeep|WinPwn - bluekeep (powershell; windows)]]
- [[kb/atomic/tests/515942b0_a09f_4163_a7bb_22fefb6f185f-port_scan_nmap|Port Scan Nmap (sh; linux, macos)]]
- [[kb/atomic/tests/54574908_f1de_4356_9021_8053dd57439a-winpwn_spoolvulnscan|WinPwn - spoolvulnscan (powershell; windows)]]
- [[kb/atomic/tests/68e907da_2539_48f6_9fc9_257a78c05540-port_scan|Port Scan (bash; linux, macos)]]
- [[kb/atomic/tests/6ca45b04_9f15_4424_b9d3_84a217285a5c-port_scan_using_python|Port Scan using python (powershell; windows)]]
- [[kb/atomic/tests/97585b04_5be2_40e9_8c31_82157b8af2d6-winpwn_ms17_10|WinPwn - MS17-10 (powershell; windows)]]
- [[kb/atomic/tests/9e55750e_4cbf_4013_9627_e9a045b541bf-remote_desktop_services_discovery_via_powershell|Remote Desktop Services Discovery via PowerShell (powershell; windows)]]
- 2 more in the generated source index

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Tools
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[empire|Empire (S0363)]]
- [[frp|FRP (S1144)]]
- [[koadic|Koadic (S0250)]]
- [[nbtscan|NBTscan (S0590)]]
- [[peirates|Peirates (S0683)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Containers
- IaaS
- Linux
- macOS
- Network Devices
- Windows

