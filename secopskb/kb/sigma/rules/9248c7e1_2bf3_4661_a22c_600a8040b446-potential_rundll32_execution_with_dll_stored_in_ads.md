---
sigma_id: "9248c7e1-2bf3-4661-a22c-600a8040b446"
title: "Potential Rundll32 Execution With DLL Stored In ADS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_ads_stored_dll_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_ads_stored_dll_execution.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9248c7e1-2bf3-4661-a22c-600a8040b446"
  - "Potential Rundll32 Execution With DLL Stored In ADS"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Rundll32 Execution With DLL Stored In ADS

Detects execution of rundll32 where the DLL being called is stored in an Alternate Data Stream (ADS).

## Metadata

- Rule ID: 9248c7e1-2bf3-4661-a22c-600a8040b446
- Status: test
- Level: high
- Author: Harjot Singh, '@cyb3rjy0t'
- Date: 2023-01-21
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_ads_stored_dll_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|re: '[Rr][Uu][Nn][Dd][Ll][Ll]32(\.[Ee][Xx][Ee])? \S+?\w:\S+?:'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Rundll32

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_ads_stored_dll_execution.yml)
