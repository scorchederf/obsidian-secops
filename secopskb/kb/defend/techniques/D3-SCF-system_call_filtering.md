---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SCF"
d3fend_name: "System Call Filtering"
d3fend_ontology_id: "d3f:SystemCallFiltering"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemCallFiltering/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
  - "T1003.002"
  - "T1003.004"
  - "T1007"
  - "T1010"
  - "T1012"
  - "T1016"
  - "T1016.001"
  - "T1016.002"
  - "T1018"
  - "T1033"
  - "T1036"
  - "T1036.005"
  - "T1047"
  - "T1049"
  - "T1053"
  - "T1053.002"
  - "T1053.003"
  - "T1053.005"
  - "T1053.006"
  - "T1053.007"
  - "T1055"
  - "T1055.001"
  - "T1055.003"
  - "T1055.004"
  - "T1055.005"
  - "T1055.008"
  - "T1055.013"
  - "T1055.014"
  - "T1057"
  - "T1074"
  - "T1074.001"
  - "T1082"
  - "T1106"
  - "T1113"
  - "T1124"
  - "T1134"
  - "T1134.004"
  - "T1140"
  - "T1212"
  - "T1218"
  - "T1218.001"
  - "T1218.002"
  - "T1218.003"
  - "T1218.005"
  - "T1218.011"
  - "T1218.013"
  - "T1220"
  - "T1497"
  - "T1497.003"
  - "T1505"
  - "T1505.001"
  - "T1505.002"
  - "T1505.003"
  - "T1518"
  - "T1518.001"
  - "T1546"
  - "T1546.007"
  - "T1546.009"
  - "T1546.010"
  - "T1548"
  - "T1548.002"
  - "T1548.004"
  - "T1550"
  - "T1550.001"
  - "T1550.002"
  - "T1550.003"
  - "T1550.004"
  - "T1555"
  - "T1555.003"
  - "T1556"
  - "T1556.001"
  - "T1556.002"
  - "T1556.003"
  - "T1556.004"
  - "T1556.005"
  - "T1556.006"
  - "T1556.007"
  - "T1556.008"
  - "T1556.009"
  - "T1562"
  - "T1562.001"
  - "T1621"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Controlling access to local computer system resources with kernel-level capabilities.

## Workspace

- [[workspaces/defend/techniques/D3-SCF-system_call_filtering-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SCF-system_call_filtering-note]]

## Parent Technique

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

## Child Techniques

- [[D3-LFAM-local_file_access_mediation|D3-LFAM: Local File Access Mediation]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1010-application_window_discovery|T1010: Application Window Discovery]]
- [[T1012-query_registry|T1012: Query Registry]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016002-wi-fi-discovery|T1016.002: Wi-Fi Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
- [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
- [[T1055-process_injection#^t1055003-thread-execution-hijacking|T1055.003: Thread Execution Hijacking]]
- [[T1055-process_injection#^t1055004-asynchronous-procedure-call|T1055.004: Asynchronous Procedure Call]]
- [[T1055-process_injection#^t1055005-thread-local-storage|T1055.005: Thread Local Storage]]
- [[T1055-process_injection#^t1055008-ptrace-system-calls|T1055.008: Ptrace System Calls]]
- [[T1055-process_injection#^t1055013-process-doppelgänging|T1055.013: Process Doppelgänging]]
- [[T1055-process_injection#^t1055014-vdso-hijacking|T1055.014: VDSO Hijacking]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1074-data_staged|T1074: Data Staged]]
- [[T1074-data_staged#^t1074001-local-data-staging|T1074.001: Local Data Staging]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
- [[T1106-native_api|T1106: Native API]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1124-system_time_discovery|T1124: System Time Discovery]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134004-parent-pid-spoofing|T1134.004: Parent PID Spoofing]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218001-compiled-html-file|T1218.001: Compiled HTML File]]
- [[T1218-system_binary_proxy_execution#^t1218002-control-panel|T1218.002: Control Panel]]
- [[T1218-system_binary_proxy_execution#^t1218003-cmstp|T1218.003: CMSTP]]
- [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
- [[T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]
- [[T1218-system_binary_proxy_execution#^t1218013-mavinject|T1218.013: Mavinject]]
- [[T1220-xsl_script_processing|T1220: XSL Script Processing]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
- [[T1497-virtualization_sandbox_evasion#^t1497003-time-based-checks|T1497.003: Time Based Checks]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1518-software_discovery|T1518: Software Discovery]]
- [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
- [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1548-abuse_elevation_control_mechanism#^t1548004-elevated-execution-with-prompt|T1548.004: Elevated Execution with Prompt]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
- [[T1556-modify_authentication_process#^t1556002-password-filter-dll|T1556.002: Password Filter DLL]]
- [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
- [[T1556-modify_authentication_process#^t1556004-network-device-authentication|T1556.004: Network Device Authentication]]
- [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
- [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
- [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
- [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
- [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
- [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]]

## Knowledge Base Article

## How it works
System call filtering uses a mandatory access control paradigm (that is, a non-discretionary access control) system because the rules and polices that determine access is determined by a security control authority and not distributed to local users. Access determinations are based on designed access control polices and are not based on local resource owner determinations.

Access is typically granted by defining sets of subjects and sets of objects. Subjects are the entities requesting access and objects are the resources that subjects are trying to access. Rules and policies are defined that associate subjects and object permissions and access controls.

### Common implementations
#### Security label access control
A fine-grained form control is to apply security labels to individual resources, including processes, and the access control decisions are against a particular resource and a given user attempting to gain access. This type of control requires that the file system has built-in support for security labels.

Access controls are typically implemented through the use of label identifiers for every file system object. Identifier labels are applied to resources and users are assigned a similar access identifier. Users attempting to access a resource will result in the operating system performing an access control check. The access control check will compare the assigned user's credentials to that of the resource or object they are attempting to access.

A security context is associated with resources and is used to determine assess. Typical basic access control elements include users, roles and types and together they form a security context which is the basis for the security labels.

This type of access control is what is employed in SELinux [2]. This form of security kernel access control is considered the most flexible implementation, but it also is the most complex to deploy across the enterprise. Where multiple virtual machines (VM) are run together this type of access control is typically employed to ensure true isolation of processes and VMs.

#### File path level controls
A less fine-grained form of mandatory access control is to apply security labels that allow for access control at the file path level.  Access control is filesystem agnostic and no relabeling of resources is required. Pathname access control usually seems more natural for implementation and corresponding access audits.

This type of system call filtering is what is employed in AppArmor [3]. AppArmor was developed to provide a simpler alternative method with much less management overhead. A simple access policy is maintained that defines path resource access rules. Access control attributes are typically associated with programs instead of users.


## Considerations
Some implementations of security label-based control contain complex rules set that are hard to verify and complex to maintain over time.

Initial planning of access model and continuous monitoring of the available users, resources and object is necessary.

## Implementations

 * Linux C-Groups, and policy engines like SELinux and AppArmor
 * Windows Mandatory Integrity Control introduced in Windows Vista


### Citations
1. [SELinux](https://selinuxproject.org/)
2. [AppArmor](https://www.apparmor.net/)

## Ontology Relationships

- [[D3-AMED-access_mediation|D3-AMED: Access Mediation]]

