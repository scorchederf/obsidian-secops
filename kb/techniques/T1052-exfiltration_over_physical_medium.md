---
mitre_id: "T1052"
mitre_name: "Exfiltration Over Physical Medium"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e6415f09-df0e-48de-9aba-928c902b7549"
mitre_created: "2017-05-31T21:30:46.461Z"
mitre_modified: "2025-10-24T17:49:32.547Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1052/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0010"
---

# T1052: Exfiltration Over Physical Medium

Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Tactics

- [[TA0010-exfiltration|TA0010: Exfiltration]]

## Subtechniques

### T1052.001: Exfiltration over USB

^t1052001-exfiltration-over-usb

Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- Linux
- macOS
- Windows

