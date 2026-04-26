---
atomic_guid: "5bcefe5f-3f30-4f1c-a61a-8d7db3f4450c"
title: "File download via nscurl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "5bcefe5f-3f30-4f1c-a61a-8d7db3f4450c"
  - "File download via nscurl"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File download via nscurl

Use nscurl to download and write a file/payload from the internet.
-k = Disable certificate checking
-o = Output destination

## Metadata

- Atomic GUID: 5bcefe5f-3f30-4f1c-a61a-8d7db3f4450c
- Technique: T1105: Ingress Tool Transfer
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### destination_path

- description: Local path to place remote file
- type: path
- default: license.txt

### remote_file

- description: URL of remote file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- elevation_required: False
- name: sh

### Command

```sh
nscurl -k "#{remote_file}" -o "#{destination_path}"
```

### Cleanup

```sh
rm "#{destination_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
