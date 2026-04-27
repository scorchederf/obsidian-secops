---
atomic_guid: "de87ed7b-52c3-43fd-9554-730f695e7f31"
title: "Create Hidden User using IsHidden option"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.002"
attack_technique_name: "Hide Artifacts: Hidden Users"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.002/T1564.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "de87ed7b-52c3-43fd-9554-730f695e7f31"
  - "Create Hidden User using IsHidden option"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Add a hidden user on macOS using IsHidden optoin

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564002-hidden-users|T1564.002: Hidden Users]]

## Input Arguments

### user_name

- description: username to add
- type: string
- default: APT

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo dscl . -create /Users/#{user_name} IsHidden 1
```

### Cleanup

```bash
sudo dscl . -delete /Users/#{user_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.002/T1564.002.yaml)
