---
sigma_id: "3ef5605c-9eb9-47b0-9a71-b727e6aa5c3b"
title: "Use NTFS Short Name in Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_image.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3ef5605c-9eb9-47b0-9a71-b727e6aa5c3b"
  - "Use NTFS Short Name in Image"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use NTFS Short Name in Image

Detect use of the Windows 8.3 short name. Which could be used as a method to avoid Image based detection

## Metadata

- Rule ID: 3ef5605c-9eb9-47b0-9a71-b727e6aa5c3b
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-06
- Modified: 2023-07-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_image.yml

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
  - ~1.bat
  - ~1.dll
  - ~1.exe
  - ~1.hta
  - ~1.js
  - ~1.msi
  - ~1.ps1
  - ~1.tmp
  - ~1.vbe
  - ~1.vbs
  - ~2.bat
  - ~2.dll
  - ~2.exe
  - ~2.hta
  - ~2.js
  - ~2.msi
  - ~2.ps1
  - ~2.tmp
  - ~2.vbe
  - ~2.vbs
filter_main_generic_parent:
  ParentImage: C:\Windows\explorer.exe
filter_optional_webex:
  ParentImage|endswith: \WebEx\WebexHost.exe
filter_optional_thor:
  ParentImage|endswith: \thor\thor64.exe
filter_optional_winzip:
  Image: C:\PROGRA~1\WinZip\WZPREL~1.EXE
filter_optional_vcred:
  Image|endswith: \VCREDI~1.EXE
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Software Installers

## References

- https://www.acunetix.com/blog/articles/windows-short-8-3-filenames-web-security-problem/
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc959352(v=technet.10)
- https://twitter.com/jonasLyk/status/1555914501802921984

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ntfs_short_name_use_image.yml)
