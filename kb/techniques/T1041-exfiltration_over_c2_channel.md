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

## Properties

- id: T1041
- name: Exfiltration Over C2 Channel
- created: 2017-05-31 21:30:41.804000+00:00
- modified: 2025-10-24 17:49:06.675000+00:00
- type: attack-pattern
- x_mitre_version: 2.3
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools

- [[S0192-pupy|S0192: Pupy]]
- [[S0363-empire|S0363: Empire]]
- [[S0434-imminent_monitor|S0434: Imminent Monitor]]
- [[S0445-shimratreporter|S0445: ShimRatReporter]]
- [[S0633-sliver|S0633: Sliver]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1050-pcshare|S1050: PcShare]]

