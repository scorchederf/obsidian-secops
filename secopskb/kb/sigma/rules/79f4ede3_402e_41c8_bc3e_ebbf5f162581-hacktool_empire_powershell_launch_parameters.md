---
sigma_id: "79f4ede3-402e-41c8-bc3e-ebbf5f162581"
title: "HackTool - Empire PowerShell Launch Parameters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_launch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_launch.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "79f4ede3-402e-41c8-bc3e-ebbf5f162581"
  - "HackTool - Empire PowerShell Launch Parameters"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - Empire PowerShell Launch Parameters

Detects suspicious powershell command line parameters used in Empire

## Metadata

- Rule ID: 79f4ede3-402e-41c8-bc3e-ebbf5f162581
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-04-20
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_launch.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ' -NoP -sta -NonI -W Hidden -Enc '
  - ' -noP -sta -w 1 -enc '
  - ' -NoP -NonI -W Hidden -enc '
  - ' -noP -sta -w 1 -enc'
  - ' -enc  SQB'
  - ' -nop -exec bypass -EncodedCommand '
condition: selection
```

## False Positives

- Other tools that incidentally use the same command line parameters

## References

- https://github.com/EmpireProject/Empire/blob/c2ba61ca8d2031dad0cfc1d5770ba723e8b710db/lib/common/helpers.py#L165
- https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/lib/modules/powershell/persistence/powerbreach/deaduser.py#L191
- https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/lib/modules/powershell/persistence/powerbreach/resolver.py#L178
- https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/data/module_source/privesc/Invoke-EventVwrBypass.ps1#L64

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_empire_powershell_launch.yml)
