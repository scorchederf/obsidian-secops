---
id: S0121
name: Lslsass
created: 2017-05-31 21:33:10.962000+00:00
modified: 2025-04-25 14:45:15.980000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Lslsass

[Lslsass](https://attack.mitre.org/software/S0121) is a publicly-available tool that can dump active logon session password hashes from the lsass process. (Citation: Mandiant APT1)

## Properties

- id: S0121
- name: Lslsass
- created: 2017-05-31 21:33:10.962000+00:00
- modified: 2025-04-25 14:45:15.980000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

