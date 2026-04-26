---
atomic_guid: "12e03af7-79f9-4f95-af48-d3f12f28a260"
title: "Disable Win Defender Notification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "12e03af7-79f9-4f95-af48-d3f12f28a260"
  - "Disable Win Defender Notification"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Win Defender Notification

Disable Win Defender Notification. Redline is using this to disable this win defender feature.

## Metadata

- Atomic GUID: 12e03af7-79f9-4f95-af48-d3f12f28a260
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
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" /v "DisableNotifications" /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications" /v "DisableNotifications" /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
