---
mitre_id: "DC0082"
mitre_name: "Network Connection Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--181a9f8c-c780-4f1f-91a8-edb770e904ba"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "mobile-attack"
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The initial establishment of a network session, where a system or process initiates a connection to a local or remote endpoint. This typically involves capturing socket information (source/destination IP, ports, protocol) and tracking session metadata. Monitoring these events helps detect lateral movement, exfiltration, and command-and-control (C2) activities.

*Data Collection Measures:*

- Windows:
    - Event ID 5156 – Filtering Platform Connection - Logs network connections permitted by Windows Filtering Platform (WFP).
    - Sysmon Event ID 3 – Network Connection Initiated - Captures process, source/destination IP, ports, and parent process.
- Linux/macOS:
    - Netfilter (iptables), nftables logs - Tracks incoming and outgoing network connections.
    - AuditD (`connect` syscall) - Logs TCP, UDP, and ICMP connections.
    - Zeek (`conn.log`) - Captures protocol, duration, and bytes transferred.
- Cloud & Network Infrastructure:
    - AWS VPC Flow Logs / Azure NSG Flow Logs - Logs IP traffic at the network level in cloud environments.
    - Zeek (conn.log) or Suricata (network events) - Captures packet metadata for detection and correlation.
- Endpoint Detection & Response (EDR):
    - Detect anomalous network activity such as new C2 connections or data exfiltration attempts.

## Workspace

- [[workspaces/attack/data-components/DC0082-network_connection_creation-note|Open workspace note]]

![[workspaces/attack/data-components/DC0082-network_connection_creation-note]]

