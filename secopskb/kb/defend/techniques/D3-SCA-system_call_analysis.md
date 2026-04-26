---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SCA"
d3fend_name: "System Call Analysis"
d3fend_ontology_id: "d3f:SystemCallAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemCallAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
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
  - "T1518"
  - "T1518.001"
  - "T1546"
  - "T1546.009"
  - "T1546.010"
  - "T1548"
  - "T1548.002"
  - "T1548.004"
  - "T1555"
  - "T1555.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Analyzing system calls to determine whether a process is exhibiting unauthorized behavior.

## Workspace

- [[workspaces/defend/techniques/D3-SCA-system_call_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SCA-system_call_analysis-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Child Techniques

- [[D3-FCA-file_creation_analysis|D3-FCA: File Creation Analysis]]

## Related ATT&CK Techniques

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
- [[T1518-software_discovery|T1518: Software Discovery]]
- [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546009-appcert-dlls|T1546.009: AppCert DLLs]]
- [[T1546-event_triggered_execution#^t1546010-appinit-dlls|T1546.010: AppInit DLLs]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1548-abuse_elevation_control_mechanism#^t1548004-elevated-execution-with-prompt|T1548.004: Elevated Execution with Prompt]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

## Knowledge Base Article

## How it works

System calls are APIs between a user application and the operating system [1].

By analyzing a process's use of these APIs, it is, in some cases, possible to ascertain whether a program is exhibiting unauthorized behavior, including trying to escalate its privileges.

### Gathering System Calls
A common method to capture system calls is to use kernel APIs to hook [2] a process's system call invocations.

The Linux system call `ptrace` tracks other system calls in a process and allows their alteration; this is made use of by GDB.  `strace` utilizes `ptrace` and will print to stdout each system call invoked. Other applications record this data in local or remote databases.

The log entry for each system call, which may reference additional information such as the date and time, and the process tree for the process which made the system call, is relayed, in real time or post-facto, to an analysis module which consults a catalog or model to determine whether the distribution matches a known-good or known-bad pattern.


### Analysis

System calls are analyzed with a variety of methods. Some analytics look for specific sequences of instructions, others may apply statistical methods to identify abnormal behavior. Sequences of instructions can be abstracted into conceptually higher order user activities, for example:

* An attacker executes many system calls in a short period of time, with several sequences which could be used to escalate privileges.
* Getting the contents from a URL, writing to a new file, and then executing the same file.
* A ransomware program which either uses a loop or creates many threads to: read a specified file, encrypt its contents, create an output file with a similar name to the original file, and delete the unencrypted original.

## Considerations

* Duplicative or extraneous system calls may be added to malware to defeat analytics.
* Malware could replace API hooking instructions to allow system calls to be made without being monitored.
* A model built from a training set of system calls and related data may not be updated fast enough to detect new threats.


[1] [Syscalls](http://man7.org/linux/man-pages/man2/syscalls.2.html)

[2] [Hooking](http://dbpedia.org/resource/Hooking)

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

