---
sigma_id: "05ebafc8-7aa2-4bcd-a269-2aec93f9e842"
title: "Add New Download Source To Winget"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winget_add_custom_source.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_add_custom_source.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "05ebafc8-7aa2-4bcd-a269-2aec93f9e842"
  - "Add New Download Source To Winget"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add New Download Source To Winget

Detects usage of winget to add new additional download sources

## Metadata

- Rule ID: 05ebafc8-7aa2-4bcd-a269-2aec93f9e842
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-17
- Source Path: rules/windows/process_creation/proc_creation_win_winget_add_custom_source.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \winget.exe
- OriginalFileName: winget.exe
selection_cli:
  CommandLine|contains|all:
  - 'source '
  - 'add '
condition: all of selection_*
```

## False Positives

- False positive are expected with legitimate sources

## References

- https://learn.microsoft.com/en-us/windows/package-manager/winget/source
- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_add_custom_source.yml)
