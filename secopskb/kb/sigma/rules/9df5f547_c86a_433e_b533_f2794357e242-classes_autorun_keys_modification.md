---
sigma_id: "9df5f547-c86a-433e-b533-f2794357e242"
title: "Classes Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_classes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_classes.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9df5f547-c86a-433e-b533-f2794357e242"
  - "Classes Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Classes Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: 9df5f547-c86a-433e-b533-f2794357e242
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_classes.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_classes_base:
  TargetObject|contains: \Software\Classes
selection_classes_target:
  TargetObject|contains:
  - \Folder\ShellEx\ExtShellFolderViews
  - \Folder\ShellEx\DragDropHandlers
  - \Folder\Shellex\ColumnHandlers
  - \Filter
  - \Exefile\Shell\Open\Command\(Default)
  - \Directory\Shellex\DragDropHandlers
  - \Directory\Shellex\CopyHookHandlers
  - \CLSID\{AC757296-3522-4E11-9862-C17BE5A1767E}\Instance
  - \CLSID\{ABE3B9A4-257D-4B97-BD1A-294AF496222E}\Instance
  - \CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance
  - \CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance
  - \Classes\AllFileSystemObjects\ShellEx\DragDropHandlers
  - \.exe
  - \.cmd
  - \ShellEx\PropertySheetHandlers
  - \ShellEx\ContextMenuHandlers
filter_main_drivers:
  Image: C:\Windows\System32\drvinst.exe
filter_main_empty:
  Details: (Empty)
filter_main_null:
  Details: null
filter_main_svchost:
  Image: C:\Windows\System32\svchost.exe
  TargetObject|contains: \lnkfile\shellex\ContextMenuHandlers\
filter_optional_msoffice:
  Details: '{807583E5-5146-11D5-A672-00B0D022E945}'
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_classes.yml)
