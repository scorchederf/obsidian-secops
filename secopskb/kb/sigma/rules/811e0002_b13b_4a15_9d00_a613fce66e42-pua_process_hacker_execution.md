---
sigma_id: "811e0002-b13b-4a15-9d00-a613fce66e42"
title: "PUA - Process Hacker Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_process_hacker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_process_hacker.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "811e0002-b13b-4a15-9d00-a613fce66e42"
  - "PUA - Process Hacker Execution"
attack_technique_ids:
  - "T1622"
  - "T1564"
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Process Hacker Execution

Detects the execution of Process Hacker based on binary metadata information (Image, Hash, Imphash, etc).
Process Hacker is a tool to view and manipulate processes, kernel options and other low level options.
Threat actors abused older vulnerable versions to manipulate system processes.

## Metadata

- Rule ID: 811e0002-b13b-4a15-9d00-a613fce66e42
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-10-10
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_pua_process_hacker.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1622-debugger_evasion|T1622]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
- Image|contains: \ProcessHacker_
- Image|endswith: \ProcessHacker.exe
- OriginalFileName:
  - ProcessHacker.exe
  - Process Hacker
- Description: Process Hacker
- Product: Process Hacker
- Hashes|contains:
  - MD5=68F9B52895F4D34E74112F3129B3B00D
  - MD5=B365AF317AE730A67C936F21432B9C71
  - SHA1=A0BDFAC3CE1880B32FF9B696458327CE352E3B1D
  - SHA1=C5E2018BF7C0F314FED4FD7FE7E69FA2E648359E
  - SHA256=D4A0FE56316A2C45B9BA9AC1005363309A3EDC7ACF9E4DF64D326A0FF273E80F
  - SHA256=BD2C2CF0631D881ED382817AFCCE2B093F4E412FFB170A719E2762F250ABFEA4
  - IMPHASH=3695333C60DEDECDCAFF1590409AA462
  - IMPHASH=04DE0AD9C37EB7BD52043D2ECAC958DF
condition: selection
```

## False Positives

- While sometimes 'Process Hacker is used by legitimate administrators, the execution of Process Hacker must be investigated and allowed on a case by case basis

## References

- https://processhacker.sourceforge.io/
- https://www.crowdstrike.com/blog/falcon-overwatch-report-finds-increase-in-ecrime/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_process_hacker.yml)
