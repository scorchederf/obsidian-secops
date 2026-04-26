---
sigma_id: "204b17ae-4007-471b-917b-b917b315c5db"
title: "Greedy File Deletion Using Del"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_del_greedy_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_del_greedy_deletion.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "204b17ae-4007-471b-917b-b917b315c5db"
  - "Greedy File Deletion Using Del"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Greedy File Deletion Using Del

Detects execution of the "del" builtin command to remove files using greedy/wildcard expression. This is often used by malware to delete content of folders that perhaps contains the initial malware infection or to delete evidence.

## Metadata

- Rule ID: 204b17ae-4007-471b-917b-b917b315c5db
- Status: test
- Level: medium
- Author: frack113 , X__Junior (Nextron Systems)
- Date: 2021-12-02
- Modified: 2023-09-11
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_del_greedy_deletion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_del:
  CommandLine|contains:
  - 'del '
  - 'erase '
selection_extensions:
  CommandLine|contains:
  - \\\*.au3
  - \\\*.dll
  - \\\*.exe
  - \\\*.js
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.joesandbox.com/analysis/509330/0/html#1044F3BDBE3BB6F734E357235F4D5898582D
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/erase

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_del_greedy_deletion.yml)
