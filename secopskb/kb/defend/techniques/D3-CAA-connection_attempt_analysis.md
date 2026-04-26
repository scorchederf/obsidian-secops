---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CAA"
d3fend_name: "Connection Attempt Analysis"
d3fend_ontology_id: "d3f:ConnectionAttemptAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AConnectionAttemptAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.006"
  - "T1021"
  - "T1021.001"
  - "T1021.002"
  - "T1021.003"
  - "T1021.004"
  - "T1021.005"
  - "T1021.006"
  - "T1021.007"
  - "T1021.008"
  - "T1047"
  - "T1090"
  - "T1090.001"
  - "T1098"
  - "T1098.001"
  - "T1110"
  - "T1110.003"
  - "T1110.004"
  - "T1197"
  - "T1199"
  - "T1207"
  - "T1210"
  - "T1546"
  - "T1546.003"
  - "T1546.008"
  - "T1557"
  - "T1557.001"
  - "T1570"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Analyzing failed connections in a network to detect unauthorized activity.

## Workspace

- [[workspaces/defend/techniques/D3-CAA-connection_attempt_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CAA-connection_attempt_analysis-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[T1021-remote_services|T1021: Remote Services]]
- [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
- [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
- [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
- [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
- [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
- [[T1021-remote_services#^t1021007-cloud-services|T1021.007: Cloud Services]]
- [[T1021-remote_services#^t1021008-direct-cloud-vm-connections|T1021.008: Direct Cloud VM Connections]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1110-brute_force#^t1110004-credential-stuffing|T1110.004: Credential Stuffing]]
- [[T1197-bits_jobs|T1197: BITS Jobs]]
- [[T1199-trusted_relationship|T1199: Trusted Relationship]]
- [[T1207-rogue_domain_controller|T1207: Rogue Domain Controller]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

## Knowledge Base Article

## How it works
Connection Attempt Analysis in multiple ways.

### Monitoring traffic to unallocated IP space
One approach looks for failed connection attempts against unallocated IP space. First, network traffic is captured to map out the network to identify network assets as well as unallocated IP space. The map is then used to determine if connection attempts are being made to the unallocated IP space.

### Monitoring for sequentially transmitted traffic
Another approach passively inspects network traffic with application protocol analyzers observing network activity characteristics such as volume of packets sent/ received, TCP session attributes, and connection information between hosts (start time, source/destination host, services, etc.). Then using pattern matching to identify traffic which appears to be probing for network hosts.

## Considerations

* Implementations that rely on analysis of unallocated IP address space increase in their complexity with network size and decentralized network infrastructure.
* Inventory of unallocated IP space should should be continuously updated to mitigate the risk of false positives.
* IPv6 also introduces challenges including IPv6 traffic bypassing IPv4 specific protection systems (ex. firewalls and IDS) and complexity in managing both IPv6 and IPv4 addresses.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

