---
id: T1572
name: Protocol Tunneling
created: 2020-03-15 16:03:39.082000+00:00
modified: 2025-10-24 17:48:45.888000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may tunnel network communications to and from a victim system within a separate protocol to avoid detection/network filtering and/or enable access to otherwise unreachable systems. Tunneling involves explicitly encapsulating a protocol within another. This behavior may conceal malicious traffic by blending in with existing traffic and/or provide an outer layer of encryption (similar to a VPN). Tunneling could also enable routing of network packets that would otherwise not reach their intended destination, such as SMB, RDP, or other traffic that would be filtered by network appliances or not routed over the Internet. 

There are various means to encapsulate a protocol within another protocol. For example, adversaries may perform SSH tunneling (also known as SSH port forwarding), which involves forwarding arbitrary data over an encrypted SSH tunnel.(Citation: SSH Tunneling)(Citation: Sygnia Abyss Locker 2025) 

[Protocol Tunneling](https://attack.mitre.org/techniques/T1572) may also be abused by adversaries during [Dynamic Resolution](https://attack.mitre.org/techniques/T1568). Known as DNS over HTTPS (DoH), queries to resolve C2 infrastructure may be encapsulated within encrypted HTTPS packets.(Citation: BleepingComp Godlua JUL19) 

Adversaries may also leverage [Protocol Tunneling](https://attack.mitre.org/techniques/T1572) in conjunction with [Proxy](https://attack.mitre.org/techniques/T1090) and/or [Protocol or Service Impersonation](https://attack.mitre.org/techniques/T1001/003) to further conceal C2 communications and infrastructure. 

## Properties

- id: T1572
- name: Protocol Tunneling
- created: 2020-03-15 16:03:39.082000+00:00
- modified: 2025-10-24 17:48:45.888000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools

- [[S0508-ngrok|S0508: ngrok]]
- [[S0699-mythic|S0699: Mythic]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]
- [[S1144-frp|S1144: FRP]]

