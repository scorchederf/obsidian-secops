---
sigma_id: "b97cd4b1-30b8-4a9d-bd72-6293928d52bc"
title: "Indirect Command Execution By Program Compatibility Wizard"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pcwrun.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "b97cd4b1-30b8-4a9d-bd72-6293928d52bc"
  - "Indirect Command Execution By Program Compatibility Wizard"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Indirect Command Execution By Program Compatibility Wizard

Detect indirect command execution via Program Compatibility Assistant pcwrun.exe

## Metadata

- Rule ID: b97cd4b1-30b8-4a9d-bd72-6293928d52bc
- Status: test
- Level: low
- Author: A. Sungurov , oscd.community
- Date: 2020-10-12
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pcwrun.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \pcwrun.exe
condition: selection
```

## False Positives

- Need to use extra processing with 'unique_count' / 'filter' to focus on outliers as opposed to commonly seen artifacts
- Legit usage of scripts

## References

- https://twitter.com/pabraeken/status/991335019833708544
- https://lolbas-project.github.io/lolbas/Binaries/Pcwrun/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun.yml)
