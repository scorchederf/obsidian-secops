---
atomic_guid: "0f0b6a29-08c3-44ad-a30b-47fd996b2110"
title: "Show if a user account has ever logged in remotely"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "0f0b6a29-08c3-44ad-a30b-47fd996b2110"
  - "Show if a user account has ever logged in remotely"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Show if a user account has ever logged in remotely

Show if a user account has ever logged in remotely

## Metadata

- Atomic GUID: 0f0b6a29-08c3-44ad-a30b-47fd996b2110
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1087.001/T1087.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1087.001.txt

## Dependencies

Check if lastlog command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v lastlog)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
sudo apt-get install login; exit 1;
```

## Executor

- name: sh

### Command

```bash
[ "$(uname)" = 'FreeBSD' ] && cmd="lastlogin" || cmd="lastlog" 
$cmd > #{output_file}
cat #{output_file}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
