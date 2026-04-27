---
atomic_guid: "fed9be70-0186-4bde-9f8a-20945f9370c2"
title: "View sudoers access"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "fed9be70-0186-4bde-9f8a-20945f9370c2"
  - "View sudoers access"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# View sudoers access

(requires root)

## Metadata

- Atomic GUID: fed9be70-0186-4bde-9f8a-20945f9370c2
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: linux, macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1087.001/T1087.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1087.001.txt

## Executor

- elevation_required: True
- name: sh

### Command

```bash
if [ -f /etc/sudoers ]; then sudo cat /etc/sudoers > #{output_file}; fi;
if [ -f /usr/local/etc/sudoers ]; then sudo cat /usr/local/etc/sudoers > #{output_file}; fi;
cat #{output_file}
```

### Cleanup

```bash
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
