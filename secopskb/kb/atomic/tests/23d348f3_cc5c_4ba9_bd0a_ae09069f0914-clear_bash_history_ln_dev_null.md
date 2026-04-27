---
atomic_guid: "23d348f3-cc5c-4ba9-bd0a-ae09069f0914"
title: "Clear Bash history (ln dev/null)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "23d348f3-cc5c-4ba9-bd0a-ae09069f0914"
  - "Clear Bash history (ln dev/null)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Clear Bash history (ln dev/null)

Clears bash history via a symlink to /dev/null

## Metadata

- Atomic GUID: 23d348f3-cc5c-4ba9-bd0a-ae09069f0914
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Input Arguments

### history_path

- description: Bash history path
- type: path
- default: ~/.bash_history

## Executor

- name: sh

### Command

```bash
ln -sf /dev/null #{history_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
