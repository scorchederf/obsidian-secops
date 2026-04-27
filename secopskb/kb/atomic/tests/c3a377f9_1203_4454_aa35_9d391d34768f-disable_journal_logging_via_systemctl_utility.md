---
atomic_guid: "c3a377f9-1203-4454-aa35-9d391d34768f"
title: "Disable journal logging via systemctl utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562"
attack_technique_name: "Impair Defenses"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "c3a377f9-1203-4454-aa35-9d391d34768f"
  - "Disable journal logging via systemctl utility"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The atomic test disables the journal logging using built-in systemctl utility

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562: Impair Defenses]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo systemctl stop systemd-journald #disables journal logging
```

### Cleanup

```bash
sudo systemctl start systemd-journald #starts journal service
sudo systemctl enable systemd-journald #starts journal service automatically at boot time
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml)
