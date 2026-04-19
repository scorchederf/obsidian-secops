---
id: T1108
name: Redundant Access
created: 2017-05-31 21:31:18.867000+00:00
modified: 2025-10-24 17:48:54.749000+00:00
type: attack-pattern
x_mitre_version: 3.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

**This technique has been deprecated. Please use [Create Account](https://attack.mitre.org/techniques/T1136), [Web Shell](https://attack.mitre.org/techniques/T1505/003), and [External Remote Services](https://attack.mitre.org/techniques/T1133) where appropriate.**

Adversaries may use more than one remote access tool with varying command and control protocols or credentialed access to remote services so they can maintain access if an access mechanism is detected or mitigated. 

If one type of tool is detected and blocked or removed as a response but the organization did not gain a full understanding of the adversary's tools and access, then the adversary will be able to retain access to the network. Adversaries may also attempt to gain access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) to use [External Remote Services](https://attack.mitre.org/techniques/T1133) such as external VPNs as a way to maintain access despite interruptions to remote access tools deployed within a target network.(Citation: Mandiant APT1) Adversaries may also retain access through cloud-based infrastructure and applications.

Use of a [Web Shell](https://attack.mitre.org/techniques/T1100) is one such way to maintain access to a network through an externally accessible Web server.

## Platforms

- Windows
- SaaS
- IaaS
- Linux
- macOS
- Office Suite
- Identity Provider

