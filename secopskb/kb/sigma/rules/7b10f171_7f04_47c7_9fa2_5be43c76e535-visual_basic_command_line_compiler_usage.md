---
sigma_id: "7b10f171-7f04-47c7-9fa2-5be43c76e535"
title: "Visual Basic Command Line Compiler Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7b10f171-7f04-47c7-9fa2-5be43c76e535"
  - "Visual Basic Command Line Compiler Usage"
attack_technique_ids:
  - "T1027.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Visual Basic Command Line Compiler Usage

Detects successful code compilation via Visual Basic Command Line Compiler that utilizes Windows Resource to Object Converter.

## Metadata

- Rule ID: 7b10f171-7f04-47c7-9fa2-5be43c76e535
- Status: test
- Level: high
- Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
- Date: 2020-10-07
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Detection

```yaml
selection:
  ParentImage|endswith: \vbc.exe
  Image|endswith: \cvtres.exe
condition: selection
```

## False Positives

- Utilization of this tool should not be seen in enterprise environment

## References

- https://lolbas-project.github.io/lolbas/Binaries/Vbc/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml)
