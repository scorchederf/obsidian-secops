---
sigma_id: "d474c8fe-bb69-4ea0-b7d9-f682b56d52d3"
title: "HackTool - Doppelanger LSASS Dumper Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml"
build_date: "2026-04-27 19:13:51"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d474c8fe-bb69-4ea0-b7d9-f682b56d52d3"
  - "HackTool - Doppelanger LSASS Dumper Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the Doppelanger hacktool which is used to dump LSASS memory via process cloning while evading common detection methods

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
- Image|endswith: \Doppelganger.exe
- Hashes|contains:
  - IMPHASH=AB94D5217896ADCD765A06B2D52F0AEB
  - IMPHASH=65F0EA61156EE0C2A35421926F0C7F78
condition: selection
```

## False Positives

- Unknown

## References

- https://labs.yarix.com/2025/06/doppelganger-an-advanced-lsass-dumper-with-process-cloning/
- https://github.com/vari-sh/RedTeamGrimoire/tree/668e0357072546065729ad623f8c02f7be21bb08/Doppelganger

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml)
