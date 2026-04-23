---
mitre_id: "T1622"
mitre_name: "Debugger Evasion"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e4dc8c01-417f-458d-9ee0-bb0617c1b391"
mitre_created: "2022-04-01T17:59:46.156Z"
mitre_modified: "2025-10-24T17:49:32.196Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1622/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0007"
---

# T1622: Debugger Evasion

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads.(Citation: ProcessHacker Github)

Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]], if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.

Specific checks will vary based on the target and/or adversary. On Windows, this may involve [[T1106-native_api|T1106: Native API]] function calls such as `IsDebuggerPresent()` and `NtQueryInformationProcess()`, or manually checking the `BeingDebugged` flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status` for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools.(Citation: Cado Security P2PInfect 2023)(Citation: Positive Technologies Hellhounds 2023) Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would “swallow” or handle the potential error).(Citation: hasherezade debug)(Citation: AlKhaser Debug)(Citation: vxunderground debug)

Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue.(Citation: Apriorit)

Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping [[T1106-native_api|T1106: Native API]] function calls such as `OutputDebugStringW()`.(Citation: wardle evilquest partii)(Citation: Checkpoint Dridex Jan 2021)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[asyncrat|AsyncRAT]]

## Platforms

- Linux
- macOS
- Windows

