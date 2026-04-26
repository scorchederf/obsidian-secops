---
sigma_id: "f0540f7e-2db3-4432-b9e0-3965486744bc"
title: "Legitimate Application Dropped Executable"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_exe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_exe.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "f0540f7e-2db3-4432-b9e0-3965486744bc"
  - "Legitimate Application Dropped Executable"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Legitimate Application Dropped Executable

Detects programs on a Windows system that should not write executables to disk

## Metadata

- Rule ID: f0540f7e-2db3-4432-b9e0-3965486744bc
- Status: test
- Level: high
- Author: frack113, Florian Roth (Nextron Systems)
- Date: 2022-08-21
- Modified: 2023-06-22
- Source Path: rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_exe.yml

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
  - .exe
  - .dll
  - .ocx
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Neo23x0/sysmon-config/blob/3f808d9c022c507aae21a9346afba4a59dd533b9/sysmonconfig-export-block.xml#L1326

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_legitimate_app_dropping_exe.yml)
