---
atomic_guid: "f564c297-7978-4aa9-b37a-d90477feea4e"
title: "sftp remote file copy (push)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "f564c297-7978-4aa9-b37a-d90477feea4e"
  - "sftp remote file copy (push)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# sftp remote file copy (push)

Utilize sftp to perform a remote file copy (push)

## Metadata

- Atomic GUID: f564c297-7978-4aa9-b37a-d90477feea4e
- Technique: T1105: Ingress Tool Transfer
- Platforms: linux, macos
- Executor: bash
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_file

- description: Path of file to copy
- type: path
- default: /tmp/adversary-sftp

### remote_host

- description: Remote host to copy toward
- type: string
- default: victim-host

### remote_path

- description: Remote path to receive sftp
- type: path
- default: /tmp/victim-files/

### username

- description: User account to authenticate on remote host
- type: string
- default: victim

## Executor

- name: bash

### Command

```bash
sftp #{username}@#{remote_host}:#{remote_path} <<< $'put #{local_file}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
