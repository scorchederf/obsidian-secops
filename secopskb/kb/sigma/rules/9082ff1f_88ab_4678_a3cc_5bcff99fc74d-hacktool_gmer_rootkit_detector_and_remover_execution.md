---
sigma_id: "9082ff1f-88ab-4678-a3cc-5bcff99fc74d"
title: "HackTool - GMER Rootkit Detector and Remover Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_gmer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_gmer.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9082ff1f-88ab-4678-a3cc-5bcff99fc74d"
  - "HackTool - GMER Rootkit Detector and Remover Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - GMER Rootkit Detector and Remover Execution

Detects the execution GMER tool based on image and hash fields.

## Metadata

- Rule ID: 9082ff1f-88ab-4678-a3cc-5bcff99fc74d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-05
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_gmer.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith: \gmer.exe
selection_sysmon_hash:
  Hashes|contains:
  - MD5=E9DC058440D321AA17D0600B3CA0AB04
  - SHA1=539C228B6B332F5AA523E5CE358C16647D8BBE57
  - SHA256=E8A3E804A96C716A3E9B69195DB6FFB0D33E2433AF871E4D4E1EAB3097237173
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- http://www.gmer.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_gmer.yml)
