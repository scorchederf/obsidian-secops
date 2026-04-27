---
atomic_guid: "0fc6e977-cb12-44f6-b263-2824ba917409"
title: "rsync remote file copy (push)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "0fc6e977-cb12-44f6-b263-2824ba917409"
  - "rsync remote file copy (push)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Utilize rsync to perform a remote file copy (push)

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### local_path

- description: Path of folder to copy
- type: path
- default: /tmp/adversary-rsync/

### remote_host

- description: Remote host to copy toward
- type: string
- default: victim-host

### remote_path

- description: Remote path to receive rsync
- type: path
- default: /tmp/victim-files

### username

- description: User account to authenticate on remote host
- type: string
- default: victim

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

- elevation_required: True
- name: sh

### Command

```bash
rsync -r #{local_path} #{username}@#{remote_host}:#{remote_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
