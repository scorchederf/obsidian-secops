---
sigma_id: "a6976974-ea6f-4e97-818e-ea08625c52cb"
title: "Potential RipZip Attack on Startup Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_ripzip_attack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ripzip_attack.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "a6976974-ea6f-4e97-818e-ea08625c52cb"
  - "Potential RipZip Attack on Startup Folder"
attack_technique_ids:
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential RipZip Attack on Startup Folder

Detects a phishing attack which expands a ZIP file containing a malicious shortcut.
If the victim expands the ZIP file via the explorer process, then the explorer process expands the malicious ZIP file and drops a malicious shortcut redirected to a backdoor into the Startup folder.
Additionally, the file name of the malicious shortcut in Startup folder contains {0AFACED1-E828-11D1-9187-B532F1E9575D} meaning the folder shortcut operation.

## Metadata

- Rule ID: a6976974-ea6f-4e97-818e-ea08625c52cb
- Status: test
- Level: high
- Author: Greg (rule)
- Date: 2022-07-21
- Modified: 2023-01-05
- Source Path: rules/windows/file/file_event/file_event_win_ripzip_attack.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - \Microsoft\Windows\Start Menu\Programs\Startup
  - .lnk.{0AFACED1-E828-11D1-9187-B532F1E9575D}
  Image|endswith: \explorer.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/jonasLyk/status/1549338335243534336?t=CrmPocBGLbDyE4p6zTX1cg&s=19

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ripzip_attack.yml)
