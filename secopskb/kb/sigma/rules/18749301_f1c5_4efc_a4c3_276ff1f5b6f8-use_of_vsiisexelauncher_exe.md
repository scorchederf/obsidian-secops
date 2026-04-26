---
sigma_id: "18749301-f1c5-4efc-a4c3-276ff1f5b6f8"
title: "Use of VSIISExeLauncher.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "18749301-f1c5-4efc-a4c3-276ff1f5b6f8"
  - "Use of VSIISExeLauncher.exe"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of VSIISExeLauncher.exe

The "VSIISExeLauncher.exe" binary part of the Visual Studio/VS Code can be used to execute arbitrary binaries

## Metadata

- Rule ID: 18749301-f1c5-4efc-a4c3-276ff1f5b6f8
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection_img:
- Image|endswith: \VSIISExeLauncher.exe
- OriginalFileName: VSIISExeLauncher.exe
selection_cli:
  CommandLine|contains:
  - ' -p '
  - ' -a '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/VSIISExeLauncher/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml)
