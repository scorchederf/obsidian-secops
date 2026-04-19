---
id: S0488
name: CrackMapExec
created: 2020-07-17 14:23:05.958000+00:00
modified: 2024-03-14 17:29:49.200000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# CrackMapExec

[CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018)

## Properties

- id: S0488
- name: CrackMapExec
- created: 2020-07-17 14:23:05.958000+00:00
- modified: 2024-03-14 17:29:49.200000+00:00
- type: tool
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1110-brute_force|T1110: Brute Force]]
    - [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
    - [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1135-network_share_discovery|T1135: Network Share Discovery]]
- [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1680-local_storage_discovery|T1680: Local Storage Discovery]]

