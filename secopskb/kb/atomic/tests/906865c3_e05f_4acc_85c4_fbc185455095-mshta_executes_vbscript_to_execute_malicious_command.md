---
atomic_guid: "906865c3-e05f-4acc-85c4-fbc185455095"
title: "Mshta executes VBScript to execute malicious command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "906865c3-e05f-4acc-85c4-fbc185455095"
  - "Mshta executes VBScript to execute malicious command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mshta executes VBScript to execute malicious command

Run a local VB script to run local user enumeration powershell command.
This attempts to emulate what FIN7 does with this technique which is using mshta.exe to execute VBScript to execute malicious code on victim systems.
Upon execution, a new PowerShell windows will be opened that displays user information.

## Metadata

- Atomic GUID: 906865c3-e05f-4acc-85c4-fbc185455095
- Technique: T1218.005: Signed Binary Proxy Execution: Mshta
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.005/T1218.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Executor

- name: command_prompt

### Command

```commandprompt
mshta vbscript:Execute("CreateObject(""Wscript.Shell"").Run ""powershell -noexit -file PathToAtomicsFolder\T1218.005\src\powershell.ps1"":close")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
