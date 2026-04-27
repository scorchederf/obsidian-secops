---
sigma_id: "25676e10-2121-446e-80a4-71ff8506af47"
title: "Exchange PowerShell Snap-Ins Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_snapins_hafnium.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_snapins_hafnium.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "25676e10-2121-446e-80a4-71ff8506af47"
  - "Exchange PowerShell Snap-Ins Usage"
attack_technique_ids:
  - "T1059.001"
  - "T1114"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exchange PowerShell Snap-Ins Usage

Detects adding and using Exchange PowerShell snap-ins to export mailbox data. As seen used by HAFNIUM and APT27

## Metadata

- Rule ID: 25676e10-2121-446e-80a4-71ff8506af47
- Status: test
- Level: high
- Author: FPT.EagleEye, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-03-03
- Modified: 2023-03-24
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_snapins_hafnium.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1114-email_collection|T1114]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli:
  CommandLine|contains: Add-PSSnapin
selection_module:
  CommandLine|contains:
  - Microsoft.Exchange.Powershell.Snapin
  - Microsoft.Exchange.Management.PowerShell.SnapIn
filter_msiexec:
  ParentImage: C:\Windows\System32\msiexec.exe
  CommandLine|contains: $exserver=Get-ExchangeServer ([Environment]::MachineName)
    -ErrorVariable exerr 2> $null
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/
- https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/
- https://www.intrinsec.com/apt27-analysis/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_snapins_hafnium.yml)
