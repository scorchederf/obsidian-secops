---
mitre_id: "T1200"
mitre_name: "Hardware Additions"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d40239b3-05ff-46d8-9bdd-b46d13463ef9"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:26.803Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1200/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
mitre_tactic_ids:
  - "TA0001"
---

# T1200: Hardware Additions

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]), keystroke injection, kernel memory reading via DMA, addition of new wireless access points to an existing network, and others.(Citation: Ossmann Star Feb 2011)(Citation: Aleks Weapons Nov 2015)(Citation: Frisk DMA August 2016)(Citation: McMillan Pwn March 2012)

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]

## Platforms

- Windows
- Linux
- macOS

