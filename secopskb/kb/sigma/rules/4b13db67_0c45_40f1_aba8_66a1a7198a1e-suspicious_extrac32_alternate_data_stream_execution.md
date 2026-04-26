---
sigma_id: "4b13db67-0c45-40f1-aba8-66a1a7198a1e"
title: "Suspicious Extrac32 Alternate Data Stream Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4b13db67-0c45-40f1-aba8-66a1a7198a1e"
  - "Suspicious Extrac32 Alternate Data Stream Execution"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Extrac32 Alternate Data Stream Execution

Extract data from cab file and hide it in an alternate data stream

## Metadata

- Rule ID: 4b13db67-0c45-40f1-aba8-66a1a7198a1e
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-26
- Modified: 2022-12-30
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - extrac32.exe
  - .cab
  CommandLine|re: :[^\\]
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Extrac32/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml)
