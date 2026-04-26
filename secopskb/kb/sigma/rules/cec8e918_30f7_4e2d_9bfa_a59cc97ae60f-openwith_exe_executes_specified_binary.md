---
sigma_id: "cec8e918-30f7-4e2d-9bfa-a59cc97ae60f"
title: "OpenWith.exe Executes Specified Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_openwith.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_openwith.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cec8e918-30f7-4e2d-9bfa-a59cc97ae60f"
  - "OpenWith.exe Executes Specified Binary"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OpenWith.exe Executes Specified Binary

The OpenWith.exe executes other binary

## Metadata

- Rule ID: cec8e918-30f7-4e2d-9bfa-a59cc97ae60f
- Status: test
- Level: high
- Author: Beyu Denis, oscd.community (rule), @harr0ey (idea)
- Date: 2019-10-12
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_openwith.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \OpenWith.exe
  CommandLine|contains: /c
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/blob/4db780e0f0b2e2bb8cb1fa13e09196da9b9f1834/yml/LOLUtilz/OSBinaries/Openwith.yml
- https://twitter.com/harr0ey/status/991670870384021504

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_openwith.yml)
