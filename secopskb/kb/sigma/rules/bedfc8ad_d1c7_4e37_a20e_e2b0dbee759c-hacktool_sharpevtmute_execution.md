---
sigma_id: "bedfc8ad-d1c7-4e37-a20e-e2b0dbee759c"
title: "HackTool - SharpEvtMute Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bedfc8ad-d1c7-4e37-a20e-e2b0dbee759c"
  - "HackTool - SharpEvtMute Execution"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of SharpEvtHook, a tool that tampers with the Windows event logs

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection:
- Image|endswith: \SharpEvtMute.exe
- Description: SharpEvtMute
- CommandLine|contains:
  - '--Filter "rule '
  - --Encoded --Filter \"
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/bats3c/EvtMute

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml)
