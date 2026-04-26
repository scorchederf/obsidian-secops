---
atomic_guid: "1c68c68d-83a4-4981-974e-8993055fa034"
title: "Windows - Disable the SR scheduled task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "1c68c68d-83a4-4981-974e-8993055fa034"
  - "Windows - Disable the SR scheduled task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Disable the SR scheduled task

Use schtasks.exe to disable the System Restore (SR) scheduled task

## Metadata

- Atomic GUID: 1c68c68d-83a4-4981-974e-8993055fa034
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
schtasks.exe /Change /TN "\Microsoft\Windows\SystemRestore\SR" /disable
```

### Cleanup

```cmd
schtasks.exe /Change /TN "\Microsoft\Windows\SystemRestore\SR" /enable >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
