---
atomic_guid: "6a3ff8dd-f49c-4272-a658-11c2fe58bd88"
title: "Windows - Delete Volume Shadow Copies via WMI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "6a3ff8dd-f49c-4272-a658-11c2fe58bd88"
  - "Windows - Delete Volume Shadow Copies via WMI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Delete Volume Shadow Copies via WMI

Deletes Windows Volume Shadow Copies via WMI. This technique is used by numerous ransomware families and APT malware such as Olympic Destroyer.

## Metadata

- Atomic GUID: 6a3ff8dd-f49c-4272-a658-11c2fe58bd88
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Dependencies

Create volume shadow copy of C:\ .

### Prerequisite Check

```text
if(!(vssadmin.exe list shadows | findstr "No items found that satisfy the query.")) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
wmic shadowcopy call create Volume='C:\'
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
wmic.exe shadowcopy delete
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
