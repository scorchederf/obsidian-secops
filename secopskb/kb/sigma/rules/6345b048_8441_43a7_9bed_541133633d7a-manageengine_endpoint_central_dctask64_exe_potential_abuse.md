---
sigma_id: "6345b048-8441-43a7-9bed-541133633d7a"
title: "ManageEngine Endpoint Central Dctask64.EXE Potential Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dctask64_arbitrary_command_and_dll_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dctask64_arbitrary_command_and_dll_execution.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6345b048-8441-43a7-9bed-541133633d7a"
  - "ManageEngine Endpoint Central Dctask64.EXE Potential Abuse"
attack_technique_ids:
  - "T1055.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ManageEngine Endpoint Central Dctask64.EXE Potential Abuse

Detects the execution of "dctask64.exe", a signed binary by ZOHO Corporation part of ManageEngine Endpoint Central.
This binary can be abused for DLL injection, arbitrary command and process execution.

## Metadata

- Rule ID: 6345b048-8441-43a7-9bed-541133633d7a
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-01-28
- Modified: 2025-01-22
- Source Path: rules/windows/process_creation/proc_creation_win_dctask64_arbitrary_command_and_dll_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \dctask64.exe
- Hashes|contains:
  - IMPHASH=6834B1B94E49701D77CCB3C0895E1AFD
  - IMPHASH=1BB6F93B129F398C7C4A76BB97450BBA
  - IMPHASH=FAA2AC19875FADE461C8D89DCF2710A3
  - IMPHASH=F1039CED4B91572AB7847D26032E6BBF
selection_cli:
  CommandLine|contains:
  - ' executecmd64 '
  - ' invokeexe '
  - ' injectDll '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/gN3mes1s/status/1222088214581825540
- https://twitter.com/gN3mes1s/status/1222095963789111296
- https://twitter.com/gN3mes1s/status/1222095371175911424

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dctask64_arbitrary_command_and_dll_execution.yml)
