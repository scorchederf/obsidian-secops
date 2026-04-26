---
mitre_id: "T1559"
mitre_name: "Inter-Process Communication"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--acd0ba37-7ba9-4cc5-ac61-796586cd856d"
mitre_created: "2020-02-12T14:08:48.689Z"
mitre_modified: "2025-10-24T17:49:13.194Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1559/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]] or [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]]. Linux environments support several different IPC mechanisms, two of which being sockets and pipes.(Citation: Linux IPC) Higher level execution mediums, such as those of [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]s, may also leverage underlying IPC mechanisms. Adversaries may also use [[T1021-remote_services|T1021: Remote Services]] such as [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]] to facilitate remote IPC execution.(Citation: Fireeye Hunting COM June 2019)

## Workspace

- [[workspaces/attack/techniques/T1559-inter-process_communication-note|Open workspace note]]

![[workspaces/attack/techniques/T1559-inter-process_communication-note]]

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Subtechniques

### T1559.001: Component Object Model

^t1559001-component-object-model

Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces.(Citation: Fireeye Hunting COM June 2019) Through COM, a client object can call methods of server objects, which are typically binary Dynamic Link Libraries (DLL) or executables (EXE).(Citation: Microsoft COM) Remote COM execution is facilitated by [[T1021-remote_services|T1021: Remote Services]] such as  [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]] (DCOM).(Citation: Fireeye Hunting COM June 2019)

Various COM interfaces are exposed that can be abused to invoke arbitrary execution via a variety of programming languages such as C, C++, Java, and [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]].(Citation: Microsoft COM) Specific COM objects also exist to directly perform functions beyond code execution, such as creating a [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]], fileless download/execution, and other adversary behaviors related to privilege escalation and persistence.(Citation: Fireeye Hunting COM June 2019)(Citation: ProjectZero File Write EoP Apr 2018)

### T1559.002: Dynamic Data Exchange

^t1559002-dynamic-data-exchange

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.

Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]], DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys.(Citation: BleepingComputer DDE Disabled in Word Dec 2017)(Citation: Microsoft ADV170021 Dec 2017)(Citation: Microsoft DDE Advisory Nov 2017)

Microsoft Office documents can be poisoned with DDE commands, directly or through embedded files, and used to deliver execution via [[T1566-phishing|T1566: Phishing]] campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros.(Citation: SensePost PS DDE May 2016)(Citation: Kettle CSV DDE Aug 2014)(Citation: Enigma Reviving DDE Jan 2018)(Citation: SensePost MacroLess DDE Oct 2017) Similarly, adversaries may infect payloads to execute applications and/or commands on a victim device by way of embedding DDE formulas within a CSV file intended to be opened through a Windows spreadsheet program.(Citation: OWASP CSV Injection)(Citation: CSV Excel Macro Injection )

DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]. DDE execution can be invoked remotely via [[T1021-remote_services|T1021: Remote Services]] such as [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]] (DCOM).(Citation: Fireeye Hunting COM June 2019)

### T1559.003: XPC Services

^t1559003-xpc-services

Adversaries can provide malicious content to an XPC service daemon for local code execution. macOS uses XPC services for basic inter-process communication between various processes, such as between the XPC Service daemon and third-party application privileged helper tools. Applications can send messages to the XPC Service daemon, which runs as root, using the low-level XPC Service `C API` or the high level `NSXPCConnection API` in order to handle tasks that require elevated privileges (such as network connections). Applications are responsible for providing the protocol definition which serves as a blueprint of the XPC services. Developers typically use XPC Services to provide applications stability and privilege separation between the application client and the daemon.(Citation: creatingXPCservices)(Citation: Designing Daemons Apple Dev)

Adversaries can abuse XPC services to execute malicious content. Requests for malicious execution can be passed through the application's XPC Services handler.(Citation: CVMServer Vuln)(Citation: Learn XPC Exploitation) This may also include identifying and abusing improper XPC client validation and/or poor sanitization of input parameters to conduct [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]].

## Mitigations

- [[M1013-application_developer_guidance|M1013: Application Developer Guidance]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1048-application_isolation_and_sandboxing|M1048: Application Isolation and Sandboxing]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Linux
- macOS
- Windows

