---
sigma_id: "e1693bc8-7168-4eab-8718-cdcaa68a1738"
title: "Suspicious WMIC Execution Via Office Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_susp_execution_via_office_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_susp_execution_via_office_process.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e1693bc8-7168-4eab-8718-cdcaa68a1738"
  - "Suspicious WMIC Execution Via Office Process"
attack_technique_ids:
  - "T1204.002"
  - "T1047"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious WMIC Execution Via Office Process

Office application called wmic to proxye execution through a LOLBIN process. This is often used to break suspicious parent-child chain (Office app spawns LOLBin).

## Metadata

- Rule ID: e1693bc8-7168-4eab-8718-cdcaa68a1738
- Status: test
- Level: high
- Author: Vadim Khrykov, Cyb3rEng
- Date: 2021-08-23
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_susp_execution_via_office_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \WINWORD.EXE
  - \EXCEL.EXE
  - \POWERPNT.exe
  - \MSPUB.exe
  - \VISIO.exe
  - \MSACCESS.EXE
  - \EQNEDT32.EXE
  - \ONENOTE.EXE
  - \wordpad.exe
  - \wordview.exe
selection_wmic_img:
- Image|endswith: \wbem\WMIC.exe
- OriginalFileName: wmic.exe
selection_wmic_cli:
  CommandLine|contains|all:
  - process
  - create
  - call
  CommandLine|contains:
  - regsvr32
  - rundll32
  - msiexec
  - mshta
  - verclsid
  - wscript
  - cscript
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/
- https://github.com/vadim-hunter/Detection-Ideas-Rules/blob/02bcbfc2bfb8b4da601bb30de0344ae453aa1afe/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi_(aka_REvil)_Ransomware.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_susp_execution_via_office_process.yml)
