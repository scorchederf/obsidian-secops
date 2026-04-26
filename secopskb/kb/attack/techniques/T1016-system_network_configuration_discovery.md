---
mitre_id: "T1016"
mitre_name: "System Network Configuration Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--707399d6-ab3e-4963-9315-d9d3818cd6a0"
mitre_created: "2017-05-31T21:30:27.342Z"
mitre_modified: "2025-10-24T17:48:56.618Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1016/"
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
  - "TA0007"
d3fend_ids:
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DA"
  - "D3-DF"
  - "D3-EAL"
  - "D3-EDL"
  - "D3-EFA"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-HBPI"
  - "D3-LFP"
  - "D3-PSA"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-SCA"
  - "D3-SCF"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include [[arp|Arp (S0099)]], [[ipconfig|ipconfig (S0100)]]/[[ifconfig|ifconfig (S0101)]], [[nbtstat|nbtstat (S0102)]], and [[route|route (S0103)]].

Adversaries may also leverage a [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. `show ip route`, `show ip interface`).(Citation: US-CERT-TA18-106A)(Citation: Mandiant APT41 Global Intrusion ) On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command `esxcli network nic list` will retrieve the MAC address, while `esxcli network ip interface ipv4 get` will retrieve the local IPv4 address.(Citation: Trellix Rnasomhouse 2024)

Adversaries may use the information from [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]] during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next. 

## Workspace

- [[workspaces/attack/techniques/T1016-system_network_configuration_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1016-system_network_configuration_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DA-dynamic_analysis|D3-DA: Dynamic Analysis]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-EAL-executable_allowlisting|D3-EAL: Executable Allowlisting]]
- [[D3-EDL-executable_denylisting|D3-EDL: Executable Denylisting]]
- [[D3-EFA-emulated_file_analysis|D3-EFA: Emulated File Analysis]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-HBPI-hardware-based_process_isolation|D3-HBPI: Hardware-based Process Isolation]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]

## Subtechniques

### T1016.001: Internet Connection Discovery

^t1016001-internet-connection-discovery

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [[ping|Ping (S0097)]], `tracert`, and GET requests to websites, or performing initial speed testing to confirm bandwidth.

Adversaries may use the results and responses from these requests to determine if the system is capable of communicating with their C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

### T1016.002: Wi-Fi Discovery

^t1016002-wi-fi-discovery

Adversaries may search for information about Wi-Fi networks, such as network names and passwords, on compromised systems. Adversaries may use Wi-Fi information as part of [[T1087-account_discovery|T1087: Account Discovery]], [[T1018-remote_system_discovery|T1018: Remote System Discovery]], and other discovery or [[TA0006-credential_access|TA0006: Credential Access]] activity to support both ongoing and future campaigns.

Adversaries may collect various types of information about Wi-Fi networks from hosts. For example, on Windows names and passwords of all Wi-Fi networks a device has previously connected to may be available through `netsh wlan show profiles` to enumerate Wi-Fi names and then `netsh wlan show profile “Wi-Fi name” key=clear` to show a Wi-Fi network’s corresponding password.(Citation: BleepingComputer Agent Tesla steal wifi passwords)(Citation: Malware Bytes New AgentTesla variant steals WiFi credentials)(Citation: Check Point APT35 CharmPower January 2022) Additionally, names and other details of locally reachable Wi-Fi networks can be discovered using calls to `wlanAPI.dll` [[T1106-native_api|T1106: Native API]] functions.(Citation: Binary Defense Emotes Wi-Fi Spreader)

On Linux, names and passwords of all Wi-Fi-networks a device has previously connected to may be available in files under ` /etc/NetworkManager/system-connections/`.(Citation: Wi-Fi Password of All Connected Networks in Windows/Linux) On macOS, the password of a known Wi-Fi may be identified with ` security find-generic-password -wa wifiname` (requires admin username/password).(Citation: Find Wi-Fi Password on Mac)


## Tools
- [[adfind|AdFind (S0552)]]
- [[arp|Arp (S0099)]]
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[ifconfig|ifconfig (S0101)]]
- [[ipconfig|ipconfig (S0100)]]
- [[koadic|Koadic (S0250)]]
- [[nbtscan|NBTscan (S0590)]]
- [[nbtstat|nbtstat (S0102)]]
- [[nltest|Nltest (S0359)]]
- [[pcshare|PcShare (S1050)]]
- [[poshc2|PoshC2 (S0378)]]
- [[pupy|Pupy (S0192)]]
- [[quasarrat|QuasarRAT (S0262)]]
- [[route|route (S0103)]]
- [[shimratreporter|ShimRatReporter (S0445)]]
- [[sliver|Sliver (S0633)]]


## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

