---
atomic_guid: "db9de996-441e-4ae0-947b-61b6871e2fdf"
title: "Disable syslog (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "db9de996-441e-4ae0-947b-61b6871e2fdf"
  - "Disable syslog (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable syslog (freebsd)

Disables syslog collection

## Metadata

- Atomic GUID: db9de996-441e-4ae0-947b-61b6871e2fdf
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
service syslogd stop
sysrc syslogd_enable="NO"
```

### Cleanup

```sh
sysrc syslogd_enable="YES"
service syslogd start
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
