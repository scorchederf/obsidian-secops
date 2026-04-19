---
id: T1200
name: Hardware Additions
created: 2018-04-18 17:59:24.739000+00:00
modified: 2025-10-24 17:49:26.803000+00:00
type: attack-pattern
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[initial_access|Initial Access]]

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091)), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)), keystroke injection, kernel memory reading via DMA, addition of new wireless access points to an existing network, and others.(Citation: Ossmann Star Feb 2011)(Citation: Aleks Weapons Nov 2015)(Citation: Frisk DMA August 2016)(Citation: McMillan Pwn March 2012)

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]

## Platforms

- Windows
- Linux
- macOS

