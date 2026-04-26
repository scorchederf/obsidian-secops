---
sigma_id: "e8d34729-86a4-4140-adfd-0a29c2106307"
title: "HackTool - CoercedPotato Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_coercedpotato.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_coercedpotato.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e8d34729-86a4-4140-adfd-0a29c2106307"
  - "HackTool - CoercedPotato Execution"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - CoercedPotato Execution

Detects the use of CoercedPotato, a tool for privilege escalation

## Metadata

- Rule ID: e8d34729-86a4-4140-adfd-0a29c2106307
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2023-10-11
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_coercedpotato.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection_loader_img:
  Image|endswith: \CoercedPotato.exe
selection_params:
  CommandLine|contains: ' --exploitId '
selection_loader_imphash:
  Hashes|contains:
  - IMPHASH=A75D7669DB6B2E107A44C4057FF7F7D6
  - IMPHASH=F91624350E2C678C5DCBE5E1F24E22C9
  - IMPHASH=14C81850A079A87E83D50CA41C709A15
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/hackvens/CoercedPotato
- https://blog.hackvens.fr/articles/CoercedPotato.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_coercedpotato.yml)
