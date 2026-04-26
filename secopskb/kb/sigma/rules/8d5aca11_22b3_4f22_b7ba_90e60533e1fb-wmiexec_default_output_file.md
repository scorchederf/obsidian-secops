---
sigma_id: "8d5aca11-22b3-4f22-b7ba-90e60533e1fb"
title: "Wmiexec Default Output File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_wmiexec_default_filename.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmiexec_default_filename.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "8d5aca11-22b3-4f22-b7ba-90e60533e1fb"
  - "Wmiexec Default Output File"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Wmiexec Default Output File

Detects the creation of the default output filename used by the wmiexec tool

## Metadata

- Rule ID: 8d5aca11-22b3-4f22-b7ba-90e60533e1fb
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-02
- Modified: 2023-03-08
- Source Path: rules/windows/file/file_event/file_event_win_wmiexec_default_filename.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
- TargetFilename|re: \\Windows\\__1\d{9}\.\d{1,7}$
- TargetFilename|re: C:\\__1\d{9}\.\d{1,7}$
- TargetFilename|re: D:\\__1\d{9}\.\d{1,7}$
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.crowdstrike.com/blog/how-to-detect-and-prevent-impackets-wmiexec/
- https://github.com/fortra/impacket/blob/f4b848fa27654ca95bc0f4c73dbba8b9c2c9f30a/examples/wmiexec.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmiexec_default_filename.yml)
