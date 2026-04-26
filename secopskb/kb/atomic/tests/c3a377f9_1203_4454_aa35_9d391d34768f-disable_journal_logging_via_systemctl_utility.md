---
atomic_guid: "c3a377f9-1203-4454-aa35-9d391d34768f"
title: "Disable journal logging via systemctl utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562"
attack_technique_name: "Impair Defenses"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml"
build_date: "2026-04-26 14:38:40"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable journal logging via systemctl utility

The atomic test disables the journal logging using built-in systemctl utility

## Metadata

- Atomic GUID: c3a377f9-1203-4454-aa35-9d391d34768f
- Technique: T1562: Impair Defenses
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562/T1562.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo systemctl stop systemd-journald #disables journal logging
```

### Cleanup

```sh
sudo systemctl start systemd-journald #starts journal service
sudo systemctl enable systemd-journald #starts journal service automatically at boot time
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml)
