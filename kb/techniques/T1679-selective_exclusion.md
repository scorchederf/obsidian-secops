---
mitre_id: "T1679"
mitre_name: "Selective Exclusion"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9b00925a-7c4b-4e53-bfc8-9a6a806fde03"
mitre_created: "2025-09-25T14:45:54.760Z"
mitre_modified: "2025-10-22T03:50:30.406Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1679/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1679: Selective Exclusion

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include `.dll`, `.exe`, and `.lnk`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)  

Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. 

Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals. 

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Platforms

- Windows

