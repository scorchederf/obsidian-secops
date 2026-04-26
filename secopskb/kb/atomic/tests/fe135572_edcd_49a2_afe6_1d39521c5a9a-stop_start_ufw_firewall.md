---
atomic_guid: "fe135572-edcd-49a2-afe6-1d39521c5a9a"
title: "Stop/Start UFW firewall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "fe135572-edcd-49a2-afe6-1d39521c5a9a"
  - "Stop/Start UFW firewall"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Stop/Start UFW firewall

Stop the Uncomplicated Firewall (UFW) if installed.

## Metadata

- Atomic GUID: fe135572-edcd-49a2-afe6-1d39521c5a9a
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if ufw is installed on the machine.

### Prerequisite Check

```bash
if [ ! -x "$(command -v ufw)" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
if echo "$(ufw status)" |grep -q "inactive"; then echo -e "\n***** ufw inactive *****\n"; exit 1; fi
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
ufw disable
```

### Cleanup

```bash
ufw enable
ufw status verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
