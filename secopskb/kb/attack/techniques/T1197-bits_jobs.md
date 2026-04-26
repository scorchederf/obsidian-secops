---
mitre_id: "T1197"
mitre_name: "BITS Jobs"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c8e87b83-edbb-48d4-9295-4974897525b7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:22.711Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1197/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0003"
d3fend_ids:
  - "D3-APCA"
  - "D3-CAA"
  - "D3-CSPP"
  - "D3-IPCTA"
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

Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]] (COM).(Citation: Microsoft COM)(Citation: Microsoft BITS) BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.

The interface to create and manage BITS jobs is accessible through [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] and the [[bitsadmin|BITSAdmin (S0190)]] tool.(Citation: Microsoft BITS)(Citation: Microsoft BITSAdmin)

Adversaries may abuse BITS to download (e.g. [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]), execute, and even clean up after running malicious code (e.g. [[T1070-indicator_removal|T1070: Indicator Removal]]). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls.(Citation: CTU BITS Malware June 2016)(Citation: Mondok Windows PiggyBack BITS May 2007)(Citation: Symantec BITS May 2007) BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).(Citation: PaloAlto UBoatRAT Nov 2017)(Citation: CTU BITS Malware June 2016)

BITS upload functionalities can also be used to perform [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]].(Citation: CTU BITS Malware June 2016)

## Workspace

- [[workspaces/attack/techniques/T1197-bits_jobs-note|Open workspace note]]

![[workspaces/attack/techniques/T1197-bits_jobs-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-IPCTA-ipc_traffic_analysis|D3-IPCTA: IPC Traffic Analysis]]
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

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools

- [[bitsadmin|BITSAdmin (S0190)]]

## Platforms

- Windows

