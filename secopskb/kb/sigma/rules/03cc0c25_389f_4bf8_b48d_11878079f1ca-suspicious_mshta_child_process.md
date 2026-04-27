---
sigma_id: "03cc0c25-389f-4bf8-b48d-11878079f1ca"
title: "Suspicious MSHTA Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_child_processes.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "03cc0c25-389f-4bf8-b48d-11878079f1ca"
  - "Suspicious MSHTA Child Process"
attack_technique_ids:
  - "T1218.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious MSHTA Child Process

Detects a suspicious process spawning from an "mshta.exe" process, which could be indicative of a malicious HTA script execution

## Metadata

- Rule ID: 03cc0c25-389f-4bf8-b48d-11878079f1ca
- Status: test
- Level: high
- Author: Michael Haag
- Date: 2019-01-16
- Modified: 2023-02-06
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \mshta.exe
selection_child:
- Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  - \cscript.exe
  - \sh.exe
  - \bash.exe
  - \reg.exe
  - \regsvr32.exe
  - \bitsadmin.exe
- OriginalFileName:
  - Cmd.Exe
  - PowerShell.EXE
  - pwsh.dll
  - wscript.exe
  - cscript.exe
  - Bash.exe
  - reg.exe
  - REGSVR32.EXE
  - bitsadmin.exe
condition: all of selection*
```

## False Positives

- Printer software / driver installations
- HP software

## References

- https://www.trustedsec.com/july-2015/malicious-htas/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_susp_child_processes.yml)
