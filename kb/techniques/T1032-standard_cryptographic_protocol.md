---
id: T1032
name: Standard Cryptographic Protocol
created: 2017-05-31 21:30:35.334000+00:00
modified: 2025-10-24 17:48:44.574000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may explicitly employ a known encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if necessary secret keys are encoded and/or generated within malware samples/configuration files.

## Platforms

- Linux
- macOS
- Windows

