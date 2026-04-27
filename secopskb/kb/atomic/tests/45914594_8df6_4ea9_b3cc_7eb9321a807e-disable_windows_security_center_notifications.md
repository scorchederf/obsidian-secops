---
atomic_guid: "45914594-8df6-4ea9-b3cc-7eb9321a807e"
title: "Disable Windows Security Center Notifications"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "45914594-8df6-4ea9-b3cc-7eb9321a807e"
  - "Disable Windows Security Center Notifications"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Windows Security Center Notifications

Modify the registry of the currently logged in user using reg.exe via cmd console to disable the windows security center notification.
See how azorult malware abuses this technique- https://app.any.run/tasks/a6f2ffe2-e6e2-4396-ae2e-04ea0143f2d8/

## Metadata

- Atomic GUID: 45914594-8df6-4ea9-b3cc-7eb9321a807e
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

```cmd
reg add HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\ImmersiveShell /v UseActionCenterExperience /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\ImmersiveShell /v UseActionCenterExperience /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
