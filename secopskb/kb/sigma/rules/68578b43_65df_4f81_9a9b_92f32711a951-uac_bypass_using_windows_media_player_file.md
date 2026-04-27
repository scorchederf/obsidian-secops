---
sigma_id: "68578b43-65df-4f81-9a9b-92f32711a951"
title: "UAC Bypass Using Windows Media Player - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_wmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_wmp.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "68578b43-65df-4f81-9a9b-92f32711a951"
  - "UAC Bypass Using Windows Media Player - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of UAC Bypass using Windows Media Player osksupport.dll (UACMe 32)

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection1:
  TargetFilename|startswith: C:\Users\
  TargetFilename|endswith: \AppData\Local\Temp\OskSupport.dll
selection2:
  Image: C:\Windows\system32\DllHost.exe
  TargetFilename: C:\Program Files\Windows Media Player\osk.exe
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_wmp.yml)
