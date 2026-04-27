---
sigma_id: "a1473adb-5338-4a20-b4c3-126763e2d3d3"
title: "Suspicious Advpack Call Via Rundll32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_advpack_obfuscated_ordinal_call.yml"
build_date: "2026-04-27 19:13:56"
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

Detects execution of "rundll32" calling "advpack.dll" with potential obfuscated ordinal calls in order to leverage the "RegisterOCX" function

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
