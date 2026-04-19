---
id: S0008
name: gsecdump
created: 2017-05-31 21:32:13.755000+00:00
modified: 2024-11-17 23:49:27.288000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# gsecdump

[gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump)

## Properties

- id: S0008
- name: gsecdump
- created: 2017-05-31 21:32:13.755000+00:00
- modified: 2024-11-17 23:49:27.288000+00:00
- type: tool
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]

