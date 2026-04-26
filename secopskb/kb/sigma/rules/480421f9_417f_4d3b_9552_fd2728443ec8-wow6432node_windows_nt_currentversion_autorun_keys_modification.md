---
sigma_id: "480421f9-417f-4d3b-9552-fd2728443ec8"
title: "Wow6432Node Windows NT CurrentVersion Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_currentversion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_currentversion.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "480421f9-417f-4d3b-9552-fd2728443ec8"
  - "Wow6432Node Windows NT CurrentVersion Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Wow6432Node Windows NT CurrentVersion Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: 480421f9-417f-4d3b-9552-fd2728443ec8
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2025-10-22
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_currentversion.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_wow_nt_current_version_base:
  TargetObject|contains: \SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion
selection_wow_nt_current_version:
  TargetObject|contains:
  - \Windows\Appinit_Dlls
  - \Image File Execution Options
  - \Drivers32
filter_main_empty:
  Details: (Empty)
filter_main_null:
  Details: null
filter_main_file_exec_options:
  Details|endswith: \Microsoft\Windows NT\CurrentVersion\Image File Execution Options
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_wow6432node_currentversion.yml)
