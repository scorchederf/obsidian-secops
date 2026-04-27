---
atomic_guid: "0fd14730-6226-4f5e-8d67-43c65f1be940"
title: "Indirect Command Execution - Scriptrunner.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1202"
attack_technique_name: "Indirect Command Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0fd14730-6226-4f5e-8d67-43c65f1be940"
  - "Indirect Command Execution - Scriptrunner.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Indirect Command Execution - Scriptrunner.exe

The "ScriptRunner.exe" binary can be abused to proxy execution through it and bypass possible whitelisting. Upon test execution, calc.exe should open
Reference: https://x.com/NickTyrer/status/914234924655312896

## Metadata

- Atomic GUID: 0fd14730-6226-4f5e-8d67-43c65f1be940
- Technique: T1202: Indirect Command Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1202/T1202.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Input Arguments

### payload_path

- description: Path to the executable
- type: String
- default: C:\Windows\System32\calc.exe

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Scriptrunner.exe -appvscript "#{payload_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml)
