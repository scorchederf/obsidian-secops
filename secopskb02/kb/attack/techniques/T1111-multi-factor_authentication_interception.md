---
mitre_id: "T1111"
mitre_name: "Multi-Factor Authentication Interception"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--dd43c543-bb85-4a6f-aa6e-160d90d06a49"
mitre_created: "2017-05-31T21:31:23.195Z"
mitre_modified: "2025-10-24T17:49:29.231Z"
mitre_version: "2.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1111/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-HCI"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc.) to gain access to credentials that can be used to access systems, services, and network resources. Use of MFA is recommended and provides a higher level of security than usernames and passwords alone, but organizations should be aware of techniques that could be used to intercept and bypass these security mechanisms. 

If a smart card is used for multi-factor authentication, then a keylogger will need to be used to obtain the password associated with a smart card during normal use. With both an inserted card and access to the smart card password, an adversary can connect to a network resource using the infected system to proxy the authentication with the inserted hardware token. (Citation: Mandiant M Trends 2011)

Adversaries may also employ a keylogger to similarly target other hardware tokens, such as RSA SecurID. Capturing token input (including a user's personal identification code) may provide temporary access (i.e. replay the one-time passcode until the next value rollover) as well as possibly enabling adversaries to reliably predict future authentication values (given access to both the algorithm and any seed values used to generate appended temporary codes). (Citation: GCN RSA June 2011)

Other methods of MFA may be intercepted and used by an adversary to authenticate. It is common for one-time codes to be sent via out-of-band communications (email, SMS). If the device and/or service is not secured, then it may be vulnerable to interception. Service providers can also be targeted: for example, an adversary may compromise an SMS messaging service in order to steal MFA codes sent to users’ phones.(Citation: Okta Scatter Swine 2022)

## Workspace

- [[workspaces/attack/techniques/T1111-multi-factor_authentication_interception-note|Open workspace note]]

![[workspaces/attack/techniques/T1111-multi-factor_authentication_interception-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]

## Platforms

- Linux
- Windows
- macOS

