---
sigma_id: "0cbe38c0-270c-41d9-ab79-6e5a9a669290"
title: "Trusted Path Bypass via Windows Directory Spoofing"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_win_trusted_path_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_trusted_path_bypass.yml"
build_date: "2026-04-26 14:14:38"
status: "experimental"
level: "high"
logsource: "windows / image_load"
aliases:
  - "0cbe38c0-270c-41d9-ab79-6e5a9a669290"
  - "Trusted Path Bypass via Windows Directory Spoofing"
attack_technique_ids:
  - "T1574.007"
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Trusted Path Bypass via Windows Directory Spoofing

Detects DLLs loading from a spoofed Windows directory path with an extra space (e.g "C:\Windows \System32") which can bypass Windows trusted path verification.
This technique tricks Windows into treating the path as trusted, allowing malicious DLLs to load with high integrity privileges bypassing UAC.

## Metadata

- Rule ID: 0cbe38c0-270c-41d9-ab79-6e5a9a669290
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-06-17
- Source Path: rules/windows/image_load/image_load_win_trusted_path_bypass.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.007]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ImageLoaded|contains:
  - :\Windows \System32\
  - :\Windows \SysWOW64\
condition: selection
```

## False Positives

- Unlikely

## References

- https://x.com/Wietze/status/1933495426952421843

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_trusted_path_bypass.yml)
