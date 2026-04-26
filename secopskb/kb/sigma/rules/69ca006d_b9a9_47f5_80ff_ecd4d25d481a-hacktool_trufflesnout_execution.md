---
sigma_id: "69ca006d-b9a9-47f5-80ff-ecd4d25d481a"
title: "HackTool - TruffleSnout Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_trufflesnout.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_trufflesnout.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "69ca006d-b9a9-47f5-80ff-ecd4d25d481a"
  - "HackTool - TruffleSnout Execution"
attack_technique_ids:
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - TruffleSnout Execution

Detects the use of TruffleSnout.exe an iterative AD discovery toolkit for offensive operators, situational awareness and targeted low noise enumeration.

## Metadata

- Rule ID: 69ca006d-b9a9-47f5-80ff-ecd4d25d481a
- Status: test
- Level: high
- Author: frack113
- Date: 2022-08-20
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_trufflesnout.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection:
- OriginalFileName: TruffleSnout.exe
- Image|endswith: \TruffleSnout.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1482/T1482.md
- https://github.com/dsnezhkov/TruffleSnout
- https://github.com/dsnezhkov/TruffleSnout/blob/7c2f22e246ef704bc96c396f66fa854e9ca742b9/TruffleSnout/Docs/USAGE.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_trufflesnout.yml)
