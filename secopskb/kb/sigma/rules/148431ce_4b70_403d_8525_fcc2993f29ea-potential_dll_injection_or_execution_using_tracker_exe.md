---
sigma_id: "148431ce-4b70-403d-8525-fcc2993f29ea"
title: "Potential DLL Injection Or Execution Using Tracker.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "148431ce-4b70-403d-8525-fcc2993f29ea"
  - "Potential DLL Injection Or Execution Using Tracker.exe"
attack_technique_ids:
  - "T1055.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Injection Or Execution Using Tracker.exe

Detects potential DLL injection and execution using "Tracker.exe"

## Metadata

- Rule ID: 148431ce-4b70-403d-8525-fcc2993f29ea
- Status: test
- Level: medium
- Author: Avneet Singh @v3t0_, oscd.community
- Date: 2020-10-18
- Modified: 2023-01-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \tracker.exe
- Description: Tracker
selection_cli:
  CommandLine|contains:
  - ' /d '
  - ' /c '
filter_msbuild1:
  CommandLine|contains: ' /ERRORREPORT:PROMPT '
filter_msbuild2:
  ParentImage|endswith:
  - \Msbuild\Current\Bin\MSBuild.exe
  - \Msbuild\Current\Bin\amd64\MSBuild.exe
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tracker/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml)
