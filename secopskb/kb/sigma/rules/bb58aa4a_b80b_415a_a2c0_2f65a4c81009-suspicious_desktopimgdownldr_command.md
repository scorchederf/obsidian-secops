---
sigma_id: "bb58aa4a-b80b-415a-a2c0-2f65a4c81009"
title: "Suspicious Desktopimgdownldr Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bb58aa4a-b80b-415a-a2c0-2f65a4c81009"
  - "Suspicious Desktopimgdownldr Command"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious Microsoft desktopimgdownldr execution with parameters used to download files from the Internet

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection1:
  CommandLine|contains: ' /lockscreenurl:'
selection1_filter:
  CommandLine|contains:
  - .jpg
  - .jpeg
  - .png
selection_reg:
  CommandLine|contains|all:
  - reg delete
  - \PersonalizationCSP
condition: ( selection1 and not selection1_filter ) or selection_reg
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/
- https://twitter.com/SBousseaden/status/1278977301745741825

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml)
