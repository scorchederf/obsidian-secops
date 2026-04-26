---
sigma_id: "0955e4e1-c281-4fb9-9ee1-5ee7b4b754d2"
title: "Use of Pcalua For Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0955e4e1-c281-4fb9-9ee1-5ee7b4b754d2"
  - "Use of Pcalua For Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of Pcalua For Execution

Detects execition of commands and binaries from the context of The program compatibility assistant (Pcalua.exe). This can be used as a LOLBIN in order to bypass application whitelisting.

## Metadata

- Rule ID: 0955e4e1-c281-4fb9-9ee1-5ee7b4b754d2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2022-06-14
- Modified: 2023-01-04
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: \pcalua.exe
  CommandLine|contains: ' -a'
condition: selection
```

## False Positives

- Legitimate use by a via a batch script or by an administrator.

## References

- https://lolbas-project.github.io/lolbas/Binaries/Pcalua/
- https://pentestlab.blog/2020/07/06/indirect-command-execution/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcalua.yml)
