---
id: S1063
name: Brute Ratel C4
created: 2023-02-07 20:26:58.792000+00:00
modified: 2024-09-19 15:46:58.008000+00:00
type: tool
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Brute Ratel C4

[Brute Ratel C4](https://attack.mitre.org/software/S1063) is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. [Brute Ratel C4](https://attack.mitre.org/software/S1063) was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of [Brute Ratel C4](https://attack.mitre.org/software/S1063) was leaked in the cybercriminal underground, leading to its use by threat actors.(Citation: Dark Vortex Brute Ratel C4)(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)(Citation: SANS Brute Ratel October 2022)(Citation: Trend Micro Black Basta October 2022)

## Uses Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027007-dynamic-api-resolution|T1027.007: Dynamic API Resolution]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
    - [[T1036-masquerading#^t1036008-masquerade-file-type|T1036.008: Masquerade File Type]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055002-portable-executable-injection|T1055.002: Portable Executable Injection]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1069-permission_groups_discovery|T1069: Permission Groups Discovery]]
    - [[T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
    - [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1106-native_api|T1106: Native API]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497003-time-based-checks|T1497.003: Time Based Checks]]
- [[T1518-software_discovery|T1518: Software Discovery]]
    - [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]
- [[T1620-reflective_code_loading|T1620: Reflective Code Loading]]

