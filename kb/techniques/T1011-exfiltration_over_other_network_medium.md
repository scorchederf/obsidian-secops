---
id: T1011
name: Exfiltration Over Other Network Medium
created: 2017-05-31 21:30:25.159000+00:00
modified: 2025-10-24 17:48:47.042000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Subtechniques

### T1011.001: Exfiltration Over Bluetooth
^t1011001-exfiltration-over-bluetooth

**Parent Technique**
- [[T1011-exfiltration_over_other_network_medium|T1011: Exfiltration Over Other Network Medium]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

Adversaries may choose to do this if they have sufficient access and proximity. Bluetooth connections might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

#### Properties

- id: T1011.001
- name: Exfiltration Over Bluetooth
- created: 2020-03-09 17:07:57.392000+00:00
- modified: 2025-10-24 17:48:51.095000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

