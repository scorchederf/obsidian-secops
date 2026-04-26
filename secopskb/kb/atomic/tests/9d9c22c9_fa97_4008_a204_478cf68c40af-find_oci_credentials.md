---
atomic_guid: "9d9c22c9-fa97-4008-a204-478cf68c40af"
title: "Find OCI credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "9d9c22c9-fa97-4008-a204-478cf68c40af"
  - "Find OCI credentials"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find OCI credentials

Find local Oracle cloud credentials from file, defaults to using / as the look path.

## Metadata

- Atomic GUID: 9d9c22c9-fa97-4008-a204-478cf68c40af
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
find #{file_path}/.oci/sessions -name "token" -type f 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
