---
atomic_guid: "8a4c33be-a0d3-434a-bee6-315405edbd5b"
title: "Disable .NET Event Tracing for Windows Via Registry (cmd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "8a4c33be-a0d3-434a-bee6-315405edbd5b"
  - "Disable .NET Event Tracing for Windows Via Registry (cmd)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable .NET Event Tracing for Windows Via Registry (cmd)

Disables ETW for the .NET Framework using the reg.exe utility to update the Windows registry

## Metadata

- Atomic GUID: 8a4c33be-a0d3-434a-bee6-315405edbd5b
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
REG ADD HKLM\Software\Microsoft\.NETFramework /v ETWEnabled /t REG_DWORD /d 0
```

### Cleanup

```cmd
REG DELETE HKLM\Software\Microsoft\.NETFramework /v ETWEnabled /f > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
