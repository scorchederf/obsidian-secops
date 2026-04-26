---
sigma_id: "82343930-652f-43f5-ab70-2ee9fdd6d5e9"
title: "Potential ShellDispatch.DLL Functionality Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_shelldispatch_potential_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_shelldispatch_potential_abuse.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "82343930-652f-43f5-ab70-2ee9fdd6d5e9"
  - "Potential ShellDispatch.DLL Functionality Abuse"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential ShellDispatch.DLL Functionality Abuse

Detects potential "ShellDispatch.dll" functionality abuse to execute arbitrary binaries via "ShellExecute"

## Metadata

- Rule ID: 82343930-652f-43f5-ab70-2ee9fdd6d5e9
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-06-20
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_shelldispatch_potential_abuse.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains: RunDll_ShellExecuteW
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.hexacorn.com/blog/2023/06/07/this-lolbin-doesnt-exist/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_shelldispatch_potential_abuse.yml)
