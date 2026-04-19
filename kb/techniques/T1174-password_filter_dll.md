---
id: T1174
name: Password Filter DLL
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-10-24 17:49:17.124000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Windows password filters are password policy enforcement mechanisms for both domain and local accounts. Filters are implemented as dynamic link libraries (DLLs) containing a method to validate potential passwords against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers for domain accounts.

Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered filter acknowledges validation.

Adversaries can register malicious password filters to harvest credentials from local computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA. A malicious password filter would receive these plain-text credentials every time a password request is made. (Citation: Carnal Ownage Password Filters Sept 2013)

## Platforms

- Windows

