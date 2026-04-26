---
sigma_id: "9fc51a3c-81b3-4fa7-b35f-7c02cf10fd2d"
title: "Usage Of Web Request Commands And Cmdlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_web_request_cmd_and_cmdlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_web_request_cmd_and_cmdlets.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9fc51a3c-81b3-4fa7-b35f-7c02cf10fd2d"
  - "Usage Of Web Request Commands And Cmdlets"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Usage Of Web Request Commands And Cmdlets

Detects the use of various web request commands with commandline tools and Windows PowerShell cmdlets (including aliases) via CommandLine

## Metadata

- Rule ID: 9fc51a3c-81b3-4fa7-b35f-7c02cf10fd2d
- Status: test
- Level: medium
- Author: James Pemberton / @4A616D6573, Endgame, JHasenbusch, oscd.community, Austin Songer @austinsonger
- Date: 2019-10-24
- Modified: 2025-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_web_request_cmd_and_cmdlets.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
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
condition: selection
```

## False Positives

- Use of Get-Command and Get-Help modules to reference Invoke-WebRequest and Start-BitsTransfer.

## References

- https://4sysops.com/archives/use-powershell-to-download-a-file-with-http-https-and-ftp/
- https://blog.jourdant.me/post/3-ways-to-download-files-with-powershell
- https://learn.microsoft.com/en-us/powershell/module/bitstransfer/add-bitsfile?view=windowsserver2019-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_web_request_cmd_and_cmdlets.yml)
