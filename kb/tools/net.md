---
mitre_id: "S0039"
mitre_name: "Net"
mitre_type: "tool"
mitre_stix_id: "tool--03342581-f790-4f03-ba41-e82e67392e23"
mitre_created: "2017-05-31T21:32:31.601Z"
mitre_modified: "2024-11-27T21:55:29.681Z"
mitre_version: "2.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0039/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "Net"
  - "net.exe"
---

# Net

The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)

[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>.

## Uses Techniques

- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070005-network-share-connection-removal|T1070.005: Network Share Connection Removal]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098007-additional-local-or-domain-groups|T1098.007: Additional Local or Domain Groups]]
- [[T1124-system_time_discovery|T1124: System Time Discovery]]
- [[T1135-network_share_discovery|T1135: Network Share Discovery]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
- [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

