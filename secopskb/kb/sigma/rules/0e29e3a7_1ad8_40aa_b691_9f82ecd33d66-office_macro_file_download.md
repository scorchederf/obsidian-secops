---
sigma_id: "0e29e3a7-1ad8-40aa-b691-9f82ecd33d66"
title: "Office Macro File Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_macro_files_downloaded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_downloaded.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "0e29e3a7-1ad8-40aa-b691-9f82ecd33d66"
  - "Office Macro File Download"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Macro File Download

Detects the creation of a new office macro files on the system via an application (browser, mail client).
This can help identify potential malicious activity, such as the download of macro-enabled documents that could be used for exploitation.

## Metadata

- Rule ID: 0e29e3a7-1ad8-40aa-b691-9f82ecd33d66
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-23
- Modified: 2025-10-29
- Source Path: rules/windows/file/file_event/file_event_win_office_macro_files_downloaded.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection_processes:
  Image|endswith:
  - \RuntimeBroker.exe
  - \outlook.exe
  - \thunderbird.exe
  - \brave.exe
  - \chrome.exe
  - \firefox.exe
  - \iexplore.exe
  - \maxthon.exe
  - \MicrosoftEdge.exe
  - \msedge.exe
  - \msedgewebview2.exe
  - \opera.exe
  - \safari.exe
  - \seamonkey.exe
  - \vivaldi.exe
  - \whale.exe
selection_ext:
- TargetFilename|endswith:
  - .docm
  - .dotm
  - .xlsm
  - .xltm
  - .potm
  - .pptm
- TargetFilename|contains:
  - .docm:Zone
  - .dotm:Zone
  - .xlsm:Zone
  - .xltm:Zone
  - .potm:Zone
  - .pptm:Zone
condition: all of selection_*
```

## False Positives

- Legitimate macro files downloaded from the internet
- Legitimate macro files sent as attachments via emails

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1566.001/T1566.001.md
- https://learn.microsoft.com/en-us/deployoffice/compat/office-file-format-reference

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_macro_files_downloaded.yml)
