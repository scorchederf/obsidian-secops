---
sigma_id: "d292e0af-9a18-420c-9525-ec0ac3936892"
title: "Suspicious Java Children Processes"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_java_children.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_java_children.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "d292e0af-9a18-420c-9525-ec0ac3936892"
  - "Suspicious Java Children Processes"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Java Children Processes

Detects java process spawning suspicious children

## Metadata

- Rule ID: d292e0af-9a18-420c-9525-ec0ac3936892
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-03
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_java_children.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  ParentImage|endswith: /java
  CommandLine|contains:
  - /bin/sh
  - bash
  - dash
  - ksh
  - zsh
  - csh
  - fish
  - curl
  - wget
  - python
condition: selection
```

## False Positives

- Unknown

## References

- https://www.tecmint.com/different-types-of-linux-shells/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_java_children.yml)
