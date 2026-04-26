---
sigma_id: "6812a10b-60ea-420c-832f-dfcc33b646ba"
title: "Potential PowerShell Execution Via DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_powershell_execution_via_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_powershell_execution_via_dll.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6812a10b-60ea-420c-832f-dfcc33b646ba"
  - "Potential PowerShell Execution Via DLL"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential PowerShell Execution Via DLL

Detects potential PowerShell execution from a DLL instead of the usual PowerShell process as seen used in PowerShdll.
This detection assumes that PowerShell commands are passed via the CommandLine.

## Metadata

- Rule ID: 6812a10b-60ea-420c-832f-dfcc33b646ba
- Status: test
- Level: high
- Author: Markus Neis, Nasreddine Bencherchali (Nextron Systems)
- Date: 2018-08-25
- Modified: 2024-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_susp_powershell_execution_via_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \InstallUtil.exe
  - \RegAsm.exe
  - \RegSvcs.exe
  - \regsvr32.exe
  - \rundll32.exe
- OriginalFileName:
  - InstallUtil.exe
  - RegAsm.exe
  - RegSvcs.exe
  - REGSVR32.EXE
  - RUNDLL32.EXE
selection_cli:
  CommandLine|contains:
  - Default.GetString
  - DownloadString
  - FromBase64String
  - 'ICM '
  - 'IEX '
  - Invoke-Command
  - Invoke-Expression
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/p3nt4/PowerShdll/blob/62cfa172fb4e1f7f4ac00ca942685baeb88ff356/README.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_powershell_execution_via_dll.yml)
