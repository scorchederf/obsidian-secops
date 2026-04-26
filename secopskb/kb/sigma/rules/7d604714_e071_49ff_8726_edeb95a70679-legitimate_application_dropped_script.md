---
sigma_id: "7d604714-e071-49ff-8726-edeb95a70679"
title: "Legitimate Application Dropped Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_script.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "7d604714-e071-49ff-8726-edeb95a70679"
  - "Legitimate Application Dropped Script"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Legitimate Application Dropped Script

Detects programs on a Windows system that should not write scripts to disk

## Metadata

- Rule ID: 7d604714-e071-49ff-8726-edeb95a70679
- Status: test
- Level: high
- Author: frack113, Florian Roth (Nextron Systems)
- Date: 2022-08-21
- Modified: 2023-06-22
- Source Path: rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_script.yml

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
  - \eqnedt32.exe
  - \wordpad.exe
  - \wordview.exe
  - \certutil.exe
  - \certoc.exe
  - \CertReq.exe
  - \Desktopimgdownldr.exe
  - \esentutl.exe
  - \mshta.exe
  - \AcroRd32.exe
  - \RdrCEF.exe
  - \hh.exe
  - \finger.exe
  TargetFilename|endswith:
  - .ps1
  - .bat
  - .vbs
  - .scf
  - .wsf
  - .wsh
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Neo23x0/sysmon-config/blob/3f808d9c022c507aae21a9346afba4a59dd533b9/sysmonconfig-export-block.xml#L1326

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_script.yml)
