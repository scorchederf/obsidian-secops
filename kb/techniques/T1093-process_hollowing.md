---
id: T1093
name: Process Hollowing
created: 2017-05-31 21:31:09.815000+00:00
modified: 2025-10-24 17:48:28.786000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Process hollowing occurs when a process is created in a suspended state then its memory is unmapped and replaced with malicious code. Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), execution of the malicious code is masked under a legitimate process and may evade defenses and detection analysis. (Citation: Leitch Hollowing) (Citation: Elastic Process Injection July 2017)

## Properties

- id: T1093
- name: Process Hollowing
- created: 2017-05-31 21:31:09.815000+00:00
- modified: 2025-10-24 17:48:28.786000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Windows

