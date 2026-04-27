---
sigma_id: "b447f7de-1e53-4cbf-bfb4-f1f6d0b04e4e"
title: "Suspicious Binaries and Scripts in Public Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_public_folder_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_public_folder_extension.yml"
build_date: "2026-04-26 17:03:22"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "b447f7de-1e53-4cbf-bfb4-f1f6d0b04e4e"
  - "Suspicious Binaries and Scripts in Public Folder"
attack_technique_ids:
  - "T1204"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Binaries and Scripts in Public Folder

Detects the creation of a file with a suspicious extension in the public folder, which could indicate potential malicious activity.

## Metadata

- Rule ID: b447f7de-1e53-4cbf-bfb4-f1f6d0b04e4e
- Status: experimental
- Level: high
- Author: The DFIR Report
- Date: 2025-01-23
- Source Path: rules/windows/file/file_event/file_event_win_susp_public_folder_extension.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204]]

## Detection

```yaml
selection:
  TargetFilename|contains: :\Users\Public\
  TargetFilename|endswith:
  - .bat
  - .dll
  - .exe
  - .hta
  - .js
  - .ps1
  - .vbe
  - .vbs
condition: selection
```

## False Positives

- Administrators deploying legitimate binaries to public folders.

## References

- https://intel.thedfirreport.com/events/view/30032
- https://intel.thedfirreport.com/eventReports/view/70
- https://thedfirreport.com/2025/01/27/cobalt-strike-and-a-pair-of-socks-lead-to-lockbit-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_public_folder_extension.yml)
