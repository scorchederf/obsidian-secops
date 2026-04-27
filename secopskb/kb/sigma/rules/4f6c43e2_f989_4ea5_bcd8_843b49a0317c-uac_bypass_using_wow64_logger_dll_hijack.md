---
sigma_id: "4f6c43e2-f989-4ea5-bcd8-843b49a0317c"
title: "UAC Bypass Using WOW64 Logger DLL Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_uac_bypass_wow64_logger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_uac_bypass_wow64_logger.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "4f6c43e2-f989-4ea5-bcd8-843b49a0317c"
  - "UAC Bypass Using WOW64 Logger DLL Hijack"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UAC Bypass Using WOW64 Logger DLL Hijack

Detects the pattern of UAC Bypass using a WoW64 logger DLL hijack (UACMe 30)

## Metadata

- Rule ID: 4f6c43e2-f989-4ea5-bcd8-843b49a0317c
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-23
- Modified: 2022-10-09
- Source Path: rules/windows/process_access/proc_access_win_uac_bypass_wow64_logger.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  SourceImage|contains: :\Windows\SysWOW64\
  GrantedAccess: '0x1fffff'
  CallTrace|startswith: UNKNOWN(0000000000000000)|UNKNOWN(0000000000000000)|
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/hfiref0x/UACME

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_uac_bypass_wow64_logger.yml)
