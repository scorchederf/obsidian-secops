---
sigma_id: "198effb6-6c98-4d0c-9ea3-451fa143c45c"
title: "Run Once Task Execution as Configured in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_runonce_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_runonce_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "198effb6-6c98-4d0c-9ea3-451fa143c45c"
  - "Run Once Task Execution as Configured in Registry"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Run Once Task Execution as Configured in Registry

This rule detects the execution of Run Once task as configured in the registry

## Metadata

- Rule ID: 198effb6-6c98-4d0c-9ea3-451fa143c45c
- Status: test
- Level: low
- Author: Avneet Singh @v3t0_, oscd.community, Christopher Peacock @SecurePeacock (updated)
- Date: 2020-10-18
- Modified: 2022-12-13
- Source Path: rules/windows/process_creation/proc_creation_win_runonce_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith: \runonce.exe
- Description: Run Once Wrapper
selection_cli:
- CommandLine|contains: /AlternateShellStartup
- CommandLine|endswith: /r
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/pabraeken/status/990717080805789697
- https://lolbas-project.github.io/lolbas/Binaries/Runonce/
- https://twitter.com/0gtweet/status/1602644163824156672?s=20&t=kuxbUnZPltpvFPZdCrqPXA

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_runonce_execution.yml)
