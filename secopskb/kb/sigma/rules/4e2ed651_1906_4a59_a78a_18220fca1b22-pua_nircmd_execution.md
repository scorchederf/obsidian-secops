---
sigma_id: "4e2ed651-1906-4a59-a78a-18220fca1b22"
title: "PUA - NirCmd Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nircmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nircmd.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4e2ed651-1906-4a59-a78a-18220fca1b22"
  - "PUA - NirCmd Execution"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - NirCmd Execution

Detects the use of NirCmd tool for command execution, which could be the result of legitimate administrative activity

## Metadata

- Rule ID: 4e2ed651-1906-4a59-a78a-18220fca1b22
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-24
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_pua_nircmd.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection_org:
- Image|endswith: \NirCmd.exe
- OriginalFileName: NirCmd.exe
selection_cmd:
  CommandLine|contains:
  - ' execmd '
  - '.exe script '
  - '.exe shexec '
  - ' runinteractive '
combo_exec:
  CommandLine|contains:
  - ' exec '
  - ' exec2 '
combo_exec_params:
  CommandLine|contains:
  - ' show '
  - ' hide '
condition: 1 of selection_* or all of combo_*
```

## False Positives

- Legitimate use by administrators

## References

- https://www.nirsoft.net/utils/nircmd.html
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/
- https://www.nirsoft.net/utils/nircmd2.html#using

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nircmd.yml)
