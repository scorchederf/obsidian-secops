---
atomic_guid: "f3a6cceb-06c9-48e5-8df8-8867a6814245"
title: "Change Powershell Execution Policy to Bypass"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "f3a6cceb-06c9-48e5-8df8-8867a6814245"
  - "Change Powershell Execution Policy to Bypass"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Change Powershell Execution Policy to Bypass

Attackers need to change the powershell execution policy in order to run their malicious powershell scripts.
They can either specify it during the execution of the powershell script or change the registry value for it.

## Metadata

- Atomic GUID: f3a6cceb-06c9-48e5-8df8-8867a6814245
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### default_execution_policy

- description: Specify the default poweshell execution policy
- type: string
- default: Default

## Executor

- name: powershell

### Command

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine
```

### Cleanup

```powershell
try { Set-ExecutionPolicy -ExecutionPolicy #{default_execution_policy} -Scope LocalMachine -Force } catch {}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
