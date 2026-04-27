---
atomic_guid: "0315bdff-4178-47e9-81e4-f31a6d23f7e4"
title: "Enable Guest Account on macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.001"
attack_technique_name: "Valid Accounts: Default Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "0315bdff-4178-47e9-81e4-f31a6d23f7e4"
  - "Enable Guest Account on macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test enables the guest account on macOS using sysadminctl utility.

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo sysadminctl -guestAccount on
```

### Cleanup

```bash
sudo sysadminctl -guestAccount off
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml)
