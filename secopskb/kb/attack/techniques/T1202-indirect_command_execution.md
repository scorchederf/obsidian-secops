---
mitre_id: "T1202"
mitre_name: "Indirect Command Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3b0e52ce-517a-4614-a523-1bd5deef6c5e"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:40.495Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1202/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking [[cmd|cmd (S0106)]]. For example, [[forfiles|Forfiles (S0193)]], the Program Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well as other utilities may invoke the execution of programs and commands from a [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]], Run window, or via scripts.(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)(Citation: Secure Team - Scriptrunner.exe)(Citation: SS64)(Citation: Bleeping Computer - Scriptrunner.exe) Adversaries may also abuse the `ssh.exe` binary to execute malicious commands via the `ProxyCommand` and `LocalCommand` options, which can be invoked via the `-o` flag or by modifying the SSH config file.(Citation: Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot)

Adversaries may abuse these features for [[TA0005-defense_evasion|TA0005: Defense Evasion]], specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of [[cmd|cmd (S0106)]] or file extensions more commonly associated with malicious payloads.

## Workspace

- [[workspaces/attack/techniques/T1202-indirect_command_execution-note|Open workspace note]]

![[workspaces/attack/techniques/T1202-indirect_command_execution-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Tools

- [[forfiles|Forfiles (S0193)]]

## Platforms

- Windows

