---
sigma_id: "3c89a1e8-0fba-449e-8f1b-8409d6267ec8"
title: "Suspicious Process Created Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_susp_process_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_susp_process_creation.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "3c89a1e8-0fba-449e-8f1b-8409d6267ec8"
  - "Suspicious Process Created Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Process Created Via Wmic.EXE

Detects WMIC executing "process call create" with suspicious calls to processes such as "rundll32", "regsrv32", etc.

## Metadata

- Rule ID: 3c89a1e8-0fba-449e-8f1b-8409d6267ec8
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-10-12
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_susp_process_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - 'process '
  - 'call '
  - 'create '
  CommandLine|contains:
  - rundll32
  - bitsadmin
  - regsvr32
  - 'cmd.exe /c '
  - 'cmd.exe /k '
  - 'cmd.exe /r '
  - 'cmd /c '
  - 'cmd /k '
  - 'cmd /r '
  - powershell
  - pwsh
  - certutil
  - cscript
  - wscript
  - mshta
  - \Users\Public\
  - \Windows\Temp\
  - \AppData\Local\
  - '%temp%'
  - '%tmp%'
  - '%ProgramData%'
  - '%appdata%'
  - '%comspec%'
  - '%localappdata%'
condition: selection
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2020/10/08/ryuks-return/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ransomware-hive-conti-avoslocker

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_susp_process_creation.yml)
