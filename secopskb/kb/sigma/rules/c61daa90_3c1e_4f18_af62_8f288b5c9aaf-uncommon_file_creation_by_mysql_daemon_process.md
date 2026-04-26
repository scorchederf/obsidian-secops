---
sigma_id: "c61daa90-3c1e-4f18-af62-8f288b5c9aaf"
title: "Uncommon File Creation By Mysql Daemon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_mysqld_uncommon_file_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_mysqld_uncommon_file_creation.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "c61daa90-3c1e-4f18-af62-8f288b5c9aaf"
  - "Uncommon File Creation By Mysql Daemon Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Uncommon File Creation By Mysql Daemon Process

Detects the creation of files with scripting or executable extensions by Mysql daemon.
Which could be an indicator of "User Defined Functions" abuse to download malware.

## Metadata

- Rule ID: c61daa90-3c1e-4f18-af62-8f288b5c9aaf
- Status: test
- Level: high
- Author: Joseph Kamau
- Date: 2024-05-27
- Source Path: rules/windows/file/file_event/file_event_win_mysqld_uncommon_file_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \mysqld.exe
  - \mysqld-nt.exe
  TargetFilename|endswith:
  - .bat
  - .dat
  - .dll
  - .exe
  - .ps1
  - .psm1
  - .vbe
  - .vbs
condition: selection
```

## False Positives

- Unknown

## References

- https://asec.ahnlab.com/en/58878/
- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/honeypot-recon-mysql-malware-infection-via-user-defined-functions-udf/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_mysqld_uncommon_file_creation.yml)
