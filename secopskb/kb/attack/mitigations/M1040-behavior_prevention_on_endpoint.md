---
mitre_id: "M1040"
mitre_name: "Behavior Prevention on Endpoint"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--90f39ee1-d5a3-4aaa-9f28-3b42815b0d46"
mitre_created: "2019-06-11T16:43:05.712Z"
mitre_modified: "2024-12-10T16:29:44.429Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1040/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:

Suspicious Process Behavior:

- Implementation: Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behavior, such as privilege escalation attempts.
- Use Case: An attacker uses a known vulnerability to spawn a privileged process from a user-level application. The endpoint tool detects the abnormal parent-child process relationship and blocks the action.

Unauthorized File Access:

- Implementation: Leverage Data Loss Prevention (DLP) or endpoint tools to block processes attempting to access sensitive files without proper authorization.
- Use Case: A process tries to read or modify a sensitive file located in a restricted directory, such as /etc/shadow on Linux or the SAM registry hive on Windows. The endpoint tool identifies this anomalous behavior and prevents it.

Abnormal API Calls:

- Implementation: Implement runtime analysis tools to monitor API calls and block those associated with malicious activities.
- Use Case: A process dynamically injects itself into another process to hijack its execution. The endpoint detects the abnormal use of APIs like `OpenProcess` and `WriteProcessMemory` and terminates the offending process.

Exploit Prevention:

- Implementation: Use behavioral exploit prevention tools to detect and block exploits attempting to gain unauthorized access.
- Use Case: A buffer overflow exploit is launched against a vulnerable application. The endpoint detects the anomalous memory write operation and halts the process.

## Workspace

- [[workspaces/attack/mitigations/M1040-behavior_prevention_on_endpoint-note|Open workspace note]]

![[workspaces/attack/mitigations/M1040-behavior_prevention_on_endpoint-note]]

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1006-direct_volume_access|T1006: Direct Volume Access]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027009-embedded-payloads|T1027.009: Embedded Payloads]]
    - [[T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]
    - [[T1027-obfuscated_files_or_information#^t1027012-lnk-icon-smuggling|T1027.012: LNK Icon Smuggling]]
    - [[T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]
    - [[T1027-obfuscated_files_or_information#^t1027014-polymorphic-code|T1027.014: Polymorphic Code]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036008-masquerade-file-type|T1036.008: Masquerade File Type]]
- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection|T1055: Process Injection]]
    - [[T1055-process_injection#^t1055001-dynamic-link-library-injection|T1055.001: Dynamic-link Library Injection]]
    - [[T1055-process_injection#^t1055002-portable-executable-injection|T1055.002: Portable Executable Injection]]
    - [[T1055-process_injection#^t1055003-thread-execution-hijacking|T1055.003: Thread Execution Hijacking]]
    - [[T1055-process_injection#^t1055004-asynchronous-procedure-call|T1055.004: Asynchronous Procedure Call]]
    - [[T1055-process_injection#^t1055005-thread-local-storage|T1055.005: Thread Local Storage]]
    - [[T1055-process_injection#^t1055008-ptrace-system-calls|T1055.008: Ptrace System Calls]]
    - [[T1055-process_injection#^t1055009-proc-memory|T1055.009: Proc Memory]]
    - [[T1055-process_injection#^t1055011-extra-window-memory-injection|T1055.011: Extra Window Memory Injection]]
    - [[T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]
    - [[T1055-process_injection#^t1055013-process-doppelgänging|T1055.013: Process Doppelgänging]]
    - [[T1055-process_injection#^t1055014-vdso-hijacking|T1055.014: VDSO Hijacking]]
    - [[T1055-process_injection#^t1055015-listplanting|T1055.015: ListPlanting]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1106-native_api|T1106: Native API]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
    - [[T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]
    - [[T1137-office_application_startup#^t1137002-office-test|T1137.002: Office Test]]
    - [[T1137-office_application_startup#^t1137003-outlook-forms|T1137.003: Outlook Forms]]
    - [[T1137-office_application_startup#^t1137004-outlook-home-page|T1137.004: Outlook Home Page]]
    - [[T1137-office_application_startup#^t1137005-outlook-rules|T1137.005: Outlook Rules]]
    - [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
- [[T1216-system_script_proxy_execution|T1216: System Script Proxy Execution]]
    - [[T1216-system_script_proxy_execution#^t1216001-pubprn|T1216.001: PubPrn]]
- [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564014-extended-attributes|T1564.014: Extended Attributes]]
- [[T1569-system_services|T1569: System Services]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574013-kernelcallbacktable|T1574.013: KernelCallbackTable]]

