---
id: T1679
name: Selective Exclusion
created: 2025-09-25 14:45:54.760000+00:00
modified: 2025-10-22 03:50:30.406000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)  

Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. 

Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals. 

## Platforms

- Windows

## Tools


