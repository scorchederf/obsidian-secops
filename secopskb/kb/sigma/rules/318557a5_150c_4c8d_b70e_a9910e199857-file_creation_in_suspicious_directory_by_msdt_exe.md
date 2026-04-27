---
sigma_id: "318557a5-150c-4c8d-b70e-a9910e199857"
title: "File Creation In Suspicious Directory By Msdt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_msdt_susp_directories.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_msdt_susp_directories.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "318557a5-150c-4c8d-b70e-a9910e199857"
  - "File Creation In Suspicious Directory By Msdt.EXE"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# File Creation In Suspicious Directory By Msdt.EXE

Detects msdt.exe creating files in suspicious directories which could be a sign of exploitation of either Follina or Dogwalk vulnerabilities

## Metadata

- Rule ID: 318557a5-150c-4c8d-b70e-a9910e199857
- Status: test
- Level: high
- Author: Vadim Varganov, Florian Roth (Nextron Systems)
- Date: 2022-08-24
- Modified: 2023-02-23
- Source Path: rules/windows/file/file_event/file_event_win_msdt_susp_directories.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  Image|endswith: \msdt.exe
  TargetFilename|contains:
  - \Desktop\
  - \Start Menu\Programs\Startup\
  - C:\PerfLogs\
  - C:\ProgramData\
  - C:\Users\Public\
condition: selection
```

## False Positives

- Unknown

## References

- https://irsl.medium.com/the-trouble-with-microsofts-troubleshooters-6e32fc80b8bd
- https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_msdt_susp_directories.yml)
