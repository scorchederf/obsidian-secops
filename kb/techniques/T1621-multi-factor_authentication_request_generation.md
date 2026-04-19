---
id: T1621
name: Multi-Factor Authentication Request Generation
created: 2022-04-01 02:15:49.754000+00:00
modified: 2025-10-24 17:49:07.399000+00:00
type: attack-pattern
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession of credentials to [Valid Accounts](https://attack.mitre.org/techniques/T1078) may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured for self-service password reset (SSPR).(Citation: Obsidian SSPR Abuse 2023)

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to “MFA fatigue.”(Citation: Russian 2FA Push Annoyance - Cimpanu)(Citation: MFA Fatigue Attacks - PortSwigger)(Citation: Suspected Russian Activity Targeting Government and Business Entities Around the Globe)

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

