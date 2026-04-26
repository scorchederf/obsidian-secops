---
atomic_guid: "69f50a5f-967c-4327-a5bb-e1a9a9983785"
title: "Delete TeamViewer Log Files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "69f50a5f-967c-4327-a5bb-e1a9a9983785"
  - "Delete TeamViewer Log Files"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete TeamViewer Log Files

Adversaries may delete TeamViewer log files to hide activity. This should provide a high true-positive alert ration.
This test just places the files in a non-TeamViewer folder, a detection would just check for a deletion event matching the TeamViewer
log file format of TeamViewer_##.log. Upon execution, no output will be displayed. Use File Explorer to verify the folder was deleted.

https://twitter.com/SBousseaden/status/1197524463304290305?s=20

## Metadata

- Atomic GUID: 69f50a5f-967c-4327-a5bb-e1a9a9983785
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Input Arguments

### teamviewer_log_file

- description: Teamviewer log file to create and delete.
- type: string
- default: $env:TEMP\TeamViewer_54.log

## Executor

- name: powershell

### Command

```powershell
New-Item -Path #{teamviewer_log_file} -Force | Out-Null
Remove-Item #{teamviewer_log_file} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
