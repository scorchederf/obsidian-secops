---
sigma_id: "6b369ced-4b1d-48f1-b427-fdc0de0790bd"
title: "Suspicious Diantz Alternate Data Stream Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6b369ced-4b1d-48f1-b427-fdc0de0790bd"
  - "Suspicious Diantz Alternate Data Stream Execution"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Diantz Alternate Data Stream Execution

Compress target file into a cab file stored in the Alternate Data Stream (ADS) of the target file.

## Metadata

- Rule ID: 6b369ced-4b1d-48f1-b427-fdc0de0790bd
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-26
- Modified: 2022-12-31
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml

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
  - diantz.exe
  - .cab
  CommandLine|re: :[^\\]
condition: selection
```

## False Positives

- Very Possible

## References

- https://lolbas-project.github.io/lolbas/Binaries/Diantz/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml)
