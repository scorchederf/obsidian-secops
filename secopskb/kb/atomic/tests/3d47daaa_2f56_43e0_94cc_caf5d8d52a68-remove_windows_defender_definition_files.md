---
atomic_guid: "3d47daaa-2f56-43e0-94cc-caf5d8d52a68"
title: "Remove Windows Defender Definition Files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "3d47daaa-2f56-43e0-94cc-caf5d8d52a68"
  - "Remove Windows Defender Definition Files"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remove Windows Defender Definition Files

Removing definition files would cause ATP to not fire for AntiMalware. Check MpCmdRun.exe man page for info on all arguments.
On later viersions of windows (1909+) this command fails even with admin due to inusfficient privelages. On older versions of windows the
command will say completed.

https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/

## Metadata

- Atomic GUID: 3d47daaa-2f56-43e0-94cc-caf5d8d52a68
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
