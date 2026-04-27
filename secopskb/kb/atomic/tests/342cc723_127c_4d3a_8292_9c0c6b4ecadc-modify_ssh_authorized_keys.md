---
atomic_guid: "342cc723-127c-4d3a-8292-9c0c6b4ecadc"
title: "Modify SSH Authorized Keys"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.004"
attack_technique_name: "SSH Authorized Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.004/T1098.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "342cc723-127c-4d3a-8292-9c0c6b4ecadc"
  - "Modify SSH Authorized Keys"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify SSH Authorized Keys

Modify contents of <user-home>/.ssh/authorized_keys to maintain persistence on victim host. 
If the user is able to save the same contents in the authorized_keys file, it shows user can modify the file.

## Metadata

- Atomic GUID: 342cc723-127c-4d3a-8292-9c0c6b4ecadc
- Technique: T1098.004: SSH Authorized Keys
- Platforms: linux, macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1098.004/T1098.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
if [ -f ~/.ssh/authorized_keys ]; then ssh_authorized_keys=$(cat ~/.ssh/authorized_keys); echo "$ssh_authorized_keys" > ~/.ssh/authorized_keys; fi;
```

### Cleanup

```bash
unset ssh_authorized_keys
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.004/T1098.004.yaml)
