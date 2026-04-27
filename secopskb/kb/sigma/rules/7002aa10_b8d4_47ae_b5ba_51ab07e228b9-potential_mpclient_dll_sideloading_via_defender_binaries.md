---
sigma_id: "7002aa10-b8d4-47ae-b5ba-51ab07e228b9"
title: "Potential Mpclient.DLL Sideloading Via Defender Binaries"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mpcmdrun_dll_sideload_defender.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_dll_sideload_defender.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7002aa10-b8d4-47ae-b5ba-51ab07e228b9"
  - "Potential Mpclient.DLL Sideloading Via Defender Binaries"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Mpclient.DLL Sideloading Via Defender Binaries

Detects potential sideloading of "mpclient.dll" by Windows Defender processes ("MpCmdRun" and "NisSrv") from their non-default directory.

## Metadata

- Rule ID: 7002aa10-b8d4-47ae-b5ba-51ab07e228b9
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2022-08-01
- Modified: 2023-08-04
- Source Path: rules/windows/process_creation/proc_creation_win_mpcmdrun_dll_sideload_defender.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \MpCmdRun.exe
  - \NisSrv.exe
filter_main_known_locations:
  Image|startswith:
  - C:\Program Files (x86)\Windows Defender\
  - C:\Program Files\Microsoft Security Client\
  - C:\Program Files\Windows Defender\
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Windows\WinSxS\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_dll_sideload_defender.yml)
