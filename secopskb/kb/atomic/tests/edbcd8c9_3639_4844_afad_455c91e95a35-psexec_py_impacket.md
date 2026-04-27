---
atomic_guid: "edbcd8c9-3639-4844-afad-455c91e95a35"
title: "psexec.py (Impacket)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "edbcd8c9-3639-4844-afad-455c91e95a35"
  - "psexec.py (Impacket)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# psexec.py (Impacket)

Will execute a command on the remote host with Impacket psexec.py script.

## Metadata

- Atomic GUID: edbcd8c9-3639-4844-afad-455c91e95a35
- Technique: T1569.002: System Services: Service Execution
- Platforms: linux
- Executor: bash
- Dependency Executor: bash
- Source Path: atomics/T1569.002/T1569.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Input Arguments

### command

- description: Command to execute in target computer
- type: string
- default: whoami

### domain

- description: Target domain
- type: string

### password

- description: Password
- type: string
- default: P@ssw0rd1

### remote_host

- description: Remote hostname or IP address
- type: string
- default: 127.0.0.1

### username

- description: Username
- type: string
- default: Administrator

## Dependencies

psexec.py (Impacket)

### Prerequisite Check

```bash
if [ -x "$(command -v psexec.py)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo pip3 install impacket
```

## Executor

- name: bash

### Command

```bash
psexec.py '#{domain}/#{username}:#{password}@#{remote_host}' '#{command}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
