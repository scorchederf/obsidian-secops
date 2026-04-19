---
id: T1681
name: Search Threat Vendor Data
created: 2025-09-26 15:42:30.468000+00:00
modified: 2025-10-24 17:48:51.996000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[reconnaissance|Reconnaissance]]

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations. 

Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation.(Citation: Sentinel One Contagious Interview ClickFix September 2025)

This technique is distinct from [Threat Intel Vendors](https://attack.mitre.org/techniques/T1597/001) in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information. 

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

