---
id: T1041
name: Exfiltration Over C2 Channel
created: 2017-05-31 21:30:41.804000+00:00
modified: 2025-10-24 17:49:06.675000+00:00
type: attack-pattern
x_mitre_version: 2.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

