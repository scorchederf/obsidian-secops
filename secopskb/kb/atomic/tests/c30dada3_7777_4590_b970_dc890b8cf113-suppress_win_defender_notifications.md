---
atomic_guid: "c30dada3-7777-4590-b970-dc890b8cf113"
title: "Suppress Win Defender Notifications"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "c30dada3-7777-4590-b970-dc890b8cf113"
  - "Suppress Win Defender Notifications"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suppress Win Defender Notifications

Modify the registry of the currently logged in user using reg.exe via cmd console to suppress the windows defender notification.
See how azorult malware abuses this technique- https://app.any.run/tasks/a6f2ffe2-e6e2-4396-ae2e-04ea0143f2d8/

## Metadata

- Atomic GUID: c30dada3-7777-4590-b970-dc890b8cf113
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\UX Configuration" /v Notification_Suppress /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\UX Configuration" /v Notification_Suppress /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
