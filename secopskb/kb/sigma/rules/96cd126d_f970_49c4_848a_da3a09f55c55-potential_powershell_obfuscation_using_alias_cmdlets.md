---
sigma_id: "96cd126d-f970-49c4-848a-da3a09f55c55"
title: "Potential PowerShell Obfuscation Using Alias Cmdlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_set_alias.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_set_alias.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "96cd126d-f970-49c4-848a-da3a09f55c55"
  - "Potential PowerShell Obfuscation Using Alias Cmdlets"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PowerShell Obfuscation Using Alias Cmdlets

Detects Set-Alias or New-Alias cmdlet usage. Which can be use as a mean to obfuscate PowerShell scripts

## Metadata

- Rule ID: 96cd126d-f970-49c4-848a-da3a09f55c55
- Status: test
- Level: low
- Author: frack113
- Date: 2023-01-08
- Modified: 2025-10-22
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_set_alias.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - 'Set-Alias '
  - 'New-Alias '
filter_main_cim:
  ScriptBlockText:
  - Set-Alias -Name ncms -Value New-CimSession -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name gcls -Value Get-CimClass -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name ncso -Value New-CimSessionOption -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name gcms -Value Get-CimSession -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name rcms -Value Remove-cimSession -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name rcie -Value Register-CimIndicationEvent -Option ReadOnly, AllScope
    -ErrorAction SilentlyContinue
  - Set-Alias -Name gcai -Value Get-CimAssociatedInstance -Option ReadOnly, AllScope
    -ErrorAction SilentlyContinue
  - Set-Alias -Name gcim -Value Get-CimInstance -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name scim -Value Set-CimInstance -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name ncim -Value New-CimInstance -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name rcim -Value Remove-cimInstance -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
  - Set-Alias -Name icim -Value Invoke-CimMethod -Option ReadOnly, AllScope -ErrorAction
    SilentlyContinue
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/1337Rin/Swag-PSO

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_set_alias.yml)
