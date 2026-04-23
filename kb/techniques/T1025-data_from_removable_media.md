---
mitre_id: "T1025"
mitre_name: "Data from Removable Media"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1b7ba276-eedc-4951-a762-0ceea2c030ec"
mitre_created: "2017-05-31T21:30:31.584Z"
mitre_modified: "2025-10-24T17:48:28.431Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1025/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0009"
---

# T1025: Data from Removable Media

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[cmd|cmd]] may be used to gather information. 

Some adversaries may also use [[T1119-automated_collection|T1119: Automated Collection]] on removable media.

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- Linux
- macOS
- Windows

