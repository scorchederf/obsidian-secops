---
sigma_id: "ae7fbf8e-f3cb-49fd-8db4-5f3bed522c71"
title: "Suspicious PowerShell Invocations - Specific"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_invocation_specific.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invocation_specific.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "ae7fbf8e-f3cb-49fd-8db4-5f3bed522c71"
  - "Suspicious PowerShell Invocations - Specific"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Invocations - Specific

Detects suspicious PowerShell invocation command parameters

## Metadata

- Rule ID: ae7fbf8e-f3cb-49fd-8db4-5f3bed522c71
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro
- Date: 2017-03-05
- Modified: 2025-02-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_invocation_specific.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_convert_b64:
  ScriptBlockText|contains|all:
  - -nop
  - ' -w '
  - hidden
  - ' -c '
  - '[Convert]::FromBase64String'
selection_iex_selection:
  ScriptBlockText|contains|all:
  - ' -w '
  - hidden
  - -noni
  - -nop
  - ' -c '
  - iex
  - New-Object
selection_enc_selection:
  ScriptBlockText|contains|all:
  - ' -w '
  - hidden
  - -ep
  - bypass
  - -Enc
selection_reg_selection:
  ScriptBlockText|contains|all:
  - powershell
  - reg
  - add
  ScriptBlockText|contains:
  - \software\microsoft\windows\currentversion\run
  - \software\wow6432node\microsoft\windows\currentversion\run
  - \software\microsoft\windows\currentversion\policies\explorer\run
selection_webclient_selection:
  ScriptBlockText|contains|all:
  - bypass
  - -noprofile
  - -windowstyle
  - hidden
  - new-object
  - system.net.webclient
  - .download
selection_iex_webclient:
  ScriptBlockText|contains|all:
  - iex
  - New-Object
  - Net.WebClient
  - .Download
filter_chocolatey:
  ScriptBlockText|contains:
  - (New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1
  - (New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')
  - Write-ChocolateyWarning
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invocation_specific.yml)
