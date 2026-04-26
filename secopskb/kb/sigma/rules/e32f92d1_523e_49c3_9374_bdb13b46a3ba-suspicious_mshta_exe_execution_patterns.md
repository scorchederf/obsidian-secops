---
sigma_id: "e32f92d1-523e-49c3-9374-bdb13b46a3ba"
title: "Suspicious Mshta.EXE Execution Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e32f92d1-523e-49c3-9374-bdb13b46a3ba"
  - "Suspicious Mshta.EXE Execution Patterns"
attack_technique_ids:
  - "T1106"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Mshta.EXE Execution Patterns

Detects suspicious mshta process execution patterns

## Metadata

- Rule ID: e32f92d1-523e-49c3-9374-bdb13b46a3ba
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-07-17
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]

## Detection

```yaml
selection_img:
- Image|endswith: \mshta.exe
- OriginalFileName: MSHTA.EXE
selection_susp:
  ParentImage|endswith:
  - \cmd.exe
  - \cscript.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
  CommandLine|contains:
  - \AppData\Local\
  - C:\ProgramData\
  - C:\Users\Public\
  - C:\Windows\Temp\
filter_img:
- Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
- CommandLine|contains:
  - .htm
  - .hta
- CommandLine|endswith:
  - mshta.exe
  - mshta
condition: all of selection_* or (selection_img and not filter_img)
```

## False Positives

- Unknown

## References

- https://en.wikipedia.org/wiki/HTML_Application
- https://www.echotrail.io/insights/search/mshta.exe
- https://app.any.run/tasks/34221348-072d-4b70-93f3-aa71f6ebecad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_pattern.yml)
