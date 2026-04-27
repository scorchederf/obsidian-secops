---
atomic_guid: "a315bfff-7a98-403b-b442-2ea1b255e556"
title: "Masquerading as FreeBSD or Linux crond process."
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-27 19:12:25"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copies sh process, renames it as crond, and executes it to masquerade as the cron daemon.

Upon successful execution, sh is renamed to `crond` and executed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Executor

- name: sh

### Command

```bash
cp /bin/sh /tmp/crond;
echo 'sleep 5' | /tmp/crond
```

### Cleanup

```bash
rm /tmp/crond
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
