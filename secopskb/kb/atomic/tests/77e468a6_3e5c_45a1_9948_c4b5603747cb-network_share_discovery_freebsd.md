---
atomic_guid: "77e468a6-3e5c-45a1-9948-c4b5603747cb"
title: "Network Share Discovery - FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "77e468a6-3e5c-45a1-9948-c4b5603747cb"
  - "Network Share Discovery - FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Network Share Discovery using smbstatus

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135: Network Share Discovery]]

## Input Arguments

### package_checker

- description: Package checking command. pkg info -x samba
- type: string
- default: (pkg info -x samba &>/dev/null)

### package_installer

- description: Package installer command. pkg install -y samba413
- type: string
- default: (which pkg && pkg install -y samba413)

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
- name: sh

### Command

```bash
smbstatus --shares
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
