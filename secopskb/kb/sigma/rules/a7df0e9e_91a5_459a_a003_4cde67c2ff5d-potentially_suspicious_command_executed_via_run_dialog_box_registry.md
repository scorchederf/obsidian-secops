---
sigma_id: "a7df0e9e-91a5-459a-a003-4cde67c2ff5d"
title: "Potentially Suspicious Command Executed Via Run Dialog Box - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_runmru_susp_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_runmru_susp_command_execution.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a7df0e9e-91a5-459a-a003-4cde67c2ff5d"
  - "Potentially Suspicious Command Executed Via Run Dialog Box - Registry"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potentially Suspicious Command Executed Via Run Dialog Box - Registry

Detects execution of commands via the run dialog box on Windows by checking values of the "RunMRU" registry key.
This technique was seen being abused by threat actors to deceive users into pasting and executing malicious commands, often disguised as CAPTCHA verification steps.

## Metadata

- Rule ID: a7df0e9e-91a5-459a-a003-4cde67c2ff5d
- Status: test
- Level: high
- Author: Ahmed Farouk, Nasreddine Bencherchali
- Date: 2024-11-01
- Source Path: rules/windows/registry/registry_set/registry_set_runmru_susp_command_execution.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_key:
  TargetObject|contains: \Microsoft\Windows\CurrentVersion\Explorer\RunMRU
selection_powershell_command:
  Details|contains:
  - powershell
  - pwsh
selection_powershell_susp_keywords:
  Details|contains:
  - ' -e '
  - ' -ec '
  - ' -en '
  - ' -enc '
  - ' -enco'
  - ftp
  - Hidden
  - http
  - iex
  - Invoke-
selection_wmic_command:
  Details|contains: wmic
selection_wmic_susp_keywords:
  Details|contains:
  - shadowcopy
  - process call create
condition: selection_key and (all of selection_powershell_* or all of selection_wmic_*)
```

## False Positives

- Unknown

## References

- https://medium.com/@ahmed.moh.farou2/fake-captcha-campaign-on-arabic-pirated-movie-sites-delivers-lumma-stealer-4f203f7adabf
- https://medium.com/@shaherzakaria8/downloading-trojan-lumma-infostealer-through-capatcha-1f25255a0e71
- https://www.forensafe.com/blogs/runmrukey.html
- https://redcanary.com/blog/threat-intelligence/intelligence-insights-october-2024/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_runmru_susp_command_execution.yml)
