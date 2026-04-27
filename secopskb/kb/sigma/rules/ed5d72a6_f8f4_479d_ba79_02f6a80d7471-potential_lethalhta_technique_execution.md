---
sigma_id: "ed5d72a6-f8f4-479d-ba79-02f6a80d7471"
title: "Potential LethalHTA Technique Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ed5d72a6-f8f4-479d-ba79-02f6a80d7471"
  - "Potential LethalHTA Technique Execution"
attack_technique_ids:
  - "T1218.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential LethalHTA Technique Execution

Detects potential LethalHTA technique where the "mshta.exe" is spawned by an "svchost.exe" process

## Metadata

- Rule ID: ed5d72a6-f8f4-479d-ba79-02f6a80d7471
- Status: test
- Level: high
- Author: Markus Neis
- Date: 2018-06-07
- Modified: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Detection

```yaml
selection:
  ParentImage|endswith: \svchost.exe
  Image|endswith: \mshta.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://codewhitesec.blogspot.com/2018/07/lethalhta.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_lethalhta_technique.yml)
