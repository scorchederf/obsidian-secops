---
atomic_guid: "a8f6148d-478a-4f43-bc62-5efee9f931a4"
title: "Find Azure credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "a8f6148d-478a-4f43-bc62-5efee9f931a4"
  - "Find Azure credentials"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Find Azure credentials

Find local Azure credentials from file, defaults to using / as the look path.

## Metadata

- Atomic GUID: a8f6148d-478a-4f43-bc62-5efee9f931a4
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

```sh
find #{file_path}/.azure -name "msal_token_cache.json" -o -name "accessTokens.json" -type f 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
