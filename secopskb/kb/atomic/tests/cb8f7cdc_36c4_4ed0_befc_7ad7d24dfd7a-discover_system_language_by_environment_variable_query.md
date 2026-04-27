---
atomic_guid: "cb8f7cdc-36c4-4ed0-befc-7ad7d24dfd7a"
title: "Discover System Language by Environment Variable Query"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "cb8f7cdc-36c4-4ed0-befc-7ad7d24dfd7a"
  - "Discover System Language by Environment Variable Query"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover System Language by Environment Variable Query

Identify System language by checking the environment variables

Upon successful execution, the 5 character locale result can be looked up to
correlate the language and territory. Environment query commands are likely
to run with a pattern match command e.g. `env | grep LANG`

Note: `env` and `printenv` will usually provide the same results. `set` is
also used as a builtin command that does not generate syscall telemetry but
does provide a list of the environment variables.

## Metadata

- Atomic GUID: cb8f7cdc-36c4-4ed0-befc-7ad7d24dfd7a
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Dependencies

Check if printenv command exists on the machine

### Prerequisite Check

```bash
[ -x "$(command -v printenv)" ] && exit 0 || exit 1
```

### Get Prerequisite

```bash
echo "printenv command does not exist"
exit 1
```

## Executor

- name: sh

### Command

```bash
env | grep LANG
printenv LANG
set | grep LANG
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
