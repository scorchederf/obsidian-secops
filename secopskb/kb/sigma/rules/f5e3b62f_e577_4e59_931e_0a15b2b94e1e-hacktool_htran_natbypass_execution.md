---
sigma_id: "f5e3b62f-e577-4e59-931e-0a15b2b94e1e"
title: "HackTool - Htran/NATBypass Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_htran_or_natbypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_htran_or_natbypass.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f5e3b62f-e577-4e59-931e-0a15b2b94e1e"
  - "HackTool - Htran/NATBypass Execution"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects executable names or flags used by Htran or Htran-like tools (e.g. NATBypass)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090: Proxy]]

### Software Tags

- S0040

## Detection

```yaml
selection_img:
  Image|endswith:
  - \htran.exe
  - \lcx.exe
selection_cli:
  CommandLine|contains:
  - '.exe -tran '
  - '.exe -slave '
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/HiwinCN/HTran
- https://github.com/cw1997/NATBypass

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_htran_or_natbypass.yml)
