---
sigma_id: "3b6ab547-8ec2-4991-b9d2-2b06702a48d7"
title: "PowerShell Download Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_download_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_patterns.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3b6ab547-8ec2-4991-b9d2-2b06702a48d7"
  - "PowerShell Download Pattern"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Download Pattern

Detects a Powershell process that contains download commands in its command line string

## Metadata

- Rule ID: 3b6ab547-8ec2-4991-b9d2-2b06702a48d7
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), oscd.community, Jonhnathan Ribeiro
- Date: 2019-01-16
- Modified: 2025-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_download_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell_ISE.EXE
  - PowerShell.EXE
  - pwsh.dll
selection_cli:
  CommandLine|contains|all:
  - new-object
  - net.webclient).
  - download
  CommandLine|contains:
  - string(
  - file(
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.redteam.pl/2020/06/black-kingdom-ransomware.html
- https://lab52.io/blog/winter-vivern-all-summer/
- https://hatching.io/blog/powershell-analysis/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_patterns.yml)
