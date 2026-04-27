---
atomic_guid: "611b39b7-e243-4c81-87a4-7145a90358b1"
title: "Process Injection via C#"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055.004"
attack_technique_name: "Process Injection: Asynchronous Procedure Call"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "611b39b7-e243-4c81-87a4-7145a90358b1"
  - "Process Injection via C#"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Injection via C#

Process Injection using C#
reference: https://github.com/pwndizzle/c-sharp-memory-injection
Excercises Five Techniques
1. Process injection
2. ApcInjectionAnyProcess
3. ApcInjectionNewProcess
4. IatInjection
5. ThreadHijack
Upon successful execution, cmd.exe will execute T1055.exe, which exercises 5 techniques. Output will be via stdout.

## Metadata

- Atomic GUID: 611b39b7-e243-4c81-87a4-7145a90358b1
- Technique: T1055.004: Process Injection: Asynchronous Procedure Call
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1055.004/T1055.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055.004]]

## Input Arguments

### exe_binary

- description: Output Binary
- type: path
- default: PathToAtomicsFolder\T1055.004\bin\T1055.exe

## Dependencies

#{exe_binary} must be exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{exe_binary}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{exe_binary}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055.004/bin/T1055.exe" -OutFile "#{exe_binary}"
```

## Executor

- name: command_prompt

### Command

```cmd
"#{exe_binary}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055.004/T1055.004.yaml)
