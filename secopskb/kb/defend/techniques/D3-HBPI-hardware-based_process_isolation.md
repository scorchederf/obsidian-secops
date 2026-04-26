---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-HBPI"
d3fend_name: "Hardware-based Process Isolation"
d3fend_ontology_id: "d3f:Hardware-basedProcessIsolation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AHardware-basedProcessIsolation/"
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
  - "T1016"
  - "T1016.001"
  - "T1016.002"
  - "T1018"
  - "T1033"
  - "T1047"
  - "T1053"
  - "T1053.002"
  - "T1053.003"
  - "T1053.005"
  - "T1053.006"
  - "T1053.007"
  - "T1055"
  - "T1055.004"
  - "T1055.013"
  - "T1057"
  - "T1082"
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
  - "T1220"
  - "T1505"
  - "T1505.001"
  - "T1505.002"
  - "T1505.003"
  - "T1546"
  - "T1546.007"
  - "T1546.009"
  - "T1546.010"
  - "T1548"
  - "T1548.002"
  - "T1550"
  - "T1550.001"
  - "T1550.002"
  - "T1550.003"
  - "T1550.004"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Preventing one process from writing to the memory space of another process through hardware based address manager implementations.

## Workspace

- [[workspaces/defend/techniques/D3-HBPI-hardware-based_process_isolation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-HBPI-hardware-based_process_isolation-note]]

## Parent Technique

- [[D3-EI-execution_isolation|D3-EI: Execution Isolation]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
- [[T1007-system_service_discovery|T1007: System Service Discovery]]
- [[T1010-application_window_discovery|T1010: Application Window Discovery]]
- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016002-wi-fi-discovery|T1016.002: Wi-Fi Discovery]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
- [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055004-asynchronous-procedure-call|T1055.004: Asynchronous Procedure Call]]
- [[T1055-process_injection#^t1055013-process-doppelgänging|T1055.013: Process Doppelgänging]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1082-system_information_discovery|T1082: System Information Discovery]]
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
- [[T1220-xsl_script_processing|T1220: XSL Script Processing]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]
- [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
- [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
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
Process isolation, in this context, is address space separation controlled by a security function that limits the communication between processes so that one process cannot directly modify the executing code of another process. For example with virtual address space:

* Process A address space is different from process B address space, which prevents process A from writing to process B

Hardware process isolation is commonly implemented through Direct Memory Access (DMA) which collaborates with a Memory Management Unit (MMU), or Input-Output Memory Management Unit (IOMMU). These hardware controls are deployed directly on processors to aid hosts or enclaves in process isolation.

* DMA - Direct memory access allows memory access to occur independently of the program currently run by the microprocessor. DMA allows for I/O devices to directly read from and write to memory, or it can be used to efficiently copy blocks of memory. During DMA transfers, the microprocessor can execute an unrelated program.
* MMU - A memory management unit acts as an access control and is responsible for performing the translation of virtual memory addresses to physical memory addresses. The MMU allocates each process its own virtual memory space.
* IOMMU - An input-output memory management unit is used to allocate each I/O device its own virtual address space to the underlying physical addresses. IOMMU allows devices that do not support long memory addresses to address the entire memory space.

## Considerations
* Private hosts may be vulnerable to DMA attack if they have a PCI or PCI Express port that connects attached devices directly to physical address space.

## Implementations:
 * Intel Virtualization Technology for Directed I/O (Intel VT-d)
 * Firecracker

## Ontology Relationships

- [[D3-EI-execution_isolation|D3-EI: Execution Isolation]]

