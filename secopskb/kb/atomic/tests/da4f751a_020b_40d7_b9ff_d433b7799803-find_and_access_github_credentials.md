---
atomic_guid: "da4f751a-020b-40d7-b9ff-d433b7799803"
title: "Find and Access Github Credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "da4f751a-020b-40d7-b9ff-d433b7799803"
  - "Find and Access Github Credentials"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Find and Access Github Credentials

This test looks for .netrc files (which stores github credentials in clear text )and dumps its contents if found.

## Metadata

- Atomic GUID: da4f751a-020b-40d7-b9ff-d433b7799803
- Technique: T1552.001: Unsecured Credentials: Credentials In Files
- Platforms: linux, macos
- Executor: bash
- Elevation Required: False
- Source Path: atomics/T1552.001/T1552.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Input Arguments

### file_path

- description: Path to search
- type: string
- default: /home

## Executor

- elevation_required: False
- name: bash

### Command

```bash
for file in $(find #{file_path} -type f -name .netrc 2> /dev/null);do echo $file ; cat $file ; done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
