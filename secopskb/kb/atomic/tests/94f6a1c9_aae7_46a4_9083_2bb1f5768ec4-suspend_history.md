---
atomic_guid: "94f6a1c9-aae7-46a4-9083-2bb1f5768ec4"
title: "Suspend History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "94f6a1c9-aae7-46a4-9083-2bb1f5768ec4"
  - "Suspend History"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspend History

suspend Shell History seen in Awfulshred wiper- https://unix.stackexchange.com/questions/10922/temporarily-suspend-bash-history-on-a-given-shell

## Metadata

- Atomic GUID: 94f6a1c9-aae7-46a4-9083-2bb1f5768ec4
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
set +o history
```

### Cleanup

```sh
set -o history
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
