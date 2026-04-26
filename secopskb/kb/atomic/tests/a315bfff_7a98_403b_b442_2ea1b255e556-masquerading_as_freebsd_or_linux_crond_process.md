---
atomic_guid: "a315bfff-7a98-403b-b442-2ea1b255e556"
title: "Masquerading as FreeBSD or Linux crond process."
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "a315bfff-7a98-403b-b442-2ea1b255e556"
  - "Masquerading as FreeBSD or Linux crond process."
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading as FreeBSD or Linux crond process.

Copies sh process, renames it as crond, and executes it to masquerade as the cron daemon.

Upon successful execution, sh is renamed to `crond` and executed.

## Metadata

- Atomic GUID: a315bfff-7a98-403b-b442-2ea1b255e556
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Executor

- name: sh

### Command

```sh
cp /bin/sh /tmp/crond;
echo 'sleep 5' | /tmp/crond
```

### Cleanup

```sh
rm /tmp/crond
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
