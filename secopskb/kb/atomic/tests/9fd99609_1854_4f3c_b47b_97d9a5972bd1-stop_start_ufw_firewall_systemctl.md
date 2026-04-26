---
atomic_guid: "9fd99609-1854-4f3c-b47b-97d9a5972bd1"
title: "Stop/Start UFW firewall systemctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "9fd99609-1854-4f3c-b47b-97d9a5972bd1"
  - "Stop/Start UFW firewall systemctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Stop/Start UFW firewall systemctl

Stop the Uncomplicated Firewall (UFW) if installed, using systemctl.

## Metadata

- Atomic GUID: 9fd99609-1854-4f3c-b47b-97d9a5972bd1
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if systemctl and ufw is installed on the machine.

### Prerequisite Check

```text
if [ ! -x "$(command -v systemctl)" ]; then echo -e "\n***** systemctl NOT installed *****\n"; exit 1; fi
if [ ! -x "$(command -v ufw)" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
if echo "$(ufw status)" |grep -q "inactive"; then echo -e "\n***** ufw inactive *****\n"; exit 1; fi
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
systemctl stop ufw
```

### Cleanup

```sh
systemctl start ufw
systemctl status ufw
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
