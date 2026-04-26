---
sigma_id: "654fcc6d-840d-4844-9b07-2c3300e54a26"
title: "Legitimate Application Dropped Archive"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_archive.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_archive.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "654fcc6d-840d-4844-9b07-2c3300e54a26"
  - "Legitimate Application Dropped Archive"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Legitimate Application Dropped Archive

Detects programs on a Windows system that should not write an archive to disk

## Metadata

- Rule ID: 654fcc6d-840d-4844-9b07-2c3300e54a26
- Status: test
- Level: high
- Author: frack113, Florian Roth
- Date: 2022-08-21
- Source Path: rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_archive.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith:
  - \winword.exe
  - \excel.exe
  - \powerpnt.exe
  - \msaccess.exe
  - \mspub.exe
  - \eqnedt32.exe
  - \visio.exe
  - \wordpad.exe
  - \wordview.exe
  - \certutil.exe
  - \certoc.exe
  - \CertReq.exe
  - \Desktopimgdownldr.exe
  - \esentutl.exe
  - \finger.exe
  - \notepad.exe
  - \AcroRd32.exe
  - \RdrCEF.exe
  - \mshta.exe
  - \hh.exe
  TargetFilename|endswith:
  - .zip
  - .rar
  - .7z
  - .diagcab
  - .appx
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Neo23x0/sysmon-config/blob/3f808d9c022c507aae21a9346afba4a59dd533b9/sysmonconfig-export-block.xml#L1326

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_archive.yml)
