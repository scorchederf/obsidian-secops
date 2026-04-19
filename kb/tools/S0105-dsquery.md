---
id: S0105
name: dsquery
created: 2017-05-31 21:33:04.937000+00:00
modified: 2025-04-16 20:38:51.407000+00:00
type: tool
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

# dsquery

[dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active Directory for information from a system within a domain. (Citation: TechNet Dsquery) It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle.

## Properties

- id: S0105
- name: dsquery
- created: 2017-05-31 21:33:04.937000+00:00
- modified: 2025-04-16 20:38:51.407000+00:00
- type: tool
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

