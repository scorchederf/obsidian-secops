---
id: T1072
name: Software Deployment Tools
created: 2017-05-31 21:30:57.201000+00:00
modified: 2025-10-24 17:49:06.595000+00:00
type: attack-pattern
x_mitre_version: 3.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Adversaries may gain access to and use centralized software suites installed within an enterprise to execute commands and move laterally through the network. Configuration management and software deployment applications may be used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune, Azure Arc, and GCP Deployment Manager.  

Access to network-wide or enterprise-wide endpoint management software may enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

SaaS-based configuration management services may allow for broad [Cloud Administration Command](https://attack.mitre.org/techniques/T1651) on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to Entra ID.(Citation: SpecterOps Lateral Movement from Azure to On-Prem AD 2020) Such services may also utilize [Web Protocols](https://attack.mitre.org/techniques/T1071/001) to communicate back to adversary owned infrastructure.(Citation: Mitiga Security Advisory: SSM Agent as Remote Access Trojan)

Network infrastructure devices may also have configuration management tools that can be similarly abused by adversaries.(Citation: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation)

The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the third-party system, or specific domain credentials may be required. However, the system may require an administrative account to log in or to access specific functionality.

## Properties

- id: T1072
- name: Software Deployment Tools
- created: 2017-05-31 21:30:57.201000+00:00
- modified: 2025-10-24 17:49:06.595000+00:00
- type: attack-pattern
- x_mitre_version: 3.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1017-user_training|M1017: User Training]]
- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1029-remote_data_storage|M1029: Remote Data Storage]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1033-limit_software_installation|M1033: Limit Software Installation]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- macOS
- Network Devices
- SaaS
- Windows

## Tools


