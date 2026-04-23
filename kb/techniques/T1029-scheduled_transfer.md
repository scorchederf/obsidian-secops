---
mitre_id: "T1029"
mitre_name: "Scheduled Transfer"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4eeaf8a9-c86b-4954-a663-9555fb406466"
mitre_created: "2017-05-31T21:30:34.139Z"
mitre_modified: "2025-10-24T17:48:45.522Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1029/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
---

# T1029: Scheduled Transfer

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as [[T1041-exfiltration_over_c2_channel|T1041: Exfiltration Over C2 Channel]] or [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]].

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- Linux
- macOS
- Windows

