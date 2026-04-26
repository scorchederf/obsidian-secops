---
atomic_guid: "53b03a54-4529-4992-852d-a00b4b7215a6"
title: "Use Space Before Command to Avoid Logging to History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "53b03a54-4529-4992-852d-a00b4b7215a6"
  - "Use Space Before Command to Avoid Logging to History"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Use Space Before Command to Avoid Logging to History

Using a space before a command causes the command to not be logged in the Bash History file

## Metadata

- Atomic GUID: 53b03a54-4529-4992-852d-a00b4b7215a6
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Executor

- name: sh

### Command

```bash
hostname
whoami
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
