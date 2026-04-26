---
sigma_id: "85c312b7-f44d-4a51-a024-d671c40b49fc"
title: "Service StartupType Change Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_disable_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_disable_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "85c312b7-f44d-4a51-a024-d671c40b49fc"
  - "Service StartupType Change Via Sc.EXE"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service StartupType Change Via Sc.EXE

Detect the use of "sc.exe" to change the startup type of a service to "disabled" or "demand"

## Metadata

- Rule ID: 85c312b7-f44d-4a51-a024-d671c40b49fc
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2023-03-04
- Source Path: rules/windows/process_creation/proc_creation_win_sc_disable_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_cli:
  CommandLine|contains|all:
  - ' config '
  - start
  CommandLine|contains:
  - disabled
  - demand
condition: all of selection_*
```

## False Positives

- False positives may occur with troubleshooting scripts

## References

- https://www.virustotal.com/gui/file/38283b775552da8981452941ea74191aa0d203edd3f61fb2dee7b0aea3514955

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_disable_service.yml)
