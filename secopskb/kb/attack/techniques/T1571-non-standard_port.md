---
mitre_id: "T1571"
mitre_name: "Non-Standard Port"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b18eae87-b469-4e14-b454-b171b416bc18"
mitre_created: "2020-03-14T18:18:32.443Z"
mitre_modified: "2025-10-24T17:49:14.187Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1571/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
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

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)

## Workspace

- [[workspaces/attack/techniques/T1571-non-standard_port-note|Open workspace note]]

![[workspaces/attack/techniques/T1571-non-standard_port-note]]

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

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools
- [[covenant|Covenant (S1155)]]
- [[quasarrat|QuasarRAT (S0262)]]


## Platforms

- ESXi
- Linux
- macOS
- Windows

