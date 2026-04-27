---
sigma_id: "afe52666-401e-4a02-b4ff-5d128990b8cb"
title: "Suspicious Greedy Compression Using Rar.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rar_susp_greedy_compression.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_susp_greedy_compression.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "afe52666-401e-4a02-b4ff-5d128990b8cb"
  - "Suspicious Greedy Compression Using Rar.EXE"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Greedy Compression Using Rar.EXE

Detects RAR usage that creates an archive from a suspicious folder, either a system folder or one of the folders often used by attackers for staging purposes

## Metadata

- Rule ID: afe52666-401e-4a02-b4ff-5d128990b8cb
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2022-12-15
- Modified: 2024-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_rar_susp_greedy_compression.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_opt_1:
- Image|endswith: \rar.exe
- Description: Command line RAR
selection_opt_2:
  CommandLine|contains:
  - '.exe a '
  - ' a -m'
selection_cli_flags:
  CommandLine|contains|all:
  - ' -hp'
  - ' -r '
selection_cli_folders:
  CommandLine|contains:
  - ' ?:\\\*.'
  - ' ?:\\\\\*.'
  - ' ?:\$Recycle.bin\'
  - ' ?:\PerfLogs\'
  - ' ?:\Temp'
  - ' ?:\Users\Public\'
  - ' ?:\Windows\'
  - ' %public%'
condition: 1 of selection_opt_* and all of selection_cli_*
```

## False Positives

- Unknown

## References

- https://decoded.avast.io/martinchlumecky/png-steganography

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_susp_greedy_compression.yml)
