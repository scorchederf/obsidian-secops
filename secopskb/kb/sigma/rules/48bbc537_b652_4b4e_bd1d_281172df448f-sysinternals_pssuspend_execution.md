---
sigma_id: "48bbc537-b652-4b4e-bd1d-281172df448f"
title: "Sysinternals PsSuspend Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "48bbc537-b652-4b4e-bd1d-281172df448f"
  - "Sysinternals PsSuspend Execution"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysinternals PsSuspend Execution

Detects usage of Sysinternals PsSuspend which can be abused to suspend critical processes

## Metadata

- Rule ID: 48bbc537-b652-4b4e-bd1d-281172df448f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-23
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
- OriginalFileName: pssuspend.exe
- Image|endswith:
  - \pssuspend.exe
  - \pssuspend64.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/pssuspend
- https://twitter.com/0gtweet/status/1638069413717975046

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_execution.yml)
