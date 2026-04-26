---
mitre_id: "T1133"
mitre_name: "External Remote Services"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--10d51417-ee35-4589-b1ff-b6df1c334e8d"
mitre_created: "2017-05-31T21:31:44.421Z"
mitre_modified: "2025-10-24T17:48:24.982Z"
mitre_version: "2.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1133/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0003"
  - "TA0001"
d3fend_ids:
  - "D3-ST"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]] and [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]] can also be used externally.(Citation: MacOS VNC software for Remote Desktop)

Access to [[T1078-valid_accounts|T1078: Valid Accounts]] to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.(Citation: Volexity Virtual Private Keylogging) Access to remote services may be used as a redundant or persistent access mechanism during an operation.

Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.(Citation: Trend Micro Exposed Docker Server)(Citation: Unit 42 Hildegard Malware)

Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access.(Citation: The BadPilot campaign) Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.(Citation: Russian threat actors dig in, prepare to seize on war fatigue)

## Workspace

- [[workspaces/attack/techniques/T1133-external_remote_services-note|Open workspace note]]

![[workspaces/attack/techniques/T1133-external_remote_services-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/512cff7a_683a_43ad_afe0_dd398e872f36-opencanary_telnet_login_attempt|OpenCanary - Telnet Login Attempt (high; opencanary / application)]]
- [[kb/sigma/rules/598290cf_5932_45cd_9123_be1e05ab4f2e-opencanary_rdp_new_connection_attempt|OpenCanary - RDP New Connection Attempt (high; opencanary / application)]]
- [[kb/sigma/rules/78d5cab4_557e_454f_9fb9_a222bd0d5edc-external_remote_smb_logon_from_public_ip|External Remote SMB Logon from Public IP (high; windows / security)]]
- [[kb/sigma/rules/8f0b1fb1_9bd4_4e74_8cdf_a8de4d2adfd0-unusual_file_deletion_by_dns_exe|Unusual File Deletion by Dns.exe (high; windows / file_delete)]]
- [[kb/sigma/rules/9f383dc0_fdeb_4d56_acbc_9f9f4f8f20f3-unusual_file_modification_by_dns_exe|Unusual File Modification by dns.exe (high; windows / file_change)]]
- [[kb/sigma/rules/a4e3d776_f12e_42c2_8510_9e6ed1f43ec3-unusual_child_process_of_dns_exe|Unusual Child Process of dns.exe (high; windows / process_creation)]]
- [[kb/sigma/rules/b64a026b_8deb_4c1d_92fd_98893209dff1-running_chrome_vpn_extensions_via_the_registry_2_vpn_extension|Running Chrome VPN Extensions via the Registry 2 VPN Extension (high; windows / registry_set)]]
- [[kb/sigma/rules/cd55f721_5623_4663_bd9b_5229cab5237d-opencanary_ssh_new_connection_attempt|OpenCanary - SSH New Connection Attempt (high; opencanary / application)]]
- [[kb/sigma/rules/e890acee_d488_420e_8f20_d9b19b3c3d43-suspicious_file_created_by_arcsoc_exe|Suspicious File Created by ArcSOC.exe (high; windows / file_event)]]
- [[kb/sigma/rules/ff7139bc_fdb1_4437_92f2_6afefe8884cb-opencanary_ssh_login_attempt|OpenCanary - SSH Login Attempt (high; opencanary / application)]]
- 1 more in the generated source index

### Atomic Tests

- [[kb/atomic/tests/4c8db261_a58b_42a6_a866_0a294deedde4-running_chrome_vpn_extensions_via_the_registry_2_vpn_extension|Running Chrome VPN Extensions via the Registry 2 vpn extension (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]
- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-ST-session_termination|D3-ST: Session Termination]]

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Containers
- Linux
- macOS
- Windows

