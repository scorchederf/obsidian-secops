---
sigma_id: "3236fcd0-b7e3-4433-b4f8-86ad61a9af2d"
title: "Suspicious PowerShell Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_susp_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_susp_download.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_classic_start"
aliases:
  - "3236fcd0-b7e3-4433-b4f8-86ad61a9af2d"
  - "Suspicious PowerShell Download"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Download

Detects suspicious PowerShell download command

## Metadata

- Rule ID: 3236fcd0-b7e3-4433-b4f8-86ad61a9af2d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-05
- Modified: 2023-10-27
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_susp_download.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_webclient:
  Data|contains: Net.WebClient
selection_download:
  Data|contains:
  - .DownloadFile(
  - .DownloadString(
condition: all of selection_*
```

## False Positives

- PowerShell scripts that download content from the Internet

## References

- https://www.trendmicro.com/en_us/research/22/j/lv-ransomware-exploits-proxyshell-in-attack.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_susp_download.yml)
