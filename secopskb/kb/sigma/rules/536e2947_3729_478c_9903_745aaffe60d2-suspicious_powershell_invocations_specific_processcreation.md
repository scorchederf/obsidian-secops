---
sigma_id: "536e2947-3729-478c-9903-745aaffe60d2"
title: "Suspicious PowerShell Invocations - Specific - ProcessCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_invocation_specific.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invocation_specific.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "536e2947-3729-478c-9903-745aaffe60d2"
  - "Suspicious PowerShell Invocations - Specific - ProcessCreation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Invocations - Specific - ProcessCreation

Detects suspicious PowerShell invocation command parameters

## Metadata

- Rule ID: 536e2947-3729-478c-9903-745aaffe60d2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_invocation_specific.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_convert_b64:
  CommandLine|contains|all:
  - -nop
  - ' -w '
  - hidden
  - ' -c '
  - '[Convert]::FromBase64String'
selection_iex:
  CommandLine|contains|all:
  - ' -w '
  - hidden
  - -noni
  - -nop
  - ' -c '
  - iex
  - New-Object
selection_enc:
  CommandLine|contains|all:
  - ' -w '
  - hidden
  - -ep
  - bypass
  - -Enc
selection_reg:
  CommandLine|contains|all:
  - powershell
  - reg
  - add
  - \software\
selection_webclient:
  CommandLine|contains|all:
  - bypass
  - -noprofile
  - -windowstyle
  - hidden
  - new-object
  - system.net.webclient
  - .download
selection_iex_webclient:
  CommandLine|contains|all:
  - iex
  - New-Object
  - Net.WebClient
  - .Download
filter_chocolatey:
  CommandLine|contains:
  - (New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1
  - Write-ChocolateyWarning
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invocation_specific.yml)
