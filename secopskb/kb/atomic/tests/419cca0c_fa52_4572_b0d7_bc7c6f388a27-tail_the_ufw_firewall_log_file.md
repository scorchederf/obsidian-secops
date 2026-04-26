---
atomic_guid: "419cca0c-fa52-4572-b0d7-bc7c6f388a27"
title: "Tail the UFW firewall log file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "419cca0c-fa52-4572-b0d7-bc7c6f388a27"
  - "Tail the UFW firewall log file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tail the UFW firewall log file

Print  the last 10 lines of the Uncomplicated Firewall (UFW) log file 
/var/log/ufw.log.

## Metadata

- Atomic GUID: 419cca0c-fa52-4572-b0d7-bc7c6f388a27
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if /var/log/ufw.log exists.

### Prerequisite Check

```text
if [ ! -f "/var/log/ufw.log" ]; then echo -e "\n***** ufw NOT logging *****\n"; exit 1; fi
```

### Get Prerequisite

```text
echo ""
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
tail /var/log/ufw.log
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
