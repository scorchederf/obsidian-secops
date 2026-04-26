---
sigma_id: "b18c9d4c-fac9-4708-bd06-dd5bfacf200f"
title: "HackTool - F-Secure C3 Load by Rundll32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_c3_rundll32_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_c3_rundll32_pattern.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "b18c9d4c-fac9-4708-bd06-dd5bfacf200f"
  - "HackTool - F-Secure C3 Load by Rundll32"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - F-Secure C3 Load by Rundll32

F-Secure C3 produces DLLs with a default exported StartNodeRelay function.

## Metadata

- Rule ID: b18c9d4c-fac9-4708-bd06-dd5bfacf200f
- Status: test
- Level: critical
- Author: Alfie Champion (ajpc500)
- Date: 2021-06-02
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_c3_rundll32_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - rundll32.exe
  - .dll
  - StartNodeRelay
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/FSecureLABS/C3/blob/11a081fd3be2aaf2a879f6b6e9a96ecdd24966ef/Src/NodeRelayDll/NodeRelayDll.cpp#L12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_c3_rundll32_pattern.yml)
