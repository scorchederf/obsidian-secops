---
mitre_id: "DC0103"
mitre_name: "Active DNS"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--2e521444-7295-4dec-96c1-7595b2df7811"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

"Domain Name: Active DNS" data component captures queried DNS registry data that highlights current domain-to-IP address resolutions. This data includes both direct queries to DNS servers and records that provide mappings between domain names and associated IP addresses. It serves as a critical resource for tracking active infrastructure and understanding the network footprint of an organization or adversary. Examples: 

- DNS Query Example: `nslookup example.com`, `dig example.com A`
- PTR Record Example: `dig -x 192.168.1.1`
- Tracking Malicious Domains: DNS logs reveal repeated queries to suspicious domains like malicious-site.com. The IPs resolved by these domains may be indicators of compromise (IOCs).
- DNS Record Types
    - A/AAAA Record: Maps domain names to IP addresses (IPv4/IPv6).
    - CNAME Record: Canonical name records, often used for redirects.
    - MX Record: Mail exchange records, used to route emails.
    - TXT Record: Can include security information like SPF or DKIM policies.
    - SOA Record: Start of authority record for domain management.
    - NS Record: Lists authoritative name servers for the domain.

This data component can be collected through the following measures:

- System Utilities: Use built-in tools like `nslookup`, `dig`, or host on Linux, macOS, and Windows to perform active DNS queries.
- DNS Logging
    - Windows DNS Server: Enable DNS Analytical Logging to capture DNS queries and responses.
    - Bind DNS: Enable query logging in the named.conf file.
- Cloud Provider DNS Logging
    - AWS Route 53: Enable query logging through CloudWatch or S3:
    - Google Cloud DNS: Enable logging for Cloud DNS queries through Google Cloud Logging.
- Network Traffic Monitoring: Use tools like Wireshark or Zeek to analyze DNS queries within network traffic.
- Security Information and Event Management (SIEM) Integration: Aggregate DNS logs in a SIEM like Splunk to create alerts and monitor patterns.
- Public OSINT Tools: Use OSINT platforms like VirusTotal, or PassiveTotal to collect information on domains and their associated IP addresses.

## Workspace

- [[workspaces/attack/data-components/DC0103-active_dns-note|Open workspace note]]

![[workspaces/attack/data-components/DC0103-active_dns-note]]

