---
mitre_id: "T1621"
mitre_name: "Multi-Factor Authentication Request Generation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--954a1639-f2d6-407d-aef3-4917622ca493"
mitre_created: "2022-04-01T02:15:49.754Z"
mitre_modified: "2025-10-24T17:49:07.399Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1621/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "IaaS"
  - "SaaS"
  - "Office Suite"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
---

# T1621: Multi-Factor Authentication Request Generation

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession of credentials to [[T1078-valid_accounts|T1078: Valid Accounts]] may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured for self-service password reset (SSPR).(Citation: Obsidian SSPR Abuse 2023)

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to “MFA fatigue.”(Citation: Russian 2FA Push Annoyance - Cimpanu)(Citation: MFA Fatigue Attacks - PortSwigger)(Citation: Suspected Russian Activity Targeting Government and Business Entities Around the Globe)

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1036-account_use_policies|M1036: Account Use Policies]]

## Platforms

- Windows
- Linux
- macOS
- IaaS
- SaaS
- Office Suite
- Identity Provider

