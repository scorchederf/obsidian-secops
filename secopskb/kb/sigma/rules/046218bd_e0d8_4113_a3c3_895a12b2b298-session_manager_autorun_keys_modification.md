---
sigma_id: "046218bd-e0d8-4113-a3c3-895a12b2b298"
title: "Session Manager Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_session_manager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_session_manager.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "046218bd-e0d8-4113-a3c3-895a12b2b298"
  - "Session Manager Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
  - "T1546.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Session Manager Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: 046218bd-e0d8-4113-a3c3-895a12b2b298
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_session_manager.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.009]]

## Detection

```yaml
session_manager_base:
  TargetObject|contains: \System\CurrentControlSet\Control\Session Manager
session_manager:
  TargetObject|contains:
  - \SetupExecute
  - \S0InitialCommand
  - \KnownDlls
  - \Execute
  - \BootExecute
  - \AppCertDlls
filter:
  Details: (Empty)
condition: session_manager_base and session_manager and not filter
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_session_manager.yml)
