---
sigma_id: "93199800-b52a-4dec-b762-75212c196542"
title: "PUA - RunXCmd Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_runxcmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_runxcmd.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "93199800-b52a-4dec-b762-75212c196542"
  - "PUA - RunXCmd Execution"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of the RunXCmd tool to execute commands with System or TrustedInstaller accounts

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

### Software Tags

- S0029

## Detection

```yaml
selection_account:
  CommandLine|contains:
  - ' /account=system '
  - ' /account=ti '
selection_exec:
  CommandLine|contains: /exec=
condition: all of selection_*
```

## False Positives

- Legitimate use by administrators

## References

- https://www.d7xtech.com/free-software/runx/
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_runxcmd.yml)
