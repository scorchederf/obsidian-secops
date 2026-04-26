---
sigma_id: "aa8e035d-7be4-48d3-a944-102aec04400d"
title: "Suspicious Extrac32 Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aa8e035d-7be4-48d3-a944-102aec04400d"
  - "Suspicious Extrac32 Execution"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Extrac32 Execution

Download or Copy file with Extrac32

## Metadata

- Rule ID: aa8e035d-7be4-48d3-a944-102aec04400d
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-26
- Modified: 2022-08-13
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_lolbas:
- CommandLine|contains: extrac32.exe
- Image|endswith: \extrac32.exe
- OriginalFileName: extrac32.exe
selection_archive:
  CommandLine|contains: .cab
selection_options:
  CommandLine|contains:
  - /C
  - /Y
  - ' \\\\'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Extrac32/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml)
