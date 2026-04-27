---
atomic_guid: "952931a4-af0b-4335-bbbe-73c8c5b327ae"
title: "Permission Groups Discovery (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.001"
attack_technique_name: "Permission Groups Discovery: Local Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "952931a4-af0b-4335-bbbe-73c8c5b327ae"
  - "Permission Groups Discovery (Local)"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Permission Groups Discovery

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]

## Executor

- name: sh

### Command

```bash
if [ -x "$(command -v dscacheutil)" ]; then dscacheutil -q group; else echo "dscacheutil is missing from the machine. skipping..."; fi;
if [ -x "$(command -v dscl)" ]; then dscl . -list /Groups; else echo "dscl is missing from the machine. skipping..."; fi;
if [ -x "$(command -v groups)" ]; then groups; else echo "groups is missing from the machine. skipping..."; fi;
if [ -x "$(command -v id)" ]; then id; else echo "id is missing from the machine. skipping..."; fi;
if [ -x "$(command -v getent)" ]; then getent group; else echo "getent is missing from the machine. skipping..."; fi;
cat /etc/group
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.001/T1069.001.yaml)
