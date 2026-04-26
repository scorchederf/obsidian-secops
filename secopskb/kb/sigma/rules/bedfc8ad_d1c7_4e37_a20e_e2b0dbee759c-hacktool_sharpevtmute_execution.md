---
sigma_id: "bedfc8ad-d1c7-4e37-a20e-e2b0dbee759c"
title: "HackTool - SharpEvtMute Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml"
build_date: "2026-04-26 15:01:45"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SharpEvtMute Execution

Detects the use of SharpEvtHook, a tool that tampers with the Windows event logs

## Metadata

- Rule ID: bedfc8ad-d1c7-4e37-a20e-e2b0dbee759c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-07
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpevtmute.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

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
