---
sigma_id: "434c08ba-8406-4d15-8b24-782cb071a691"
title: "PowerShell Execution With Potential Decryption Capabilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_decrypt_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_decrypt_pattern.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "434c08ba-8406-4d15-8b24-782cb071a691"
  - "PowerShell Execution With Potential Decryption Capabilities"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Execution With Potential Decryption Capabilities

Detects PowerShell commands that decrypt an ".LNK" "file to drop the next stage of the malware.

## Metadata

- Rule ID: 434c08ba-8406-4d15-8b24-782cb071a691
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-30
- Modified: 2023-12-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_decrypt_pattern.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli_dir:
  CommandLine|contains:
  - 'Get-ChildItem '
  - 'dir '
  - 'gci '
  - 'ls '
selection_cli_gc:
  CommandLine|contains:
  - 'Get-Content '
  - 'gc '
  - 'cat '
  - 'type '
  - ReadAllBytes
selection_cli_specific:
- CommandLine|contains|all:
  - ' ^| '
  - \*.lnk
  - -Recurse
  - '-Skip '
- CommandLine|contains|all:
  - ' -ExpandProperty '
  - \*.lnk
  - WriteAllBytes
  - ' .length '
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://research.checkpoint.com/2023/chinese-threat-actors-targeting-europe-in-smugx-campaign/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_decrypt_pattern.yml)
