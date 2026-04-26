---
atomic_guid: "5d7057c9-2c8a-4026-91dd-13b5584daa69"
title: "Discover System Language by locale file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "5d7057c9-2c8a-4026-91dd-13b5584daa69"
  - "Discover System Language by locale file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Discover System Language by locale file

Identify System language with the by reading the locale configuration file.

The locale configuration file contains the `LANG` environment variable which
will contain the 5 character locale that can be looked up to correlate the
language and territory.

## Metadata

- Atomic GUID: 5d7057c9-2c8a-4026-91dd-13b5584daa69
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Dependencies

Check the location of the locale configuration file.

### Prerequisite Check

```text
[ -f /etc/locale.conf ] || [ -f /etc/default/locale ] && exit 0 || exit 1
```

### Get Prerequisite

```text
echo "Test only valid for systems that have locale file"
```

## Executor

- name: sh

### Command

```sh
[ -f /etc/locale.conf ] && cat /etc/locale.conf || cat /etc/default/locale
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
