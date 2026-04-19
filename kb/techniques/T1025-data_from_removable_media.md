---
id: T1025
name: Data from Removable Media
created: 2017-05-31 21:30:31.584000+00:00
modified: 2025-10-24 17:48:28.431000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information. 

Some adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on removable media.

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- Linux
- macOS
- Windows

## Tools


