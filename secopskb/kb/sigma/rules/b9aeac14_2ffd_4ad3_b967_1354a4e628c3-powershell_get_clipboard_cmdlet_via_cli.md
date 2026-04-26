---
sigma_id: "b9aeac14-2ffd-4ad3-b967-1354a4e628c3"
title: "PowerShell Get-Clipboard Cmdlet Via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_get_clipboard.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_get_clipboard.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b9aeac14-2ffd-4ad3-b967-1354a4e628c3"
  - "PowerShell Get-Clipboard Cmdlet Via CLI"
attack_technique_ids:
  - "T1115"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Get-Clipboard Cmdlet Via CLI

Detects usage of the 'Get-Clipboard' cmdlet via CLI

## Metadata

- Rule ID: b9aeac14-2ffd-4ad3-b967-1354a4e628c3
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-05-02
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_get_clipboard.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1115-clipboard_data|T1115]]

## Detection

```yaml
selection:
  CommandLine|contains: Get-Clipboard
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/16
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/3.B.2_C36B49B5-DF58-4A34-9FE9-56189B9DEFEA.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_get_clipboard.yml)
