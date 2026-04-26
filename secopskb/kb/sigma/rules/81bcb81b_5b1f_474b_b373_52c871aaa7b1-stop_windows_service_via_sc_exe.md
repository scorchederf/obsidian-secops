---
sigma_id: "81bcb81b-5b1f-474b-b373-52c871aaa7b1"
title: "Stop Windows Service Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_stop_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_stop_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "81bcb81b-5b1f-474b-b373-52c871aaa7b1"
  - "Stop Windows Service Via Sc.EXE"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Stop Windows Service Via Sc.EXE

Detects the stopping of a Windows service via the "sc.exe" utility

## Metadata

- Rule ID: 81bcb81b-5b1f-474b-b373-52c871aaa7b1
- Status: test
- Level: low
- Author: Jakob Weinzettl, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-05
- Modified: 2024-01-18
- Source Path: rules/windows/process_creation/proc_creation_win_sc_stop_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection_img:
- OriginalFileName: sc.exe
- Image|endswith: \sc.exe
selection_cli:
  CommandLine|contains: ' stop '
condition: all of selection_*
```

## False Positives

- There are many legitimate reasons to stop a service. This rule isn't looking for any suspicious behavior in particular. Filter legitimate activity accordingly

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc742107(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_stop_service.yml)
