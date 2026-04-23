---
mitre_id: "T1041"
mitre_name: "Exfiltration Over C2 Channel"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--92d7da27-2d91-488e-a00c-059dc162766d"
mitre_created: "2017-05-31T21:30:41.804Z"
mitre_modified: "2025-10-24T17:49:06.675Z"
mitre_version: "2.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1041/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
---

# T1041: Exfiltration Over C2 Channel

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Tools

- [[pupy|Pupy]]
- [[empire|Empire]]
- [[imminent_monitor|Imminent Monitor]]
- [[shimratreporter|ShimRatReporter]]
- [[sliver|Sliver]]
- [[silenttrinity|SILENTTRINITY]]
- [[pcshare|PcShare]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

