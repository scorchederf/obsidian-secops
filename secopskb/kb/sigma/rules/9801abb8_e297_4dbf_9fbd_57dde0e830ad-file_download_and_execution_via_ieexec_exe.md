---
sigma_id: "9801abb8-e297-4dbf-9fbd-57dde0e830ad"
title: "File Download And Execution Via IEExec.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ieexec_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ieexec_download.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9801abb8-e297-4dbf-9fbd-57dde0e830ad"
  - "File Download And Execution Via IEExec.EXE"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Download And Execution Via IEExec.EXE

Detects execution of the IEExec utility to download and execute files

## Metadata

- Rule ID: 9801abb8-e297-4dbf-9fbd-57dde0e830ad
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-16
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_ieexec_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith: \IEExec.exe
- OriginalFileName: IEExec.exe
selection_cli:
  CommandLine|contains:
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ieexec/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ieexec_download.yml)
