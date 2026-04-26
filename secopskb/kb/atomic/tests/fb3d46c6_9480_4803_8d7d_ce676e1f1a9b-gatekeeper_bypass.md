---
atomic_guid: "fb3d46c6-9480-4803-8d7d-ce676e1f1a9b"
title: "Gatekeeper Bypass"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.001"
attack_technique_name: "Subvert Trust Controls: Gatekeeper Bypass"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.001/T1553.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "fb3d46c6-9480-4803-8d7d-ce676e1f1a9b"
  - "Gatekeeper Bypass"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Gatekeeper Bypass

Gatekeeper Bypass via command line

## Metadata

- Atomic GUID: fb3d46c6-9480-4803-8d7d-ce676e1f1a9b
- Technique: T1553.001: Subvert Trust Controls: Gatekeeper Bypass
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1553.001/T1553.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.001]]

## Input Arguments

### app_path

- description: Path to app to be used
- type: path
- default: myapp.app

## Executor

- name: sh

### Command

```bash
xattr -d com.apple.quarantine #{app_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.001/T1553.001.yaml)
