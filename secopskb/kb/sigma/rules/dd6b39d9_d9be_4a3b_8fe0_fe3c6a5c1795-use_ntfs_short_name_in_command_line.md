---
sigma_id: "dd6b39d9-d9be-4a3b-8fe0-fe3c6a5c1795"
title: "Use NTFS Short Name in Command Line"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_cli.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dd6b39d9-d9be-4a3b-8fe0-fe3c6a5c1795"
  - "Use NTFS Short Name in Command Line"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use NTFS Short Name in Command Line

Detect use of the Windows 8.3 short name. Which could be used as a method to avoid command-line detection

## Metadata

- Rule ID: dd6b39d9-d9be-4a3b-8fe0-fe3c6a5c1795
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-05
- Modified: 2022-09-21
- Source Path: rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ~1.exe
  - ~1.bat
  - ~1.msi
  - ~1.vbe
  - ~1.vbs
  - ~1.dll
  - ~1.ps1
  - ~1.js
  - ~1.hta
  - ~2.exe
  - ~2.bat
  - ~2.msi
  - ~2.vbe
  - ~2.vbs
  - ~2.dll
  - ~2.ps1
  - ~2.js
  - ~2.hta
filter:
- ParentImage|endswith:
  - \WebEx\WebexHost.exe
  - \thor\thor64.exe
- CommandLine|contains: C:\xampp\vcredist\VCREDI~1.EXE
condition: selection and not filter
```

## False Positives

- Applications could use this notation occasionally which might generate some false positives. In that case Investigate the parent and child process.

## References

- https://www.acunetix.com/blog/articles/windows-short-8-3-filenames-web-security-problem/
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc959352(v=technet.10)
- https://twitter.com/jonasLyk/status/1555914501802921984

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_cli.yml)
