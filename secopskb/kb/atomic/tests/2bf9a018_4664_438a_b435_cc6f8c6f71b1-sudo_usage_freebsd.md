---
atomic_guid: "2bf9a018-4664-438a-b435-cc6f8c6f71b1"
title: "Sudo usage (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.003"
attack_technique_name: "Abuse Elevation Control Mechanism: Sudo and Sudo Caching"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "2bf9a018-4664-438a-b435-cc6f8c6f71b1"
  - "Sudo usage (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Common Sudo enumeration methods.

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]

## Dependencies

Check if sudo is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v sudo)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y sudo)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo -l      
sudo cat /usr/local/etc/sudoers
sudo ee /usr/local/etc/sudoers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml)
