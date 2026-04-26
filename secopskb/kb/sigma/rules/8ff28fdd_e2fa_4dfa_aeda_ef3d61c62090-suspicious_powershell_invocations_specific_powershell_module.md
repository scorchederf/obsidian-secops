---
sigma_id: "8ff28fdd-e2fa-4dfa-aeda-ef3d61c62090"
title: "Suspicious PowerShell Invocations - Specific - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_invocation_specific.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_invocation_specific.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "8ff28fdd-e2fa-4dfa-aeda-ef3d61c62090"
  - "Suspicious PowerShell Invocations - Specific - PowerShell Module"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Invocations - Specific - PowerShell Module

Detects suspicious PowerShell invocation command parameters

## Metadata

- Rule ID: 8ff28fdd-e2fa-4dfa-aeda-ef3d61c62090
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro
- Date: 2017-03-05
- Modified: 2025-02-17
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_invocation_specific.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_convert_b64:
  ContextInfo|contains|all:
  - -nop
  - ' -w '
  - hidden
  - ' -c '
  - '[Convert]::FromBase64String'
selection_iex:
  ContextInfo|contains|all:
  - ' -w '
  - hidden
  - -noni
  - -nop
  - ' -c '
  - iex
  - New-Object
selection_enc:
  ContextInfo|contains|all:
  - ' -w '
  - hidden
  - -ep
  - bypass
  - -Enc
selection_reg:
  ContextInfo|contains|all:
  - powershell
  - reg
  - add
  ContextInfo|contains:
  - \software\microsoft\windows\currentversion\run
  - \software\wow6432node\microsoft\windows\currentversion\run
  - \software\microsoft\windows\currentversion\policies\explorer\run
selection_webclient:
  ContextInfo|contains|all:
  - bypass
  - -noprofile
  - -windowstyle
  - hidden
  - new-object
  - system.net.webclient
  - .download
selection_iex_webclient:
  ContextInfo|contains|all:
  - iex
  - New-Object
  - Net.WebClient
  - .Download
filter_chocolatey:
  ContextInfo|contains:
  - (New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1
  - Write-ChocolateyWarning
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_invocation_specific.yml)
