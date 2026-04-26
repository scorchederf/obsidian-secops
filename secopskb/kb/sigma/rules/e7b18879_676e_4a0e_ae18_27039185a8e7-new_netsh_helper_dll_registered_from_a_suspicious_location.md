---
sigma_id: "e7b18879-676e-4a0e-ae18-27039185a8e7"
title: "New Netsh Helper DLL Registered From A Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_netsh_help_dll_persistence_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_netsh_help_dll_persistence_susp_location.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e7b18879-676e-4a0e-ae18-27039185a8e7"
  - "New Netsh Helper DLL Registered From A Suspicious Location"
attack_technique_ids:
  - "T1546.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Netsh Helper DLL Registered From A Suspicious Location

Detects changes to the Netsh registry key to add a new DLL value that is located on a suspicious location. This change might be an indication of a potential persistence attempt by adding a malicious Netsh helper

## Metadata

- Rule ID: e7b18879-676e-4a0e-ae18-27039185a8e7
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-11-28
- Source Path: rules/windows/registry/registry_set/registry_set_netsh_help_dll_persistence_susp_location.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.007]]

## Detection

```yaml
selection_target:
  TargetObject|contains: \SOFTWARE\Microsoft\NetSh
selection_folders_1:
  Details|contains:
  - :\Perflogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \Temporary Internet
selection_folders_2:
- Details|contains|all:
  - :\Users\
  - \Favorites\
- Details|contains|all:
  - :\Users\
  - \Favourites\
- Details|contains|all:
  - :\Users\
  - \Contacts\
- Details|contains|all:
  - :\Users\
  - \Pictures\
condition: selection_target and 1 of selection_folders_*
```

## False Positives

- Unknown

## References

- https://www.ired.team/offensive-security/persistence/t1128-netsh-helper-dll
- https://pentestlab.blog/2019/10/29/persistence-netsh-helper-dll/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_netsh_help_dll_persistence_susp_location.yml)
