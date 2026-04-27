---
atomic_guid: "4b7fa042-9482-45e1-b348-4b756b2a0742"
title: "Examine password policy - macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "4b7fa042-9482-45e1-b348-4b756b2a0742"
  - "Examine password policy - macOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Examine password policy - macOS

Lists the password policy to console on macOS.

## Metadata

- Atomic GUID: 4b7fa042-9482-45e1-b348-4b756b2a0742
- Technique: T1201: Password Policy Discovery
- Platforms: macos
- Executor: bash
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- name: bash

### Command

```bash
pwpolicy getaccountpolicies
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
