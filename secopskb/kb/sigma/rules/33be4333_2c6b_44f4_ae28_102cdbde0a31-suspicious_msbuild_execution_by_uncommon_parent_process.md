---
sigma_id: "33be4333-2c6b-44f4-ae28-102cdbde0a31"
title: "Suspicious Msbuild Execution By Uncommon Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "33be4333-2c6b-44f4-ae28-102cdbde0a31"
  - "Suspicious Msbuild Execution By Uncommon Parent Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Msbuild Execution By Uncommon Parent Process

Detects suspicious execution of 'Msbuild.exe' by a uncommon parent process

## Metadata

- Rule ID: 33be4333-2c6b-44f4-ae28-102cdbde0a31
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-11-17
- Source Path: rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith: \MSBuild.exe
- OriginalFileName: MSBuild.exe
filter_parent:
  ParentImage|endswith:
  - \devenv.exe
  - \cmd.exe
  - \msbuild.exe
  - \python.exe
  - \explorer.exe
  - \nuget.exe
condition: selection and not filter_parent
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/abdf586e-df0c-4d39-89a7-06bf24913401/
- https://www.echotrail.io/insights/search/msbuild.exe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml)
