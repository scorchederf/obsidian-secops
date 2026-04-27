---
atomic_guid: "acb6b1ff-e2ad-4d64-806c-6c35fe73b951"
title: "Remote System Discovery - arp nix"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "acb6b1ff-e2ad-4d64-806c-6c35fe73b951"
  - "Remote System Discovery - arp nix"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote System Discovery - arp nix

Identify remote systems via arp.

Upon successful execution, sh will execute arp to list out the arp cache. Output will be via stdout.

## Metadata

- Atomic GUID: acb6b1ff-e2ad-4d64-806c-6c35fe73b951
- Technique: T1018: Remote System Discovery
- Platforms: linux, macos
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Dependencies

Check if arp command exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v arp)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
(which yum && yum -y install net-tools)||(which apt-get && apt-get install -y net-tools)
```

## Executor

- name: sh

### Command

```bash
arp -a | grep -v '^?'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
