---
atomic_guid: "784e4011-bd1a-4ecd-a63a-8feb278512e6"
title: "Clear and Disable Bash History Logging"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.003"
attack_technique_name: "Indicator Removal on Host: Clear Command History"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "784e4011-bd1a-4ecd-a63a-8feb278512e6"
  - "Clear and Disable Bash History Logging"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Clear and Disable Bash History Logging

Clears the history and disable bash history logging of the current shell and future shell sessions

## Metadata

- Atomic GUID: 784e4011-bd1a-4ecd-a63a-8feb278512e6
- Technique: T1070.003: Indicator Removal on Host: Clear Command History
- Platforms: linux, macos
- Executor: bash
- Source Path: atomics/T1070.003/T1070.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.003]]

## Executor

- name: bash

### Command

```bash
set +o history
echo 'set +o history' >> ~/.bashrc
. ~/.bashrc
history -c
```

### Cleanup

```bash
sed -i 's/set +o history//g' ~/.bashrc
. ~/.bashrc
set -o history
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.003/T1070.003.yaml)
