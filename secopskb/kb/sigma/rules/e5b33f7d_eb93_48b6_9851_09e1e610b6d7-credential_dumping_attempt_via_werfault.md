---
sigma_id: "e5b33f7d-eb93-48b6-9851-09e1e610b6d7"
title: "Credential Dumping Attempt Via WerFault"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_werfault.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_werfault.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "e5b33f7d-eb93-48b6-9851-09e1e610b6d7"
  - "Credential Dumping Attempt Via WerFault"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Credential Dumping Attempt Via WerFault

Detects process LSASS memory dump using Mimikatz, NanoDump, Invoke-Mimikatz, Procdump or Taskmgr based on the CallTrace pointing to ntdll.dll, dbghelp.dll or dbgcore.dll for win10, server2016 and up.

## Metadata

- Rule ID: e5b33f7d-eb93-48b6-9851-09e1e610b6d7
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2012-06-27
- Modified: 2023-11-29
- Source Path: rules/windows/process_access/proc_access_win_lsass_werfault.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0002

## Detection

```yaml
selection:
  SourceImage|endswith: \WerFault.exe
  TargetImage|endswith: \lsass.exe
  GrantedAccess: '0x1FFFFF'
condition: selection
```

## False Positives

- Actual failures in lsass.exe that trigger a crash dump (unlikely)
- Unknown cases in which WerFault accesses lsass.exe

## References

- https://github.com/helpsystems/nanodump/commit/578116faea3d278d53d70ea932e2bbfe42569507

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_werfault.yml)
