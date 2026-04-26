---
sigma_id: "54127bd4-f541-4ac3-afdb-ea073f63f692"
title: "Potential Persistence Via Notepad++ Plugins"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_notepad_plus_plus_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_notepad_plus_plus_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "54127bd4-f541-4ac3-afdb-ea073f63f692"
  - "Potential Persistence Via Notepad++ Plugins"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Notepad++ Plugins

Detects creation of new ".dll" files inside the plugins directory of a notepad++ installation by a process other than "gup.exe". Which could indicates possible persistence

## Metadata

- Rule ID: 54127bd4-f541-4ac3-afdb-ea073f63f692
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-10
- Modified: 2025-09-01
- Source Path: rules/windows/file/file_event/file_event_win_notepad_plus_plus_persistence.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|contains: \Notepad++\plugins\
  TargetFilename|endswith: .dll
filter_gup:
  Image|endswith: \Notepad++\updater\gup.exe
filter_install:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\Temp\
  Image|endswith:
  - \target.exe
  - Installer.x64.exe
filter_main_installer:
  Image|contains: \npp.
  Image|endswith: .exe
  TargetFilename:
  - C:\Program Files\Notepad++\plugins\NppExport\NppExport.dll
  - C:\Program Files\Notepad++\plugins\mimeTools\mimeTools.dll
  - C:\Program Files\Notepad++\plugins\NppConverter\NppConverter.dll
  - C:\Program Files\Notepad++\plugins\Config\nppPluginList.dll
condition: selection and not 1 of filter_*
```

## False Positives

- Possible FPs during first installation of Notepad++
- Legitimate use of custom plugins by users in order to enhance notepad++ functionalities

## References

- https://pentestlab.blog/2022/02/14/persistence-notepad-plugins/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_notepad_plus_plus_persistence.yml)
