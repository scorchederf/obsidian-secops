---
mitre_id: "T1199"
mitre_name: "Trusted Relationship"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9fa07bef-9c81-421e-a8e5-ad4366c5a925"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-11-12T15:42:52.705Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1199/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "SaaS"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Identity Provider"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0001"
d3fend_ids:
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CSPP"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RTSD"
  - "D3-ST"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, [[T1078-valid_accounts|T1078: Valid Accounts]] used by the other party for access to internal network systems may be compromised and used.(Citation: CISA IT Service Providers)

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.(Citation: Office 365 Delegated Administration)

## Workspace

- [[workspaces/attack/techniques/T1199-trusted_relationship-note|Open workspace note]]

![[workspaces/attack/techniques/T1199-trusted_relationship-note]]

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-ST-session_termination|D3-ST: Session Termination]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]

## Platforms

- Windows
- SaaS
- IaaS
- Linux
- macOS
- Identity Provider
- Office Suite

