---
mitre_id: "T1030"
mitre_name: "Data Transfer Size Limits"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c3888c54-775d-4b2f-b759-75a2ececcbfd"
mitre_created: "2017-05-31T21:30:34.523Z"
mitre_modified: "2025-10-24T17:49:20.770Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1030/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "ESXi"
mitre_tactic_ids:
  - "TA0010"
---

# T1030: Data Transfer Size Limits

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools

- [[mythic|Mythic]]
- [[rclone|Rclone]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

