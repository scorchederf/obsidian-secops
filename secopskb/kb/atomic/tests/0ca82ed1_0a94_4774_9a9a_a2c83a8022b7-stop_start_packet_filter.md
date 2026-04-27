---
atomic_guid: "0ca82ed1-0a94-4774-9a9a-a2c83a8022b7"
title: "Stop/Start Packet Filter"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "0ca82ed1-0a94-4774-9a9a-a2c83a8022b7"
  - "Stop/Start Packet Filter"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Stop/Start Packet Filter

Stop the Packet Filter if installed.

## Metadata

- Atomic GUID: 0ca82ed1-0a94-4774-9a9a-a2c83a8022b7
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if pfctl is installed on the machine.

### Prerequisite Check

```bash
if [ ! -x "$(command -v pfctl)" ]; then echo -e "\n***** PF NOT installed *****\n"; exit 1; fi
if [ "$(kldstat -n pf)" = "" ]; then echo -e "\n***** PF inactive *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
echo ""
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
service pf stop
service pf disable
```

### Cleanup

```bash
service pf enable
service pf start
service pf status
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
