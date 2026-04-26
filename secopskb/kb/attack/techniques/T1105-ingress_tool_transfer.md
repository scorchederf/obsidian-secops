---
mitre_id: "T1105"
mitre_name: "Ingress Tool Transfer"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e6919abc-99f9-4c6c-95a5-14761e7b2add"
mitre_created: "2017-05-31T21:31:16.408Z"
mitre_modified: "2025-10-24T17:49:32.714Z"
mitre_version: "2.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1105/"
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
  - "Network Devices"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [[ftp|ftp (S0095)]]. Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]). 

On Windows, adversaries may use various utilities to download tools, such as `copy`, `finger`, [[certutil|certutil (S0160)]], and [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] commands such as `IEX(New-Object Net.WebClient).downloadString()` and `Invoke-WebRequest`. On Linux and macOS systems, a variety of utilities also exist, such as `curl`, `scp`, `sftp`, `tftp`, `rsync`, `finger`, and `wget`.(Citation: t1105_lolbas)  A number of these tools, such as `wget`, `curl`, and `scp`, also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via `certutil -hashfile`).(Citation: Google Cloud Threat Intelligence COSCMICENERGY 2023)

Adversaries may also abuse installers and package managers, such as `yum` or `winget`, to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows `search-ms` protocol handler, to deliver malicious files to victims through remote file searches invoked by [[T1204-user_execution|T1204: User Execution]] (typically after interacting with [[T1566-phishing|T1566: Phishing]] lures).(Citation: T1105: Trellix_search-ms)

Files can also be transferred using various [[T1102-web_service|T1102: Web Service]]s as well as native or otherwise present tools on the victim system.(Citation: PTSecurity Cobalt Dec 2016) In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine.(Citation: Dropbox Malware Sync)

## Workspace

- [[workspaces/attack/techniques/T1105-ingress_tool_transfer-note|Open workspace note]]

![[workspaces/attack/techniques/T1105-ingress_tool_transfer-note]]

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
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools
- [[asyncrat|AsyncRAT (S1087)]]
- [[bitsadmin|BITSAdmin (S0190)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[carrotball|CARROTBALL (S0465)]]
- [[certutil|certutil (S0160)]]
- [[cmd|cmd (S0106)]]
- [[cspy_downloader|CSPY Downloader (S0527)]]
- [[donut|Donut (S0695)]]
- [[empire|Empire (S0363)]]
- [[esentutl|esentutl (S0404)]]
- [[ftp|ftp (S0095)]]
- [[koadic|Koadic (S0250)]]
- [[mcmd|MCMD (S0500)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[remcos|Remcos (S0332)]]
- [[remoteutilities|RemoteUtilities (S0592)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

