---
atomic_guid: "875805bc-9e86-4e87-be86-3a5527315cae"
title: "Network Share Discovery - linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "875805bc-9e86-4e87-be86-3a5527315cae"
  - "Network Share Discovery - linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Network Share Discovery - linux

Network Share Discovery using smbstatus

## Metadata

- Atomic GUID: 875805bc-9e86-4e87-be86-3a5527315cae
- Technique: T1135: Network Share Discovery
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Input Arguments

### package_checker

- description: Package checking command. Debian - dpkg -s samba
- type: string
- default: (rpm -q samba &>/dev/null) || (dpkg -s samba | grep -q installed)

### package_installer

- description: Package installer command. Debian - apt install samba
- type: string
- default: (which yum && yum -y install epel-release samba)||(which apt-get && DEBIAN_FRONTEND=noninteractive apt-get install -y samba)

## Dependencies

Package with smbstatus (samba) must exist on device

### Prerequisite Check

```bash
if #{package_checker} > /dev/null; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
#{package_installer}
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
smbstatus --shares
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
