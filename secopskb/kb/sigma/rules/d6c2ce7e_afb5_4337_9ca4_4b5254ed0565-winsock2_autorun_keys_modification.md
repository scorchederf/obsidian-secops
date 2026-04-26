---
sigma_id: "d6c2ce7e-afb5-4337-9ca4-4b5254ed0565"
title: "WinSock2 Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_winsock2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_winsock2.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "d6c2ce7e-afb5-4337-9ca4-4b5254ed0565"
  - "WinSock2 Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WinSock2 Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: d6c2ce7e-afb5-4337-9ca4-4b5254ed0565
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_winsock2.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
winsock_parameters_base:
  TargetObject|contains: \System\CurrentControlSet\Services\WinSock2\Parameters
winsock_parameters:
  TargetObject|contains:
  - \Protocol_Catalog9\Catalog_Entries
  - \NameSpace_Catalog5\Catalog_Entries
filter:
- Details: (Empty)
- Image: C:\Windows\System32\MsiExec.exe
- Image: C:\Windows\syswow64\MsiExec.exe
condition: winsock_parameters_base and winsock_parameters and not filter
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_winsock2.yml)
