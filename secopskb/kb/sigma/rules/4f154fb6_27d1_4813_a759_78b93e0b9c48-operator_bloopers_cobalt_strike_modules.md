---
sigma_id: "4f154fb6-27d1-4813-a759-78b93e0b9c48"
title: "Operator Bloopers Cobalt Strike Modules"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_modules.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_modules.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4f154fb6-27d1-4813-a759-78b93e0b9c48"
  - "Operator Bloopers Cobalt Strike Modules"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Operator Bloopers Cobalt Strike Modules

Detects Cobalt Strike module/commands accidentally entered in CMD shell

## Metadata

- Rule ID: 4f154fb6-27d1-4813-a759-78b93e0b9c48
- Status: test
- Level: high
- Author: _pete_0, TheDFIRReport
- Date: 2022-05-06
- Modified: 2023-01-30
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_modules.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection_img:
- OriginalFileName: Cmd.Exe
- Image|endswith: \cmd.exe
selection_cli:
  CommandLine|contains:
  - Invoke-UserHunter
  - Invoke-ShareFinder
  - Invoke-Kerberoast
  - Invoke-SMBAutoBrute
  - Invoke-Nightmare
  - zerologon
  - av_query
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/cobalt-4-5-user-guide.pdf
- https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/
- https://thedfirreport.com/2022/06/16/sans-ransomware-summit-2022-can-you-detect-this/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_bloopers_modules.yml)
