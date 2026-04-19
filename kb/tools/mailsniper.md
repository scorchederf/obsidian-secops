---
id: S0413
name: MailSniper
created: 2019-10-05 02:34:01.189000+00:00
modified: 2024-10-14 22:11:30.271000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# MailSniper

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.(Citation: GitHub MailSniper)

## Properties

- id: S0413
- name: MailSniper
- created: 2019-10-05 02:34:01.189000+00:00
- modified: 2024-10-14 22:11:30.271000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087003-email-account|T1087.003: Email Account]]
- [[T1110-brute_force|T1110: Brute Force]]
    - [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]

