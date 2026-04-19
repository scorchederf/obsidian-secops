---
id: T1030
name: Data Transfer Size Limits
created: 2017-05-31 21:30:34.523000+00:00
modified: 2025-10-24 17:49:20.770000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Properties

- id: T1030
- name: Data Transfer Size Limits
- created: 2017-05-31 21:30:34.523000+00:00
- modified: 2025-10-24 17:49:20.770000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

## Tools

- [[S0699-mythic|S0699: Mythic]]
- [[S1040-rclone|S1040: Rclone]]

