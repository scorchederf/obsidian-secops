---
mitre_id: "T1572"
mitre_name: "Protocol Tunneling"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4fe28b27-b13c-453e-a386-c2ef362a573b"
mitre_created: "2020-03-15T16:03:39.082Z"
mitre_modified: "2025-10-24T17:48:45.888Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1572/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0011"
---

# T1572: Protocol Tunneling

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling)(Citation: Sygnia Abyss Locker 2025) 

[[T1572-protocol_tunneling|T1572: Protocol Tunneling]] may also be abused by adversaries during [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]. Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [[T1572-protocol_tunneling|T1572: Protocol Tunneling]] in conjunction with [[T1090-proxy|T1090: Proxy]] and/or [[T1001-data_obfuscation#^t1001003-protocol-or-service-impersonation|T1001.003: Protocol or Service Impersonation]] to further conceal C2 communications and infrastructure. 

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools

- [[ngrok|ngrok]]
- [[mythic|Mythic]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[frp|FRP]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

