---
sigma_id: "bbb7e38c-0b41-4a11-b306-d2a457b7ac2b"
title: "Suspicious File Created In PerfLogs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_perflogs_susp_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_perflogs_susp_files.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "bbb7e38c-0b41-4a11-b306-d2a457b7ac2b"
  - "Suspicious File Created In PerfLogs"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Created In PerfLogs

Detects suspicious file based on their extension being created in "C:\PerfLogs\". Note that this directory mostly contains ".etl" files

## Metadata

- Rule ID: bbb7e38c-0b41-4a11-b306-d2a457b7ac2b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_perflogs_susp_files.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\PerfLogs\
  TargetFilename|endswith:
  - .7z
  - .bat
  - .bin
  - .chm
  - .dll
  - .exe
  - .hta
  - .lnk
  - .ps1
  - .psm1
  - .py
  - .scr
  - .sys
  - .vbe
  - .vbs
  - .zip
condition: selection
```

## False Positives

- Unlikely

## References

- Internal Research
- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_perflogs_susp_files.yml)
