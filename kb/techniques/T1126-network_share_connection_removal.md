---
id: T1126
name: Network Share Connection Removal
created: 2017-05-31 21:31:38.350000+00:00
modified: 2025-10-24 17:49:32.975000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation. Windows shared drive and [Windows Admin Shares](https://attack.mitre.org/techniques/T1077) connections can be removed when no longer needed. [Net](https://attack.mitre.org/software/S0039) is an example utility that can be used to remove network share connections with the <code>net use \\system\share /delete</code> command. (Citation: Technet Net Use)



## Platforms

- Windows

