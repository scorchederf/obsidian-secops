---
mitre_id: "T1072"
mitre_name: "Software Deployment Tools"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--92a78814-b191-47ca-909c-1ccfe3777414"
mitre_created: "2017-05-31T21:30:57.201Z"
mitre_modified: "2025-10-24T17:49:06.595Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1072/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "SaaS"
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
  - "TA0008"
---

# T1072: Software Deployment Tools

Adversaries may gain access to and use centralized software suites installed within an enterprise to execute commands and move laterally through the network. Configuration management and software deployment applications may be used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune, Azure Arc, and GCP Deployment Manager.  

Access to network-wide or enterprise-wide endpoint management software may enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

SaaS-based configuration management services may allow for broad [[T1651-cloud_administration_command|T1651: Cloud Administration Command]] on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to Entra ID.(Citation: SpecterOps Lateral Movement from Azure to On-Prem AD 2020) Such services may also utilize [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]] to communicate back to adversary owned infrastructure.(Citation: Mitiga Security Advisory: SSM Agent as Remote Access Trojan)

Network infrastructure devices may also have configuration management tools that can be similarly abused by adversaries.(Citation: Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation)

The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the third-party system, or specific domain credentials may be required. However, the system may require an administrative account to log in or to access specific functionality.

## Tactics

- [[TA0002-execution|TA0002: Execution]]
- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

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

