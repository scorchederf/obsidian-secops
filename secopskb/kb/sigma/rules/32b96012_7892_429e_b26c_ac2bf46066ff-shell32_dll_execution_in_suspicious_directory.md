---
sigma_id: "32b96012-7892-429e-b26c-ac2bf46066ff"
title: "Shell32 DLL Execution in Suspicious Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_shell32_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_shell32_susp_execution.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "32b96012-7892-429e-b26c-ac2bf46066ff"
  - "Shell32 DLL Execution in Suspicious Directory"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Shell32 DLL Execution in Suspicious Directory

Detects shell32.dll executing a DLL in a suspicious directory

## Metadata

- Rule ID: 32b96012-7892-429e-b26c-ac2bf46066ff
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-11-24
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_shell32_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains|all:
  - shell32.dll
  - Control_RunDLL
  CommandLine|contains:
  - '%AppData%'
  - '%LocalAppData%'
  - '%Temp%'
  - '%tmp%'
  - \AppData\
  - \Temp\
  - \Users\Public\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.group-ib.com/resources/threat-research/red-curl-2.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_shell32_susp_execution.yml)
