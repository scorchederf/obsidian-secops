---
sigma_id: "81315b50-6b60-4d8f-9928-3466e1022515"
title: "Desktop.INI Created by Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_desktop_ini_created_by_uncommon_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_desktop_ini_created_by_uncommon_process.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "81315b50-6b60-4d8f-9928-3466e1022515"
  - "Desktop.INI Created by Uncommon Process"
attack_technique_ids:
  - "T1547.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Desktop.INI Created by Uncommon Process

Detects unusual processes accessing desktop.ini, which can be leveraged to alter how Explorer displays a folder's content (i.e. renaming files) without changing them on disk.

## Metadata

- Rule ID: 81315b50-6b60-4d8f-9928-3466e1022515
- Status: test
- Level: medium
- Author: Maxime Thiebaut (@0xThiebaut), Tim Shelton (HAWK.IO)
- Date: 2020-03-19
- Modified: 2025-12-09
- Source Path: rules/windows/file/file_event/file_event_win_desktop_ini_created_by_uncommon_process.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.009]]

## Detection

```yaml
selection:
  TargetFilename|endswith: \desktop.ini
filter_main_generic:
  Image|startswith:
  - C:\Windows\
  - C:\Program Files\
  - C:\Program Files (x86)\
filter_main_upgrade:
  TargetFilename|startswith: C:\$WINDOWS.~BT\NewOS\
filter_optional_jetbrains:
  Image|startswith: C:\Users\
  Image|endswith: \AppData\Local\JetBrains\Toolbox\bin\7z.exe
  TargetFilename|contains: \JetBrains\apps\
filter_optional_onedrive:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\Microsoft\OneDrive\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Operations performed through Windows SCCM or equivalent
- Read only access list authority

## References

- https://isc.sans.edu/forums/diary/Desktopini+as+a+postexploitation+tool/25912/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_desktop_ini_created_by_uncommon_process.yml)
