---
atomic_guid: "263ba6cb-ea2b-41c9-9d4e-b652dadd002c"
title: "Windows - wbadmin Delete Windows Backup Catalog"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "263ba6cb-ea2b-41c9-9d4e-b652dadd002c"
  - "Windows - wbadmin Delete Windows Backup Catalog"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - wbadmin Delete Windows Backup Catalog

Deletes Windows Backup Catalog. This technique is used by numerous ransomware families and APT malware such as Olympic Destroyer. Upon execution,
"The backup catalog has been successfully deleted." will be displayed in the PowerShell session.

## Metadata

- Atomic GUID: 263ba6cb-ea2b-41c9-9d4e-b652dadd002c
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
wbadmin delete catalog -quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
