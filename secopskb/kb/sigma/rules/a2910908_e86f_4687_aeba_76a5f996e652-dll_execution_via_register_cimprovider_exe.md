---
sigma_id: "a2910908-e86f-4687-aeba-76a5f996e652"
title: "DLL Execution Via Register-cimprovider.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_cimprovider_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_cimprovider_dll_load.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a2910908-e86f-4687-aeba-76a5f996e652"
  - "DLL Execution Via Register-cimprovider.exe"
attack_technique_ids:
  - "T1574"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DLL Execution Via Register-cimprovider.exe

Detects using register-cimprovider.exe to execute arbitrary dll file.

## Metadata

- Rule ID: a2910908-e86f-4687-aeba-76a5f996e652
- Status: test
- Level: medium
- Author: Ivan Dyachkov, Yulia Fomina, oscd.community
- Date: 2020-10-07
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_registry_cimprovider_dll_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]]

## Detection

```yaml
selection:
  Image|endswith: \register-cimprovider.exe
  CommandLine|contains|all:
  - -path
  - dll
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/PhilipTsukerman/status/992021361106268161
- https://lolbas-project.github.io/lolbas/Binaries/Register-cimprovider/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_cimprovider_dll_load.yml)
