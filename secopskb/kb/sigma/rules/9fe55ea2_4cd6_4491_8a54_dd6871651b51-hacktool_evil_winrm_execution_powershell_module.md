---
sigma_id: "9fe55ea2-4cd6-4491-8a54-dd6871651b51"
title: "HackTool - Evil-WinRm Execution - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_hktl_evil_winrm_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_hktl_evil_winrm_execution.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / ps_module"
aliases:
  - "9fe55ea2-4cd6-4491-8a54-dd6871651b51"
  - "HackTool - Evil-WinRm Execution - PowerShell Module"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Evil-WinRm Execution - PowerShell Module

Detects the execution of Evil-WinRM via PowerShell Module logs by leveraging the hardcoded strings inside the utility.

## Metadata

- Rule ID: 9fe55ea2-4cd6-4491-8a54-dd6871651b51
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-02-25
- Source Path: rules/windows/powershell/powershell_module/posh_pm_hktl_evil_winrm_execution.yml

## Logsource

- category: ps_module
- product: windows

## Detection

```yaml
selection_wsm:
  ContextInfo|contains:
  - :\Windows\System32\wsmprovhost.exe
  - :\Windows\SysWOW64\wsmprovhost.exe
selection_payload_1:
  Payload|contains:
  - value="(get-location).path
  - value="(get-item*).length
  - 'Invoke-Binary '
  - Donut-Loader -process_id*-donutfile
  - Bypass-4MSI
  - IEX ([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($a))).replace('???','')
selection_payload_2:
  Payload|contains|all:
  - $servicios = Get-ItemProperty "registry::HKLM\System\CurrentControlSet\Services\"
  - Where-Object {$_.imagepath -notmatch "system" -and $_.imagepath -ne $null } |
    Select-Object pschildname,imagepath
selection_payload_3:
  Payload|contains|all:
  - $a +=  \"$($_.FullName.Replace('\\','/'))/\"}else{  $a += \"$($_.FullName.Replace('\\',
    '/'))\" }
  - $a=@();$
condition: selection_wsm and 1 of selection_payload_*
```

## False Positives

- Unknown

## References

- https://github.com/Hackplayers/evil-winrm/blob/7514b055d67ec19836e95c05bd63e7cc47c4c2aa/evil-winrm.rb
- https://github.com/search?q=repo%3AHackplayers%2Fevil-winrm++shell.run%28&type=code

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_hktl_evil_winrm_execution.yml)
