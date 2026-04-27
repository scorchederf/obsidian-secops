---
atomic_guid: "9e507bb8-1d30-4e3b-a49b-cb5727d7ea79"
title: "Extract Browser and System credentials with LaZagne"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "9e507bb8-1d30-4e3b-a49b-cb5727d7ea79"
  - "Extract Browser and System credentials with LaZagne"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Extract Browser and System credentials with LaZagne

[LaZagne Source](https://github.com/AlessandroZ/LaZagne)

## Metadata

- Atomic GUID: 9e507bb8-1d30-4e3b-a49b-cb5727d7ea79
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
python2 laZagne.py all
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
