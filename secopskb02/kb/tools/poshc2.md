---
mitre_id: "S0378"
mitre_name: "PoshC2"
mitre_type: "tool"
mitre_stix_id: "tool--4b57c098-f043-4da2-83ef-7588a6d426bc"
mitre_created: "2019-04-23T12:31:58.125Z"
mitre_modified: "2025-04-16T20:38:51.558Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0378/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "PoshC2"
aliases:
  - "S0378"
  - "PoshC2"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2)

## Workspace

- [[workspaces/tools/S0378-poshc2-note|Open workspace note]]

![[workspaces/tools/S0378-poshc2-note]]

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
    - [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
- [[T1201-password_policy_discovery|T1201: Password Policy Discovery]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
    - [[T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

