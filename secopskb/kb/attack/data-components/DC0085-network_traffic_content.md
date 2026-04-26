---
mitre_id: "DC0085"
mitre_name: "Network Traffic Content"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--3772e279-27d6-477a-9fe3-c6beb363594c"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:34.343Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "mobile-attack"
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

The full packet capture (PCAP) or session data that logs both protocol headers and payload content. This allows analysts to inspect command and control (C2) traffic, exfiltration, and other suspicious activity within network communications. Unlike metadata-based logs, full content analysis enables deeper protocol inspection, payload decoding, and forensic investigations.

*Data Collection Measures:*

- Network Packet Capture (Full Content Logging)
    - Wireshark / tcpdump / tshark
        - Full packet captures (PCAP files) for manual analysis or IDS correlation. `tcpdump -i eth0 -w capture.pcap`
    - Zeek (formerly Bro)
        - Extracts protocol headers and payload details into structured logs. `echo "redef Log::default_store = Log::ASCII;" > local.zeek | zeek -Cr capture.pcap local.zeek`
    - Suricata / Snort (IDS/IPS with PCAP Logging)
        - Deep packet inspection (DPI) with signature-based and behavioral analysis. `suricata -c /etc/suricata/suricata.yaml -i eth0 -l /var/log/suricata`
- Host-Based Collection
    - Sysmon Event ID 22 – DNS Query Logging, Captures DNS requests made by processes, useful for detecting C2 domains.
    - Sysmon Event ID 3 – Network Connection Initiated, Logs process-to-network connection relationships.
    - AuditD (Linux) – syscall=connect, Monitors outbound network requests from processes. `auditctl -a always,exit -F arch=b64 -S connect -k network_activity`
- Cloud & SaaS Traffic Collection
    - AWS VPC Flow Logs / Azure NSG Flow Logs / Google VPC Flow Logs, Captures metadata about inbound/outbound network traffic.
    - Cloud IDS (AWS GuardDuty, Azure Sentinel, Google Chronicle), Detects malicious activity in cloud environments by analyzing network traffic patterns.

## Workspace

- [[workspaces/attack/data-components/DC0085-network_traffic_content-note|Open workspace note]]

![[workspaces/attack/data-components/DC0085-network_traffic_content-note]]

