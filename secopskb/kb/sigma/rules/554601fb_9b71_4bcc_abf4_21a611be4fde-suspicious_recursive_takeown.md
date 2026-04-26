---
sigma_id: "554601fb-9b71-4bcc-abf4-21a611be4fde"
title: "Suspicious Recursive Takeown"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_takeown_recursive_own.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_takeown_recursive_own.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "554601fb-9b71-4bcc-abf4-21a611be4fde"
  - "Suspicious Recursive Takeown"
attack_technique_ids:
  - "T1222.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Recursive Takeown

Adversaries can interact with the DACLs using built-in Windows commands takeown which can grant adversaries higher permissions on specific files and folders

## Metadata

- Rule ID: 554601fb-9b71-4bcc-abf4-21a611be4fde
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-30
- Modified: 2022-11-21
- Source Path: rules/windows/process_creation/proc_creation_win_takeown_recursive_own.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Detection

```yaml
selection:
  Image|endswith: \takeown.exe
  CommandLine|contains|all:
  - '/f '
  - /r
condition: selection
```

## False Positives

- Scripts created by developers and admins
- Administrative activity

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/takeown
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1222.001/T1222.001.md#atomic-test-1---take-ownership-using-takeown-utility

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_takeown_recursive_own.yml)
