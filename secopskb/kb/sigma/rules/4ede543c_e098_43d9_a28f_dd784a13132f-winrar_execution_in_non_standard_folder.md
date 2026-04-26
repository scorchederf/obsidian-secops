---
sigma_id: "4ede543c-e098-43d9-a28f-dd784a13132f"
title: "WinRAR Execution in Non-Standard Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrar_uncommon_folder_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_uncommon_folder_execution.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4ede543c-e098-43d9-a28f-dd784a13132f"
  - "WinRAR Execution in Non-Standard Folder"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WinRAR Execution in Non-Standard Folder

Detects a suspicious WinRAR execution in a folder which is not the default installation folder

## Metadata

- Rule ID: 4ede543c-e098-43d9-a28f-dd784a13132f
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Tigzy
- Date: 2021-11-17
- Modified: 2025-07-16
- Source Path: rules/windows/process_creation/proc_creation_win_winrar_uncommon_folder_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection:
- Image|endswith:
  - \rar.exe
  - \winrar.exe
- Description:
  - Command line RAR
  - WinRAR
filter_main_unrar:
  Image|endswith: \UnRAR.exe
filter_main_path:
  Image|contains:
  - :\Program Files (x86)\WinRAR\
  - :\Program Files\WinRAR\
filter_optional_temp:
  Image|contains: :\Windows\Temp\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate use of WinRAR in a folder of a software that bundles WinRAR

## References

- https://twitter.com/cyb3rops/status/1460978167628406785

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_uncommon_folder_execution.yml)
