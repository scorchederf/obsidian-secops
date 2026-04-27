---
sigma_id: "b9d9b652-d8ed-4697-89a2-a1186ee680ac"
title: "OSACompile Run-Only Execution"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_osacompile_runonly_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_osacompile_runonly_execution.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "b9d9b652-d8ed-4697-89a2-a1186ee680ac"
  - "OSACompile Run-Only Execution"
attack_technique_ids:
  - "T1059.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential suspicious run-only executions compiled using OSACompile

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - osacompile
  - ' -x '
  - ' -e '
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/applescript/
- https://ss64.com/osx/osacompile.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_osacompile_runonly_execution.yml)
