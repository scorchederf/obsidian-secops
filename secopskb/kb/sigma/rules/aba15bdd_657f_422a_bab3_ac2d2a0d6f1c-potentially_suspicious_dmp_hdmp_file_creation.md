---
sigma_id: "aba15bdd-657f-422a-bab3-ac2d2a0d6f1c"
title: "Potentially Suspicious DMP/HDMP File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_dump_file_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dump_file_susp_creation.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "aba15bdd-657f-422a-bab3-ac2d2a0d6f1c"
  - "Potentially Suspicious DMP/HDMP File Creation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious DMP/HDMP File Creation

Detects the creation of a file with the ".dmp"/".hdmp" extension by a shell or scripting application such as "cmd", "powershell", etc. Often created by software during a crash. Memory dumps can sometimes contain sensitive information such as credentials. It's best to determine the source of the crash.

## Metadata

- Rule ID: aba15bdd-657f-422a-bab3-ac2d2a0d6f1c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-07
- Source Path: rules/windows/file/file_event/file_event_win_dump_file_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  TargetFilename|endswith:
  - .dmp
  - .dump
  - .hdmp
condition: selection
```

## False Positives

- Some administrative PowerShell or VB scripts might have the ability to collect dumps and move them to other folders which might trigger a false positive.

## References

- https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dump_file_susp_creation.yml)
