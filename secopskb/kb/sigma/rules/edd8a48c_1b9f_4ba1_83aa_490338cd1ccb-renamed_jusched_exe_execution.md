---
sigma_id: "edd8a48c-1b9f-4ba1-83aa-490338cd1ccb"
title: "Renamed Jusched.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_jusched.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_jusched.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "edd8a48c-1b9f-4ba1-83aa-490338cd1ccb"
  - "Renamed Jusched.EXE Execution"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed Jusched.EXE Execution

Detects the execution of a renamed "jusched.exe" as seen used by the cobalt group

## Metadata

- Rule ID: edd8a48c-1b9f-4ba1-83aa-490338cd1ccb
- Status: test
- Level: high
- Author: Markus Neis, Swisscom
- Date: 2019-06-04
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_jusched.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  Description:
  - Java Update Scheduler
  - Java(TM) Update Scheduler
filter:
  Image|endswith: \jusched.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.bitdefender.com/files/News/CaseStudies/study/262/Bitdefender-WhitePaper-An-APT-Blueprint-Gaining-New-Visibility-into-Financial-Threats-interactive.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_jusched.yml)
