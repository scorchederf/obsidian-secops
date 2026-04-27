---
sigma_id: "41bb431f-56d8-4691-bb56-ed34e390906f"
title: "UAC Bypass Using MSConfig Token Modification - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "41bb431f-56d8-4691-bb56-ed34e390906f"
  - "UAC Bypass Using MSConfig Token Modification - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of UAC Bypass using a msconfig GUI hack (UACMe 55)

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Users\
  TargetFilename|endswith: \AppData\Local\Temp\pkgmgr.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_msconfig_gui.yml)
