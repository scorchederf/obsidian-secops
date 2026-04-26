---
sigma_id: "a96970af-f126-420d-90e1-d37bf25e50e1"
title: "Use Short Name Path in Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_path_use_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_path_use_image.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a96970af-f126-420d-90e1-d37bf25e50e1"
  - "Use Short Name Path in Image"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use Short Name Path in Image

Detect use of the Windows 8.3 short name. Which could be used as a method to avoid Image detection

## Metadata

- Rule ID: a96970af-f126-420d-90e1-d37bf25e50e1
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali
- Date: 2022-08-07
- Modified: 2025-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_path_use_image.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  Image|contains:
  - ~1\
  - ~2\
filter_main_system_process:
  ParentImage:
  - C:\Windows\System32\Dism.exe
  - C:\Windows\System32\cleanmgr.exe
filter_main_installers:
- Image|contains|all:
  - \AppData\
  - \Temp\
- Image|endswith:
  - ~1\unzip.exe
  - ~1\7zG.exe
filter_optional_webex:
  ParentImage|endswith: \WebEx\WebexHost.exe
filter_optional_thor:
  ParentImage|endswith: \thor\thor64.exe
filter_optional_installshield:
- Product: InstallShield (R)
- Description: InstallShield (R) Setup Engine
- Company: InstallShield Software Corporation
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Applications could use this notation occasionally which might generate some false positives. In that case Investigate the parent and child process.

## References

- https://www.acunetix.com/blog/articles/windows-short-8-3-filenames-web-security-problem/
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc959352(v=technet.10)
- https://twitter.com/frack113/status/1555830623633375232

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_path_use_image.yml)
