---
sigma_id: "a1473adb-5338-4a20-b4c3-126763e2d3d3"
title: "Suspicious Advpack Call Via Rundll32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a1473adb-5338-4a20-b4c3-126763e2d3d3"
  - "Suspicious Advpack Call Via Rundll32.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Advpack Call Via Rundll32.EXE

Detects execution of "rundll32" calling "advpack.dll" with potential obfuscated ordinal calls in order to leverage the "RegisterOCX" function

## Metadata

- Rule ID: a1473adb-5338-4a20-b4c3-126763e2d3d3
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-17
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
- CommandLine|contains: rundll32
selection_cli_dll:
  CommandLine|contains: advpack
selection_cli_ordinal:
- CommandLine|contains|all:
  - '#+'
  - '12'
- CommandLine|contains: '#-'
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://twitter.com/Hexacorn/status/1224848930795552769
- http://www.hexacorn.com/blog/2020/02/05/stay-positive-lolbins-not/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml)
