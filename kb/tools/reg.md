---
id: S0075
name: Reg
created: 2017-05-31 21:32:49+00:00
modified: 2025-04-16 20:38:56.474000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Reg

[Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)

Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT)

## Uses Techniques

- [[T1012-query_registry|T1012: Query Registry]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

