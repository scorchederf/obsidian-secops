---
sigma_id: "b0ce780f-10bd-496d-9067-066d23dc3aa5"
title: "HackTool - SharpWSUS/WSUSpendu Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpwsus_wsuspendu_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpwsus_wsuspendu_execution.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b0ce780f-10bd-496d-9067-066d23dc3aa5"
  - "HackTool - SharpWSUS/WSUSpendu Execution"
attack_technique_ids:
  - "T1210"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - SharpWSUS/WSUSpendu Execution

Detects the execution of SharpWSUS or WSUSpendu, utilities that allow for lateral movement through WSUS.
Windows Server Update Services (WSUS) is a critical component of Windows systems and is frequently configured in a way that allows an attacker to circumvent internal networking limitations.

## Metadata

- Rule ID: b0ce780f-10bd-496d-9067-066d23dc3aa5
- Status: test
- Level: high
- Author: @Kostastsale, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-07
- Modified: 2024-08-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpwsus_wsuspendu_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210]]

## Detection

```yaml
selection_wsuspendu_inject:
  CommandLine|contains: ' -Inject '
selection_wsuspendu_payload:
  CommandLine|contains:
  - ' -PayloadArgs '
  - ' -PayloadFile '
selection_sharpwsus_commands:
  CommandLine|contains:
  - ' approve '
  - ' create '
  - ' check '
  - ' delete '
selection_sharpwsus_flags:
  CommandLine|contains:
  - ' /payload:'
  - ' /payload='
  - ' /updateid:'
  - ' /updateid='
condition: all of selection_wsuspendu_* or all of selection_sharpwsus_*
```

## False Positives

- Unknown

## References

- https://labs.nettitude.com/blog/introducing-sharpwsus/
- https://github.com/nettitude/SharpWSUS
- https://web.archive.org/web/20210512154016/https://github.com/AlsidOfficial/WSUSpendu/blob/master/WSUSpendu.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpwsus_wsuspendu_execution.yml)
