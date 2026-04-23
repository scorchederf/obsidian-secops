---
mitre_id: "S0413"
mitre_name: "MailSniper"
mitre_type: "tool"
mitre_stix_id: "tool--999c4e6e-b8dc-4b4f-8d6e-1b829f29997e"
mitre_created: "2019-10-05T02:34:01.189Z"
mitre_modified: "2024-10-14T22:11:30.271Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0413/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_aliases:
  - "MailSniper"
---

# MailSniper

MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used by a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain.(Citation: GitHub MailSniper)

## Uses Techniques

- [[T1087-account_discovery|T1087: Account Discovery]]
- [[T1087-account_discovery#^t1087003-email-account|T1087.003: Email Account]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]

