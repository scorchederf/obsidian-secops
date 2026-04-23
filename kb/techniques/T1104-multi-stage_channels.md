---
mitre_id: "T1104"
mitre_name: "Multi-Stage Channels"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--84e02621-8fdf-470f-bd58-993bb6a89d91"
mitre_created: "2017-05-31T21:31:15.935Z"
mitre_modified: "2025-10-24T17:49:03.646Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1104/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "ESXi"
mitre_tactic_ids:
  - "TA0011"
---

# T1104: Multi-Stage Channels

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [[T1008-fallback_channels|T1008: Fallback Channels]] in case the original first-stage communication path is discovered and blocked.

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- Linux
- macOS
- Windows
- ESXi

