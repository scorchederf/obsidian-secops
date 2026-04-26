---
sigma_id: "f956c7c1-0f60-4bc5-b7d7-b39ab3c08908"
title: "PktMon.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pktmon_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pktmon_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f956c7c1-0f60-4bc5-b7d7-b39ab3c08908"
  - "PktMon.EXE Execution"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PktMon.EXE Execution

Detects execution of PktMon, a tool that captures network packets.

## Metadata

- Rule ID: f956c7c1-0f60-4bc5-b7d7-b39ab3c08908
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-17
- Modified: 2023-06-23
- Source Path: rules/windows/process_creation/proc_creation_win_pktmon_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection:
- Image|endswith: \pktmon.exe
- OriginalFileName: PktMon.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://lolbas-project.github.io/lolbas/Binaries/Pktmon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pktmon_execution.yml)
