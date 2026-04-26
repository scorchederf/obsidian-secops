---
sigma_id: "dfd2fcb7-8bd5-4daa-b132-5adb61d6ad45"
title: "Windows Hotfix Updates Reconnaissance Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_recon_hotfix.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_hotfix.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dfd2fcb7-8bd5-4daa-b132-5adb61d6ad45"
  - "Windows Hotfix Updates Reconnaissance Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Hotfix Updates Reconnaissance Via Wmic.EXE

Detects the execution of wmic with the "qfe" flag in order to obtain information about installed hotfix updates on the system. This is often used by pentester and attacker enumeration scripts

## Metadata

- Rule ID: dfd2fcb7-8bd5-4daa-b132-5adb61d6ad45
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_recon_hotfix.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- OriginalFileName: wmic.exe
- Image|endswith: \WMIC.exe
selection_cli:
  CommandLine|contains: ' qfe'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/carlospolop/PEASS-ng/blob/fa0f2e17fbc1d86f1fd66338a40e665e7182501d/winPEAS/winPEASbat/winPEAS.bat
- https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_recon_hotfix.yml)
