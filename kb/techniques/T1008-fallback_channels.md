---
mitre_id: "T1008"
mitre_name: "Fallback Channels"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--f24faf46-3b26-4dbb-98f2-63460498e433"
mitre_created: "2017-05-31T21:30:21.689Z"
mitre_modified: "2025-10-24T17:49:35.854Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1008/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
  - "ESXi"
mitre_tactic_ids:
  - "TA0011"
---

# T1008: Fallback Channels

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Tools

- [[mythic|Mythic]]

## Platforms

- Linux
- Windows
- macOS
- ESXi

