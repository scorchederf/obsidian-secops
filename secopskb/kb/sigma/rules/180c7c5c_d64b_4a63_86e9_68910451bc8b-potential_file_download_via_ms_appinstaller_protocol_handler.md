---
sigma_id: "180c7c5c-d64b-4a63-86e9-68910451bc8b"
title: "Potential File Download Via MS-AppInstaller Protocol Handler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_ms_appinstaller_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ms_appinstaller_download.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "180c7c5c-d64b-4a63-86e9-68910451bc8b"
  - "Potential File Download Via MS-AppInstaller Protocol Handler"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential File Download Via MS-AppInstaller Protocol Handler

Detects usage of the "ms-appinstaller" protocol handler via command line to potentially download arbitrary files via AppInstaller.EXE
The downloaded files are temporarly stored in ":\Users\%username%\AppData\Local\Packages\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe\AC\INetCache\<RANDOM-8-CHAR-DIRECTORY>"

## Metadata

- Rule ID: 180c7c5c-d64b-4a63-86e9-68910451bc8b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel
- Date: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_ms_appinstaller_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ms-appinstaller://?source=
  - http
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/AppInstaller/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_ms_appinstaller_download.yml)
