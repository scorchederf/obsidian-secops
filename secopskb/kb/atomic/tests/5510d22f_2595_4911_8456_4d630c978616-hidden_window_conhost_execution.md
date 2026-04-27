---
atomic_guid: "5510d22f-2595-4911-8456-4d630c978616"
title: "Hidden Window-Conhost Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.003"
attack_technique_name: "Hide Artifacts: Hidden Window"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "5510d22f-2595-4911-8456-4d630c978616"
  - "Hidden Window-Conhost Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Hidden Window-Conhost Execution

Launch conhost.exe in "headless" mode, it means that no visible window will pop up on the victim's machine. 
This could be a sign of "conhost" usage as a LOLBIN or potential process injection activity.
conhost.exe can be used as proxy the execution of arbitrary commands

## Metadata

- Atomic GUID: 5510d22f-2595-4911-8456-4d630c978616
- Technique: T1564.003: Hide Artifacts: Hidden Window
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1564.003/T1564.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
conhost.exe --headless calc.exe
```

### Cleanup

```powershell
Stop-Process -Name calc*
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml)
