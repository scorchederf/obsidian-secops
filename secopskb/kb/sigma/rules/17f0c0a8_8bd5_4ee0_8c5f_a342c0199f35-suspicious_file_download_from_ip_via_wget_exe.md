---
sigma_id: "17f0c0a8-8bd5-4ee0-8c5f-a342c0199f35"
title: "Suspicious File Download From IP Via Wget.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wget_download_direct_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_direct_ip.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "17f0c0a8-8bd5-4ee0-8c5f-a342c0199f35"
  - "Suspicious File Download From IP Via Wget.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious File Download From IP Via Wget.EXE

Detects potentially suspicious file downloads directly from IP addresses using Wget.exe

## Metadata

- Rule ID: 17f0c0a8-8bd5-4ee0-8c5f-a342c0199f35
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Source Path: rules/windows/process_creation/proc_creation_win_wget_download_direct_ip.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \wget.exe
- OriginalFileName: wget.exe
selection_ip:
  CommandLine|re: ://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
selection_http:
  CommandLine|contains: http
selection_flag:
- CommandLine|re: \s-O\s
- CommandLine|contains: --output-document
selection_ext:
  CommandLine|endswith:
  - .ps1
  - .ps1'
  - .ps1"
  - .dat
  - .dat'
  - .dat"
  - .msi
  - .msi'
  - .msi"
  - .bat
  - .bat'
  - .bat"
  - .exe
  - .exe'
  - .exe"
  - .vbs
  - .vbs'
  - .vbs"
  - .vbe
  - .vbe'
  - .vbe"
  - .hta
  - .hta'
  - .hta"
  - .dll
  - .dll'
  - .dll"
  - .psm1
  - .psm1'
  - .psm1"
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.gnu.org/software/wget/manual/wget.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_direct_ip.yml)
