---
sigma_id: "2d367498-5112-4ae5-a06a-96e7bc33a211"
title: "Suspicious Binary Writes Via AnyDesk"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_anydesk_writing_susp_binaries.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_anydesk_writing_susp_binaries.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "2d367498-5112-4ae5-a06a-96e7bc33a211"
  - "Suspicious Binary Writes Via AnyDesk"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects AnyDesk writing binary files to disk other than "gcapi.dll".
According to RedCanary research it is highly abnormal for AnyDesk to write executable files to disk besides gcapi.dll,
which is a legitimate DLL that is part of the Google Chrome web browser used to interact with the Google Cloud API. (See reference section for more details)

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]

## Detection

```yaml
selection:
  Image|endswith:
  - \AnyDesk.exe
  - \AnyDeskMSI.exe
  TargetFilename|endswith:
  - .dll
  - .exe
filter_dlls:
  TargetFilename|endswith: \gcapi.dll
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/
- https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_anydesk_writing_susp_binaries.yml)
