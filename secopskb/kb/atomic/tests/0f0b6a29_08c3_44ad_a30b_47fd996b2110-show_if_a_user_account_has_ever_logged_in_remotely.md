---
atomic_guid: "0f0b6a29-08c3-44ad-a30b-47fd996b2110"
title: "Show if a user account has ever logged in remotely"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-27 19:12:26"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Show if a user account has ever logged in remotely

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]

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
