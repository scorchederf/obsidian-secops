---
sigma_id: "dff1e1cc-d3fd-47c8-bfc2-aeb878a754c0"
title: "Shell Process Spawned by Java.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_susp_child_process_2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_susp_child_process_2.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dff1e1cc-d3fd-47c8-bfc2-aeb878a754c0"
  - "Shell Process Spawned by Java.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Shell Process Spawned by Java.EXE

Detects shell spawned from Java host process, which could be a sign of exploitation (e.g. log4j exploitation)

## Metadata

- Rule ID: dff1e1cc-d3fd-47c8-bfc2-aeb878a754c0
- Status: test
- Level: medium
- Author: Andreas Hunkeler (@Karneades), Nasreddine Bencherchali
- Date: 2021-12-17
- Modified: 2024-01-18
- Source Path: rules/windows/process_creation/proc_creation_win_java_susp_child_process_2.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  ParentImage|endswith: \java.exe
  Image|endswith:
  - \bash.exe
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
filter_main_build:
  ParentImage|contains: build
  CommandLine|contains: build
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate calls to system binaries
- Company specific internal usage

## References

- https://web.archive.org/web/20231230220738/https://www.lunasec.io/docs/blog/log4j-zero-day/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_susp_child_process_2.yml)
