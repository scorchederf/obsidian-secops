---
mitre_id: "DC0106"
mitre_name: "Response Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--1067aa74-5796-4d9b-b4f1-a4c9eb6fd9da"
mitre_created: "2021-10-20T15:05:19.275Z"
mitre_modified: "2025-10-21T15:14:40.350Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0106: Response Metadata

Contextual information about an Internet-facing resource collected during a scan, including details such as open ports, running services, protocols, and versions. This metadata is typically derived from interpreting scan results and helps build a profile of the targeted system. Examples: 

- Port and Service Details:
    - Open ports (e.g., 22, 80, 443).
    - Identified services running on those ports (e.g., SSH, HTTP, HTTPS).
- Service Versions: Detected software version information (e.g., Apache 2.4.41, OpenSSH 8.2).
- Operating System Information: OS fingerprinting data (e.g., Linux Kernel 5.4.0).
- TLS/SSL Certificate Data: Information about the TLS/SSL certificate, such as the expiration date, issuer, and cipher suites.

*Data Collection Measures:*

- Scanning Tools:
    - Nmap: Collects port, service, and version information using commands like nmap -sV <IP>.
    - Masscan: High-speed scanning tool for discovering open ports and active services.
    - Zmap: Focused on large-scale Internet scanning, collecting metadata about discovered services.
    - Shodan API: Retrieves scan metadata for publicly exposed devices and services.
- Network Logs:
    - Use logs from firewalls, intrusion detection systems (IDS), or intrusion prevention systems (IPS) to gather metadata from scan attempts. Example: Zeek or Suricata logs for incoming scan traffic.
- OSINT Platforms: Platforms like Censys, GreyNoise, or Shodan provide aggregated metadata about Internet-facing resources.
- Cloud Metadata Services: AWS Security Hub, Azure Monitor, or GCP Security Command Center can collect and centralize scan-related metadata for Internet-facing resources in cloud environments.

## Workspace

- [[kb/notes/attack/data-components/dc0106-notes|Open workspace note]]

