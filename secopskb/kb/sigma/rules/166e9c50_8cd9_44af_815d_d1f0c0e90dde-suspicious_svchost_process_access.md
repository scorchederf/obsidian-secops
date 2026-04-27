---
sigma_id: "166e9c50-8cd9-44af-815d-d1f0c0e90dde"
title: "Suspicious Svchost Process Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_svchost_susp_access_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_svchost_susp_access_request.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "166e9c50-8cd9-44af-815d-d1f0c0e90dde"
  - "Suspicious Svchost Process Access"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious access to the "svchost" process such as that used by Invoke-Phantom to kill the thread of the Windows event logging service.

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection:
  TargetImage|endswith: :\Windows\System32\svchost.exe
  GrantedAccess: '0x1F3FFF'
  CallTrace|contains: UNKNOWN
filter_main_msbuild:
  SourceImage|contains: :\Program Files\Microsoft Visual Studio\
  SourceImage|endswith: \MSBuild\Current\Bin\MSBuild.exe
  CallTrace|contains:
  - Microsoft.Build.ni.dll
  - System.ni.dll
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/hlldz/Invoke-Phant0m
- https://twitter.com/timbmsft/status/900724491076214784

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_svchost_susp_access_request.yml)
