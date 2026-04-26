---
sigma_id: "ce7cf472-6fcc-490a-9481-3786840b5d9b"
title: "InfDefaultInstall.exe .inf Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ce7cf472-6fcc-490a-9481-3786840b5d9b"
  - "InfDefaultInstall.exe .inf Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# InfDefaultInstall.exe .inf Execution

Executes SCT script using scrobj.dll from a command in entered into a specially prepared INF file.

## Metadata

- Rule ID: ce7cf472-6fcc-490a-9481-3786840b5d9b
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-13
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - 'InfDefaultInstall.exe '
  - '.inf'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md#atomic-test-4---infdefaultinstallexe-inf-execution
- https://lolbas-project.github.io/lolbas/Binaries/Infdefaultinstall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_infdefaultinstall_execute_sct_scripts.yml)
