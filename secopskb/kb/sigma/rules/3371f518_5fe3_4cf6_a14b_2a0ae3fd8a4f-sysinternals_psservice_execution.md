---
sigma_id: "3371f518-5fe3-4cf6-a14b-2a0ae3fd8a4f"
title: "Sysinternals PsService Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psservice.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psservice.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3371f518-5fe3-4cf6-a14b-2a0ae3fd8a4f"
  - "Sysinternals PsService Execution"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysinternals PsService Execution

Detects usage of Sysinternals PsService which can be abused for service reconnaissance and tampering

## Metadata

- Rule ID: 3371f518-5fe3-4cf6-a14b-2a0ae3fd8a4f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-16
- Modified: 2023-02-24
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psservice.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
- OriginalFileName: psservice.exe
- Image|endswith:
  - \PsService.exe
  - \PsService64.exe
condition: selection
```

## False Positives

- Legitimate use of PsService by an administrator

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psservice

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psservice.yml)
