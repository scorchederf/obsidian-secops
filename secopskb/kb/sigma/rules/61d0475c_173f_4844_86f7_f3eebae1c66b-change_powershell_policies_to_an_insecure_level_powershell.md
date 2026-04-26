---
sigma_id: "61d0475c-173f-4844-86f7-f3eebae1c66b"
title: "Change PowerShell Policies to an Insecure Level - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_set_policies_to_unsecure_level.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_policies_to_unsecure_level.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "61d0475c-173f-4844-86f7-f3eebae1c66b"
  - "Change PowerShell Policies to an Insecure Level - PowerShell"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Change PowerShell Policies to an Insecure Level - PowerShell

Detects changing the PowerShell script execution policy to a potentially insecure level using the "Set-ExecutionPolicy" cmdlet.

## Metadata

- Rule ID: 61d0475c-173f-4844-86f7-f3eebae1c66b
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-10-20
- Modified: 2023-12-14
- Source Path: rules/windows/powershell/powershell_script/posh_ps_set_policies_to_unsecure_level.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains: Set-ExecutionPolicy
selection_option:
  ScriptBlockText|contains:
  - Unrestricted
  - bypass
filter_optional_chocolatey:
  ScriptBlockText|contains:
  - (New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')
  - (New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Administrator script

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4
- https://adsecurity.org/?p=2604

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_set_policies_to_unsecure_level.yml)
