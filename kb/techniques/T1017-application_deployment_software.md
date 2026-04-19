---
id: T1017
name: Application Deployment Software
created: 2017-05-31 21:30:27.755000+00:00
modified: 2025-10-24 17:48:37.004000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Adversaries may deploy malicious software to systems within a network using application deployment systems employed by enterprise administrators. The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the deployment server, or specific domain credentials may be required. However, the system may require an administrative account to log in or to perform software deployment.

Access to a network-wide or enterprise-wide software deployment system enables an adversary to have remote code execution on all systems that are connected to such a system. The access may be used to laterally move to systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

## Properties

- id: T1017
- name: Application Deployment Software
- created: 2017-05-31 21:30:27.755000+00:00
- modified: 2025-10-24 17:48:37.004000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Linux
- macOS
- Windows

