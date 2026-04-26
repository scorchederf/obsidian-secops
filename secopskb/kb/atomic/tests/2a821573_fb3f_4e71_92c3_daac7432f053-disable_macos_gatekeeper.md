---
atomic_guid: "2a821573-fb3f-4e71-92c3-daac7432f053"
title: "Disable macOS Gatekeeper"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "2a821573-fb3f-4e71-92c3-daac7432f053"
  - "Disable macOS Gatekeeper"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable macOS Gatekeeper

Disables macOS Gatekeeper

## Metadata

- Atomic GUID: 2a821573-fb3f-4e71-92c3-daac7432f053
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: macos
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
sudo spctl --master-disable
```

### Cleanup

```sh
sudo spctl --master-enable
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
