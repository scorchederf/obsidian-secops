---
id: T1559
name: Inter-Process Communication
created: 2020-02-12 14:08:48.689000+00:00
modified: 2025-10-24 17:49:13.194000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern. 

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows [Dynamic Data Exchange](https://attack.mitre.org/techniques/T1559/002) or [Component Object Model](https://attack.mitre.org/techniques/T1559/001). Linux environments support several different IPC mechanisms, two of which being sockets and pipes.(Citation: Linux IPC) Higher level execution mediums, such as those of [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)s, may also leverage underlying IPC mechanisms. Adversaries may also use [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) to facilitate remote IPC execution.(Citation: Fireeye Hunting COM June 2019)

## Subtechniques

### T1559.001: Component Object Model
^t1559001-component-object-model

**Parent Technique**
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]

**Tactic**
- [[execution|Execution]]

Adversaries may use the Windows Component Object Model (COM) for local code execution. COM is an inter-process communication (IPC) component of the native Windows application programming interface (API) that enables interaction between software objects, or executable code that implements one or more interfaces.(Citation: Fireeye Hunting COM June 2019) Through COM, a client object can call methods of server objects, which are typically binary Dynamic Link Libraries (DLL) or executables (EXE).(Citation: Microsoft COM) Remote COM execution is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021) such as  [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) (DCOM).(Citation: Fireeye Hunting COM June 2019)

Various COM interfaces are exposed that can be abused to invoke arbitrary execution via a variety of programming languages such as C, C++, Java, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005).(Citation: Microsoft COM) Specific COM objects also exist to directly perform functions beyond code execution, such as creating a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053), fileless download/execution, and other adversary behaviors related to privilege escalation and persistence.(Citation: Fireeye Hunting COM June 2019)(Citation: ProjectZero File Write EoP Apr 2018)

#### Properties

- id: T1559.001
- name: Component Object Model
- created: 2020-02-12 14:09:53.107000+00:00
- modified: 2025-10-24 17:48:35.814000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1559.002: Dynamic Data Exchange
^t1559002-dynamic-data-exchange

**Parent Technique**
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]

**Tactic**
- [[execution|Execution]]

Adversaries may use Windows Dynamic Data Exchange (DDE) to execute arbitrary commands. DDE is a client-server protocol for one-time and/or continuous inter-process communication (IPC) between applications. Once a link is established, applications can autonomously exchange transactions consisting of strings, warm data links (notifications when a data item changes), hot data links (duplications of changes to a data item), and requests for command execution.

Object Linking and Embedding (OLE), or the ability to link data between documents, was originally implemented through DDE. Despite being superseded by [Component Object Model](https://attack.mitre.org/techniques/T1559/001), DDE may be enabled in Windows 10 and most of Microsoft Office 2016 via Registry keys.(Citation: BleepingComputer DDE Disabled in Word Dec 2017)(Citation: Microsoft ADV170021 Dec 2017)(Citation: Microsoft DDE Advisory Nov 2017)

Microsoft Office documents can be poisoned with DDE commands, directly or through embedded files, and used to deliver execution via [Phishing](https://attack.mitre.org/techniques/T1566) campaigns or hosted Web content, avoiding the use of Visual Basic for Applications (VBA) macros.(Citation: SensePost PS DDE May 2016)(Citation: Kettle CSV DDE Aug 2014)(Citation: Enigma Reviving DDE Jan 2018)(Citation: SensePost MacroLess DDE Oct 2017) Similarly, adversaries may infect payloads to execute applications and/or commands on a victim device by way of embedding DDE formulas within a CSV file intended to be opened through a Windows spreadsheet program.(Citation: OWASP CSV Injection)(Citation: CSV Excel Macro Injection )

DDE could also be leveraged by an adversary operating on a compromised machine who does not have direct access to a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). DDE execution can be invoked remotely via [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) (DCOM).(Citation: Fireeye Hunting COM June 2019)

#### Properties

- id: T1559.002
- name: Dynamic Data Exchange
- created: 2020-02-12 14:10:50.699000+00:00
- modified: 2025-10-24 17:48:31.581000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

### T1559.003: XPC Services
^t1559003-xpc-services

**Parent Technique**
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]

**Tactic**
- [[execution|Execution]]

Adversaries can provide malicious content to an XPC service daemon for local code execution. macOS uses XPC services for basic inter-process communication between various processes, such as between the XPC Service daemon and third-party application privileged helper tools. Applications can send messages to the XPC Service daemon, which runs as root, using the low-level XPC Service <code>C API</code> or the high level <code>NSXPCConnection API</code> in order to handle tasks that require elevated privileges (such as network connections). Applications are responsible for providing the protocol definition which serves as a blueprint of the XPC services. Developers typically use XPC Services to provide applications stability and privilege separation between the application client and the daemon.(Citation: creatingXPCservices)(Citation: Designing Daemons Apple Dev)

Adversaries can abuse XPC services to execute malicious content. Requests for malicious execution can be passed through the application's XPC Services handler.(Citation: CVMServer Vuln)(Citation: Learn XPC Exploitation) This may also include identifying and abusing improper XPC client validation and/or poor sanitization of input parameters to conduct [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).

#### Properties

- id: T1559.003
- name: XPC Services
- created: 2021-10-12 06:45:36.763000+00:00
- modified: 2025-04-15 19:58:47.031000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

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

## Tools


