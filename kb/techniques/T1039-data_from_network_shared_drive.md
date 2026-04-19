---
id: T1039
name: Data from Network Shared Drive
created: 2017-05-31 21:30:41.022000+00:00
modified: 2025-10-24 17:49:13.555000+00:00
type: attack-pattern
x_mitre_version: 1.5
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106) may be used to gather information.

## Platforms

- Linux
- macOS
- Windows

## Tools


