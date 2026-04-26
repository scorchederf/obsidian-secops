---
sigma_id: "bbb80e91-5746-4fbe-8898-122e2cafdbf4"
title: "Suspicious PowerShell Invocations - Generic - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_invocation_generic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_invocation_generic.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "bbb80e91-5746-4fbe-8898-122e2cafdbf4"
  - "Suspicious PowerShell Invocations - Generic - PowerShell Module"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Invocations - Generic - PowerShell Module

Detects suspicious PowerShell invocation command parameters

## Metadata

- Rule ID: bbb80e91-5746-4fbe-8898-122e2cafdbf4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-12
- Modified: 2023-01-03
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_invocation_generic.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_encoded:
  ContextInfo|contains:
  - ' -enc '
  - ' -EncodedCommand '
  - ' -ec '
selection_hidden:
  ContextInfo|contains:
  - ' -w hidden '
  - ' -window hidden '
  - ' -windowstyle hidden '
  - ' -w 1 '
selection_noninteractive:
  ContextInfo|contains:
  - ' -noni '
  - ' -noninteractive '
condition: all of selection*
```

## False Positives

- Very special / sneaky PowerShell scripts

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_invocation_generic.yml)
