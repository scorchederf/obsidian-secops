---
sigma_id: "e13f668e-7f95-443d-98d2-1816a7648a7b"
title: "Detected Windows Software Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_software_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_software_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e13f668e-7f95-443d-98d2-1816a7648a7b"
  - "Detected Windows Software Discovery"
attack_technique_ids:
  - "T1518"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Detected Windows Software Discovery

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable.

## Metadata

- Rule ID: e13f668e-7f95-443d-98d2-1816a7648a7b
- Status: test
- Level: medium
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-16
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_reg_software_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - query
  - \software\
  - /v
  - svcversion
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518/T1518.md
- https://github.com/harleyQu1nn/AggressorScripts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_software_discovery.yml)
