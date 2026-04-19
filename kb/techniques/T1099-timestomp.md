---
id: T1099
name: Timestomp
created: 2017-05-31 21:31:12.675000+00:00
modified: 2025-10-24 17:48:25.923000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may take actions to hide the deployment of new, or modification of existing files to obfuscate their activities. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder. This is done, for example, on files that have been modified or created by the adversary so that they do not appear conspicuous to forensic investigators or file analysis tools. Timestomping may be used along with file name [Masquerading](https://attack.mitre.org/techniques/T1036) to hide malware and tools. (Citation: WindowsIR Anti-Forensic Techniques)

## Platforms

- Linux
- Windows
- macOS

