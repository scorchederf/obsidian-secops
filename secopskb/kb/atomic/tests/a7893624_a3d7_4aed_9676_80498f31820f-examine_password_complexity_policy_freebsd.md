---
atomic_guid: "a7893624-a3d7-4aed-9676-80498f31820f"
title: "Examine password complexity policy - FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "a7893624-a3d7-4aed-9676-80498f31820f"
  - "Examine password complexity policy - FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Examine password complexity policy - FreeBSD

Lists the password complexity policy to console on FreeBSD.

## Metadata

- Atomic GUID: a7893624-a3d7-4aed-9676-80498f31820f
- Technique: T1201: Password Policy Discovery
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Executor

- name: sh

### Command

```bash
cat /etc/pam.d/passwd
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
