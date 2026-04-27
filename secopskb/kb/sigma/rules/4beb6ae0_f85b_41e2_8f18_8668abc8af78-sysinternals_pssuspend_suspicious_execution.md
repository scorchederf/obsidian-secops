---
sigma_id: "4beb6ae0-f85b-41e2-8f18-8668abc8af78"
title: "Sysinternals PsSuspend Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_susp_execution.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4beb6ae0-f85b-41e2-8f18-8668abc8af78"
  - "Sysinternals PsSuspend Suspicious Execution"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious execution of Sysinternals PsSuspend, where the utility is used to suspend critical processes such as AV or EDR to bypass defenses

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_img:
- OriginalFileName: pssuspend.exe
- Image|endswith:
  - \pssuspend.exe
  - \pssuspend64.exe
selection_cli:
  CommandLine|contains: msmpeng.exe
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/pssuspend
- https://twitter.com/0gtweet/status/1638069413717975046

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_pssuspend_susp_execution.yml)
