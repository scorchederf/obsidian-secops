---
sigma_id: "6331d09b-4785-4c13-980f-f96661356249"
title: "PowerShell Downgrade Attack - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_downgrade_attack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_downgrade_attack.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_classic_start"
aliases:
  - "6331d09b-4785-4c13-980f-f96661356249"
  - "PowerShell Downgrade Attack - PowerShell"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Downgrade Attack - PowerShell

Detects PowerShell downgrade attack by comparing the host versions with the actually used engine version 2.0

## Metadata

- Rule ID: 6331d09b-4785-4c13-980f-f96661356249
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Lee Holmes (idea), Harish Segar (improvements)
- Date: 2017-03-22
- Modified: 2023-10-27
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_downgrade_attack.yml

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Data|contains: EngineVersion=2.
filter_main:
  Data|contains: HostVersion=2.
condition: selection and not filter_main
```

## False Positives

- Unknown

## References

- http://www.leeholmes.com/blog/2017/03/17/detecting-and-preventing-powershell-downgrade-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_downgrade_attack.yml)
