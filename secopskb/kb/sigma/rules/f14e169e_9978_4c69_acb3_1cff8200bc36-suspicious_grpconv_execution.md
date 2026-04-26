---
sigma_id: "f14e169e-9978-4c69-acb3-1cff8200bc36"
title: "Suspicious GrpConv Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_susp_grpconv.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_grpconv.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f14e169e-9978-4c69-acb3-1cff8200bc36"
  - "Suspicious GrpConv Execution"
attack_technique_ids:
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious GrpConv Execution

Detects the suspicious execution of a utility to convert Windows 3.x .grp files or for persistence purposes by malicious software or actors

## Metadata

- Rule ID: f14e169e-9978-4c69-acb3-1cff8200bc36
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-19
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_susp_grpconv.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - grpconv.exe -o
  - grpconv -o
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1526833181831200770

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_grpconv.yml)
