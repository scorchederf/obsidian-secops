---
sigma_id: "eb2d07d4-49cb-4523-801a-da002df36602"
title: "HackTool - EDRSilencer Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_edrsilencer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_edrsilencer.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "eb2d07d4-49cb-4523-801a-da002df36602"
  - "HackTool - EDRSilencer Execution"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - EDRSilencer Execution

Detects the execution of EDRSilencer, a tool that leverages Windows Filtering Platform (WFP) to block Endpoint Detection and Response (EDR) agents from reporting security events to the server based on PE metadata information.

## Metadata

- Rule ID: eb2d07d4-49cb-4523-801a-da002df36602
- Status: test
- Level: high
- Author: @gott_cyber
- Date: 2024-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_edrsilencer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
- Image|endswith: \EDRSilencer.exe
- OriginalFileName: EDRSilencer.exe
- Description|contains: EDRSilencer
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/netero1010/EDRSilencer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_edrsilencer.yml)
