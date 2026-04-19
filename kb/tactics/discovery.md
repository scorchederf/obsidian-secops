---
id: x-mitre-tactic--c17c5845-175e-4421-9713-829d0573dbc9
name: Discovery
created: 2018-10-17 00:14:20.652000+00:00
modified: 2025-04-25 14:45:35.302000+00:00
type: x-mitre-tactic
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Discovery

The adversary is trying to figure out your environment.

Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective. 

## Properties

- id: x-mitre-tactic--c17c5845-175e-4421-9713-829d0573dbc9
- name: Discovery
- created: 2018-10-17 00:14:20.652000+00:00
- modified: 2025-04-25 14:45:35.302000+00:00
- type: x-mitre-tactic
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Related Techniques

- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1010-application_window_discovery|T1010: Application Window Discovery]]
- [[T1012-query_registry|T1012: Query Registry]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
    - [[T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]
    - [[T1016-system_network_configuration_discovery#^t1016002-wi-fi-discovery|T1016.002: Wi-Fi Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1063-security_software_discovery|T1063: Security Software Discovery]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
    - [[T1069-permission_groups_discovery#^t1069003-cloud-groups|T1069.003: Cloud Groups]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
    - [[T1087-account_discovery#^t1087003-email-account|T1087.003: Email Account]]
    - [[T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[T1120-peripheral_device_discovery|T1120: Peripheral Device Discovery]]
- [[T1124-system_time_discovery|T1124: System Time Discovery]]
- [[T1135-network_share_discovery|T1135: Network Share Discovery]]
- [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]
- [[T1217-browser_information_discovery|T1217: Browser Information Discovery]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]
    - [[T1497-virtualization_sandbox_evasion#^t1497002-user-activity-based-checks|T1497.002: User Activity Based Checks]]
    - [[T1497-virtualization_sandbox_evasion#^t1497003-time-based-checks|T1497.003: Time Based Checks]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
    - [[T1518-software_discovery#^t1518002-backup-software-discovery|T1518.002: Backup Software Discovery]]
- [[T1526-cloud_service_discovery|T1526: Cloud Service Discovery]]
- [[T1538-cloud_service_dashboard|T1538: Cloud Service Dashboard]]
- [[T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]
- [[T1613-container_and_resource_discovery|T1613: Container and Resource Discovery]]
- [[T1614-system_location_discovery|T1614: System Location Discovery]]
    - [[T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]
- [[T1615-group_policy_discovery|T1615: Group Policy Discovery]]
- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]
- [[T1622-debugger_evasion|T1622: Debugger Evasion]]
- [[T1652-device_driver_discovery|T1652: Device Driver Discovery]]
- [[T1654-log_enumeration|T1654: Log Enumeration]]
- [[T1673-virtual_machine_discovery|T1673: Virtual Machine Discovery]]
- [[T1680-local_storage_discovery|T1680: Local Storage Discovery]]
