---
atomic_guid: "f723d13d-48dc-4317-9990-cf43a9ac0bf2"
title: "Clears Recycle bin via rd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "f723d13d-48dc-4317-9990-cf43a9ac0bf2"
  - "Clears Recycle bin via rd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clears Recycle bin via rd

An adversary clears the recycle bin in the system partition using rd to remove traces of deleted files.
[Reference](https://thedfirreport.com/2024/08/12/threat-actors-toolkit-leveraging-sliver-poshc2-batch-scripts/)

## Metadata

- Atomic GUID: f723d13d-48dc-4317-9990-cf43a9ac0bf2
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
rd /s /q %systemdrive%\$RECYCLE.BIN
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
