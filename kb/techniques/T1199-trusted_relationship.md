---
mitre_id: "T1199"
mitre_name: "Trusted Relationship"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9fa07bef-9c81-421e-a8e5-ad4366c5a925"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-11-12T15:42:52.705Z"
mitre_version: "2.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1199/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "SaaS"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Identity Provider"
  - "Office Suite"
mitre_tactic_ids:
  - "TA0001"
---

# T1199: Trusted Relationship

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, [[T1078-valid_accounts|T1078: Valid Accounts]] used by the other party for access to internal network systems may be compromised and used.(Citation: CISA IT Service Providers)

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant.(Citation: Office 365 Delegated Administration)

## Tactics

- [[TA0001-initial_access|TA0001: Initial Access]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]

## Platforms

- Windows
- SaaS
- IaaS
- Linux
- macOS
- Identity Provider
- Office Suite

