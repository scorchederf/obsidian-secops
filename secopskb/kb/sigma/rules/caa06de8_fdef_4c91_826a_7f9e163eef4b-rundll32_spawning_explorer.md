---
sigma_id: "caa06de8-fdef-4c91-826a-7f9e163eef4b"
title: "RunDLL32 Spawning Explorer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_spawn_explorer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_spawn_explorer.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "caa06de8-fdef-4c91-826a-7f9e163eef4b"
  - "RunDLL32 Spawning Explorer"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# RunDLL32 Spawning Explorer

Detects RunDLL32.exe spawning explorer.exe as child, which is very uncommon, often observes Gamarue spawning the explorer.exe process in an unusual way

## Metadata

- Rule ID: caa06de8-fdef-4c91-826a-7f9e163eef4b
- Status: test
- Level: high
- Author: elhoim, CD_ROM_
- Date: 2022-04-27
- Modified: 2022-05-25
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_spawn_explorer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  ParentImage|endswith: \rundll32.exe
  Image|endswith: \explorer.exe
filter:
  ParentCommandLine|contains: \shell32.dll,Control_RunDLL
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/intelligence-insights-november-2021/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_spawn_explorer.yml)
