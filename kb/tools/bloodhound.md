---
id: S0521
name: BloodHound
created: 2020-10-28 12:51:29.358000+00:00
modified: 2025-03-12 20:27:03.654000+00:00
type: tool
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

# BloodHound

[BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike BloodHound April 2018)(Citation: FoxIT Wocao December 2019)

## Properties

- id: S0521
- name: BloodHound
- created: 2020-10-28 12:51:29.358000+00:00
- modified: 2025-03-12 20:27:03.654000+00:00
- type: tool
- x_mitre_version: 1.7
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1106-native_api|T1106: Native API]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
- [[T1615-group_policy_discovery|T1615: Group Policy Discovery]]

