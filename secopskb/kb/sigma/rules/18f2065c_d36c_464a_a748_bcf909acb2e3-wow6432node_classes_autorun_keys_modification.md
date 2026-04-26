---
sigma_id: "18f2065c-d36c-464a-a748-bcf909acb2e3"
title: "Wow6432Node Classes Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_classes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_classes.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "18f2065c-d36c-464a-a748-bcf909acb2e3"
  - "Wow6432Node Classes Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wow6432Node Classes Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: 18f2065c-d36c-464a-a748-bcf909acb2e3
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_classes.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
wow_classes_base:
  TargetObject|contains: \Software\Wow6432Node\Classes
wow_classes:
  TargetObject|contains:
  - \Folder\ShellEx\ExtShellFolderViews
  - \Folder\ShellEx\DragDropHandlers
  - \Folder\ShellEx\ColumnHandlers
  - \Directory\Shellex\DragDropHandlers
  - \Directory\Shellex\CopyHookHandlers
  - \CLSID\{AC757296-3522-4E11-9862-C17BE5A1767E}\Instance
  - \CLSID\{ABE3B9A4-257D-4B97-BD1A-294AF496222E}\Instance
  - \CLSID\{7ED96837-96F0-4812-B211-F13C24117ED3}\Instance
  - \CLSID\{083863F1-70DE-11d0-BD40-00A0C911CE86}\Instance
  - \AllFileSystemObjects\ShellEx\DragDropHandlers
  - \ShellEx\PropertySheetHandlers
  - \ShellEx\ContextMenuHandlers
filter:
  Details: (Empty)
condition: wow_classes_base and wow_classes and not filter
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_classes.yml)
