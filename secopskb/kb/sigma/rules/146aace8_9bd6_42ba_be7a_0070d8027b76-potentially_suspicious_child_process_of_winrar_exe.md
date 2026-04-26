---
sigma_id: "146aace8-9bd6-42ba-be7a-0070d8027b76"
title: "Potentially Suspicious Child Process Of WinRAR.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrar_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_susp_child_process.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "146aace8-9bd6-42ba-be7a-0070d8027b76"
  - "Potentially Suspicious Child Process Of WinRAR.EXE"
attack_technique_ids:
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Child Process Of WinRAR.EXE

Detects potentially suspicious child processes of WinRAR.exe.

## Metadata

- Rule ID: 146aace8-9bd6-42ba-be7a-0070d8027b76
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-31
- Source Path: rules/windows/process_creation/proc_creation_win_winrar_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \WinRAR.exe
selection_binaries:
- Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- OriginalFileName:
  - Cmd.Exe
  - cscript.exe
  - mshta.exe
  - PowerShell.EXE
  - pwsh.dll
  - regsvr32.exe
  - RUNDLL32.EXE
  - wscript.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.group-ib.com/blog/cve-2023-38831-winrar-zero-day/
- https://github.com/knight0x07/WinRAR-Code-Execution-Vulnerability-CVE-2023-38831/blob/26ab6c40b6d2c09bb4fc60feaa4a3a90cfd20c23/Part-1-Overview.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrar_susp_child_process.yml)
