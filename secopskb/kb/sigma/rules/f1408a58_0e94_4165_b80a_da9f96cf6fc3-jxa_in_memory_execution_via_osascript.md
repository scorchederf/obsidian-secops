---
sigma_id: "f1408a58-0e94-4165-b80a-da9f96cf6fc3"
title: "JXA In-memory Execution Via OSAScript"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_jxa_in_memory_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jxa_in_memory_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "f1408a58-0e94-4165-b80a-da9f96cf6fc3"
  - "JXA In-memory Execution Via OSAScript"
attack_technique_ids:
  - "T1059.002"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# JXA In-memory Execution Via OSAScript

Detects possible malicious execution of JXA in-memory via OSAScript

## Metadata

- Rule ID: f1408a58-0e94-4165-b80a-da9f96cf6fc3
- Status: test
- Level: high
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-01-31
- Source Path: rules/macos/process_creation/proc_creation_macos_jxa_in_memory_execution.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_main:
  CommandLine|contains|all:
  - osascript
  - ' -e '
  - eval
  - NSData.dataWithContentsOfURL
selection_js:
- CommandLine|contains|all:
  - ' -l '
  - JavaScript
- CommandLine|contains: .js
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/applescript/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jxa_in_memory_execution.yml)
