---
id: T1075
name: Pass the Hash
created: 2017-05-31 21:30:59.339000+00:00
modified: 2025-10-24 17:49:20.221000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Pass the hash (PtH) is a method of authenticating as a user without having access to the user's cleartext password. This method bypasses standard authentication steps that require a cleartext password, moving directly into the portion of the authentication that uses the password hash. In this technique, valid password hashes for the account being used are captured using a Credential Access technique. Captured hashes are used with PtH to authenticate as that user. Once authenticated, PtH may be used to perform actions on local or remote systems. 

Windows 7 and higher with KB2871997 require valid domain user credentials or RID 500 administrator hashes. (Citation: NSA Spotting)

## Properties

- id: T1075
- name: Pass the Hash
- created: 2017-05-31 21:30:59.339000+00:00
- modified: 2025-10-24 17:49:20.221000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Platforms

- Windows

