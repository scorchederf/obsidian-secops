---
mitre_id: "T1011"
mitre_name: "Exfiltration Over Other Network Medium"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--51ea26b1-ff1e-4faa-b1a0-1114cd298c87"
mitre_created: "2017-05-31T21:30:25.159Z"
mitre_modified: "2025-10-24T17:48:47.042Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1011/"
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

# T1011: Exfiltration Over Other Network Medium

Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Subtechniques

### T1011.001: Exfiltration Over Bluetooth

^t1011001-exfiltration-over-bluetooth

Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

Adversaries may choose to do this if they have sufficient access and proximity. Bluetooth connections might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

