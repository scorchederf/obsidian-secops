---
id: T1052
name: Exfiltration Over Physical Medium
created: 2017-05-31 21:30:46.461000+00:00
modified: 2025-10-24 17:49:32.547000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[exfiltration|Exfiltration]]

Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Properties

- id: T1052
- name: Exfiltration Over Physical Medium
- created: 2017-05-31 21:30:46.461000+00:00
- modified: 2025-10-24 17:49:32.547000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1052.001: Exfiltration over USB

^t1052001-exfiltration-over-usb

**Parent Technique**
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]

**Tactic**
- [[exfiltration|Exfiltration]]

Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

#### Properties

- id: T1052.001
- name: Exfiltration over USB
- created: 2020-03-11 13:50:11.467000+00:00
- modified: 2025-10-24 17:49:10.994000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- Linux
- macOS
- Windows

