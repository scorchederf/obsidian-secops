---
mitre_id: "T1008"
mitre_name: "Fallback Channels"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f24faf46-3b26-4dbb-98f2-63460498e433"
mitre_created: "2017-05-31T21:30:21.689Z"
mitre_modified: "2025-10-24T17:49:35.854Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1008/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0011"
d3fend_ids:
  - "D3-APCA"
  - "D3-CSPP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RPA"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Workspace

- [[workspaces/attack/techniques/T1008-fallback_channels-note|Open workspace note]]

![[workspaces/attack/techniques/T1008-fallback_channels-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/117d3d3a_755c_4a61_b23e_9171146d094c-suspicious_outlook_macro_created|Suspicious Outlook Macro Created (high; windows / file_event)]]
- [[kb/sigma/rules/396ae3eb_4174_4b9b_880e_dc0364d78a19-potential_persistence_via_outlook_loadmacroprovideronboot_setting|Potential Persistence Via Outlook LoadMacroProviderOnBoot Setting (high; windows / registry_set)]]
- [[kb/sigma/rules/e3b50fa5_3c3f_444e_937b_0a99d33731cd-outlook_macro_execution_without_warning_setting_enabled|Outlook Macro Execution Without Warning Setting Enabled (high; windows / registry_set)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools

- [[mythic|Mythic (S0699)]]

## Platforms

- Linux
- Windows
- macOS
- ESXi

