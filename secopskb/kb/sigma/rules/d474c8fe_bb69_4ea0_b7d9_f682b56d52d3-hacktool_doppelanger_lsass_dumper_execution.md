---
sigma_id: "d474c8fe-bb69-4ea0-b7d9-f682b56d52d3"
title: "HackTool - Doppelanger LSASS Dumper Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml"
build_date: "2026-04-26 14:14:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Doppelanger LSASS Dumper Execution

Detects the execution of the Doppelanger hacktool which is used to dump LSASS memory via process cloning while evading common detection methods

## Metadata

- Rule ID: d474c8fe-bb69-4ea0-b7d9-f682b56d52d3
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-07-01
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_doppelganger.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

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
