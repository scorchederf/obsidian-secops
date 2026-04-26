---
sigma_id: "1139d2e2-84b1-4226-b445-354492eba8ba"
title: "Usage Of Web Request Commands And Cmdlets - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_web_request_cmd_and_cmdlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_web_request_cmd_and_cmdlets.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "1139d2e2-84b1-4226-b445-354492eba8ba"
  - "Usage Of Web Request Commands And Cmdlets - ScriptBlock"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Usage Of Web Request Commands And Cmdlets - ScriptBlock

Detects the use of various web request commands with commandline tools and Windows PowerShell cmdlets (including aliases) via PowerShell scriptblock logs

## Metadata

- Rule ID: 1139d2e2-84b1-4226-b445-354492eba8ba
- Status: test
- Level: medium
- Author: James Pemberton / @4A616D6573
- Date: 2019-10-24
- Modified: 2025-10-20
- Source Path: rules/windows/powershell/powershell_script/posh_ps_web_request_cmd_and_cmdlets.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - '[System.Net.WebRequest]::create'
  - 'curl '
  - Invoke-RestMethod
  - Invoke-WebRequest
  - ' irm '
  - 'iwr '
  - Resume-BitsTransfer
  - Start-BitsTransfer
  - 'wget '
  - WinHttp.WinHttpRequest
filter:
  Path|startswith: C:\Packages\Plugins\Microsoft.GuestConfiguration.ConfigurationforWindows\
condition: selection and not filter
```

## False Positives

- Use of Get-Command and Get-Help modules to reference Invoke-WebRequest and Start-BitsTransfer.

## References

- https://4sysops.com/archives/use-powershell-to-download-a-file-with-http-https-and-ftp/
- https://blog.jourdant.me/post/3-ways-to-download-files-with-powershell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_web_request_cmd_and_cmdlets.yml)
