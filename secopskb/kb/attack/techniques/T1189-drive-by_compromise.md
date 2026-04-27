---
mitre_id: "T1189"
mitre_name: "Drive-by Compromise"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d742a578-d70e-4d0e-96a6-02a9c30204e6"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:28.067Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1189/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Identity Provider"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0001"
d3fend_ids:
  - "D3-APCA"
  - "D3-CSPP"
  - "D3-HD"
  - "D3-IAA"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-OTF"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-PSEP"
  - "D3-RPA"
  - "D3-RTSD"
  - "D3-SAOR"
  - "D3-UA"
  - "D3-UGLPA"
  - "D3-URA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. Multiple ways of delivering exploit code to a browser exist (i.e., [[T1608-stage_capabilities#^t1608004-drive-by-target|T1608.004: Drive-by Target]]), including:

* A legitimate website is compromised, allowing adversaries to inject malicious code
* Script files served to a legitimate website from a publicly writeable cloud storage bucket are modified by an adversary
* Malicious ads are paid for and served through legitimate ad providers (i.e., [[T1583-acquire_infrastructure#^t1583008-malvertising|T1583.008: Malvertising]])
* Built-in web application interfaces that allow user-controllable content are leveraged for the insertion of malicious scripts or iFrames (e.g., cross-site scripting)

Browser push notifications may also be abused by adversaries and leveraged for malicious code injection via [[T1204-user_execution|T1204: User Execution]]. By clicking "allow" on browser push notifications, users may be granting a website permission to run JavaScript code on their browser.(Citation: Push notifications - viruspositive)(Citation: push notification -mcafee)(Citation: push notifications - malwarebytes)

Often the website used by an adversary is one visited by a specific community, such as government, a particular industry, or a particular region, where the goal is to compromise a specific user or set of users based on a shared interest. This kind of targeted campaign is often referred to a strategic web compromise or watering hole attack. There are several known examples of this occurring.(Citation: Shadowserver Strategic Web Compromise)

Typical drive-by compromise process:

1. A user visits a website that is used to host the adversary controlled content.
2. Scripts automatically execute, typically searching versions of the browser and plugins for a potentially vulnerable version. The user may be required to assist in this process by enabling scripting, notifications, or active website components and ignoring warning dialog boxes.
3. Upon finding a vulnerable version, exploit code is delivered to the browser.
4. If exploitation is successful, the adversary will gain code execution on the user's system unless other protections are in place. In some cases, a second visit to the website after the initial scan is required before exploit code is delivered.

Unlike [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]], the focus of this technique is to exploit software on a client endpoint upon visiting a website. This will commonly give an adversary access to systems on the internal network instead of external systems that may be in a DMZ.

## Workspace

- [[workspaces/attack/techniques/T1189-drive-by_compromise-note|Open workspace note]]

![[workspaces/attack/techniques/T1189-drive-by_compromise-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/4922a5dd_6743_4fc2_8e81_144374280997-flash_player_update_from_suspicious_location|Flash Player Update from Suspicious Location (high; proxy)]]
- [[kb/sigma/rules/65354b83_a2ea_4ea6_8414_3ab38be0d409-cross_site_scripting_strings|Cross Site Scripting Strings (high; webserver)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-HD-homoglyph_detection|D3-HD: Homoglyph Detection]]
- [[D3-IAA-identifier_activity_analysis|D3-IAA: Identifier Activity Analysis]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-OTF-outbound_traffic_filtering|D3-OTF: Outbound Traffic Filtering]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-PSEP-process_segment_execution_prevention|D3-PSEP: Process Segment Execution Prevention]]
- [[D3-RPA-relay_pattern_analysis|D3-RPA: Relay Pattern Analysis]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SAOR-segment_address_offset_randomization|D3-SAOR: Segment Address Offset Randomization]]
- [[D3-UA-url_analysis|D3-UA: URL Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-URA-url_reputation_analysis|D3-URA: URL Reputation Analysis]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1048-application_isolation_and_sandboxing|M1048: Application Isolation and Sandboxing]]
- [[M1050-exploit_protection|M1050: Exploit Protection]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Identity Provider
- Linux
- macOS
- Windows

