---
sigma_id: "88872991-7445-4a22-90b2-a3adadb0e827"
title: "Stop Windows Service Via Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_stop_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_stop_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "88872991-7445-4a22-90b2-a3adadb0e827"
  - "Stop Windows Service Via Net.EXE"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Stop Windows Service Via Net.EXE

Detects the stopping of a Windows service via the "net" utility.

## Metadata

- Rule ID: 88872991-7445-4a22-90b2-a3adadb0e827
- Status: test
- Level: low
- Author: Jakob Weinzettl, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_net_stop_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection_img:
- OriginalFileName:
  - net.exe
  - net1.exe
- Image|endswith:
  - \net.exe
  - \net1.exe
selection_cli:
  CommandLine|contains: ' stop '
condition: all of selection_*
```

## False Positives

- There are many legitimate reasons to stop a service. This rule isn't looking for any suspicious behaviour in particular. Filter legitimate activity accordingly

## References

- https://ss64.com/nt/net-service.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_stop_service.yml)
