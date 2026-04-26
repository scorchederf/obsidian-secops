---
mitre_id: "T1029"
mitre_name: "Scheduled Transfer"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4eeaf8a9-c86b-4954-a663-9555fb406466"
mitre_created: "2017-05-31T21:30:34.139Z"
mitre_modified: "2025-10-24T17:48:45.522Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1029/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
d3fend_ids:
  - "D3-APCA"
  - "D3-CSPP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RTSD"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]] or [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]].

## Workspace

- [[workspaces/attack/techniques/T1029-scheduled_transfer-note|Open workspace note]]

![[workspaces/attack/techniques/T1029-scheduled_transfer-note]]

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- Linux
- macOS
- Windows

