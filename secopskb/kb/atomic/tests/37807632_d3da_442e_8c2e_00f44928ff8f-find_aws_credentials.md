---
atomic_guid: "37807632-d3da-442e-8c2e-00f44928ff8f"
title: "Find AWS credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "37807632-d3da-442e-8c2e-00f44928ff8f"
  - "Find AWS credentials"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find AWS credentials

Find local AWS credentials from file, defaults to using / as the look path.

## Metadata

- Atomic GUID: 37807632-d3da-442e-8c2e-00f44928ff8f
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Input Arguments

### file_path

- description: Path to search
- type: string
- default: /

## Executor

- name: sh

### Command

```bash
find #{file_path}/.aws -name "credentials" -type f 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
