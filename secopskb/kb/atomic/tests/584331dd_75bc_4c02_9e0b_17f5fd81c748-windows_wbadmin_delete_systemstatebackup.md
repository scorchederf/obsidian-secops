---
atomic_guid: "584331dd-75bc-4c02-9e0b-17f5fd81c748"
title: "Windows - wbadmin Delete systemstatebackup"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "584331dd-75bc-4c02-9e0b-17f5fd81c748"
  - "Windows - wbadmin Delete systemstatebackup"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - wbadmin Delete systemstatebackup

Deletes the Windows systemstatebackup using wbadmin.exe. This technique is used by numerous ransomware families. This may only be successful on server platforms that have Windows Backup enabled.

## Metadata

- Atomic GUID: 584331dd-75bc-4c02-9e0b-17f5fd81c748
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

```commandprompt
wbadmin delete systemstatebackup -keepVersions:0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
