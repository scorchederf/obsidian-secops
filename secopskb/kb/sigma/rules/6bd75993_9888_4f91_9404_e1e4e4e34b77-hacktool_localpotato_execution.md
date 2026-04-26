---
sigma_id: "6bd75993-9888-4f91-9404-e1e4e4e34b77"
title: "HackTool - LocalPotato Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_localpotato.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_localpotato.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6bd75993-9888-4f91-9404-e1e4e4e34b77"
  - "HackTool - LocalPotato Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - LocalPotato Execution

Detects the execution of the LocalPotato POC based on basic PE metadata information and default CLI examples

## Metadata

- Rule ID: 6bd75993-9888-4f91-9404-e1e4e4e34b77
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-14
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_localpotato.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \LocalPotato.exe
selection_cli:
  CommandLine|contains|all:
  - .exe -i C:\
  - -o Windows\
selection_hash_plain:
  Hashes|contains:
  - IMPHASH=E1742EE971D6549E8D4D81115F88F1FC
  - IMPHASH=DD82066EFBA94D7556EF582F247C8BB5
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://www.localpotato.com/localpotato_html/LocalPotato.html
- https://github.com/decoder-it/LocalPotato

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_localpotato.yml)
