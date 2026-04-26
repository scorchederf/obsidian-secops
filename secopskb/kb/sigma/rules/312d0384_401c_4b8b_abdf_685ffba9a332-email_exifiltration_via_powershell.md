---
sigma_id: "312d0384-401c-4b8b-abdf-685ffba9a332"
title: "Email Exifiltration Via Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_email_exfil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_email_exfil.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "312d0384-401c-4b8b-abdf-685ffba9a332"
  - "Email Exifiltration Via Powershell"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Email Exifiltration Via Powershell

Detects email exfiltration via powershell cmdlets

## Metadata

- Rule ID: 312d0384-401c-4b8b-abdf-685ffba9a332
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems),  Azure-Sentinel (idea)
- Date: 2022-09-09
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_email_exfil.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains|all:
  - Add-PSSnapin
  - Get-Recipient
  - -ExpandProperty
  - EmailAddresses
  - SmtpAddress
  - -hidetableheaders
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/09/07/profiling-dev-0270-phosphorus-ransomware-operations/
- https://github.com/Azure/Azure-Sentinel/blob/7e6aa438e254d468feec061618a7877aa528ee9f/Hunting%20Queries/Microsoft%20365%20Defender/Ransomware/DEV-0270/Email%20data%20exfiltration%20via%20PowerShell.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_email_exfil.yml)
