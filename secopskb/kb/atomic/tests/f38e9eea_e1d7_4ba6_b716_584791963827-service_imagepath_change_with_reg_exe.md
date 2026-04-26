---
atomic_guid: "f38e9eea-e1d7-4ba6-b716-584791963827"
title: "Service ImagePath Change with reg.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.011"
attack_technique_name: "Hijack Execution Flow: Services Registry Permissions Weakness"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.011/T1574.011.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "f38e9eea-e1d7-4ba6-b716-584791963827"
  - "Service ImagePath Change with reg.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Service ImagePath Change with reg.exe

Change Service registry ImagePath of a bengin service to a malicious file

## Metadata

- Atomic GUID: f38e9eea-e1d7-4ba6-b716-584791963827
- Technique: T1574.011: Hijack Execution Flow: Services Registry Permissions Weakness
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1574.011/T1574.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Input Arguments

### malicious_service_path

- description: malicious service path
- type: string
- default: %windir%\system32\cmd.exe

### weak_service_name

- description: weak service name
- type: string
- default: calcservice

### weak_service_path

- description: weak service path
- type: string
- default: %windir%\system32\win32calc.exe

## Dependencies

The service must exist (#{weak_service_name})

### Prerequisite Check

```text
if (Get-Service #{weak_service_name}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
sc.exe create #{weak_service_name} binpath= "#{weak_service_path}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
reg.exe add "HKLM\SYSTEM\CurrentControlSet\Services\#{weak_service_name}" /f /v ImagePath /d "#{malicious_service_path}"
```

### Cleanup

```commandprompt
sc.exe delete #{weak_service_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.011/T1574.011.yaml)
