---
atomic_guid: "beaf815a-c883-4194-97e9-fdbbb2bbdd7c"
title: "Edit UFW firewall user.rules file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "beaf815a-c883-4194-97e9-fdbbb2bbdd7c"
  - "Edit UFW firewall user.rules file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Edit UFW firewall user.rules file

Edit the Uncomplicated Firewall (UFW) rules file /etc/ufw/user.rules.

## Metadata

- Atomic GUID: beaf815a-c883-4194-97e9-fdbbb2bbdd7c
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if /etc/ufw/user.rules exists.

### Prerequisite Check

```bash
if [ ! -f "/etc/ufw/user.rules" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
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
echo "# THIS IS A COMMENT" >> /etc/ufw/user.rules
grep "# THIS IS A COMMENT" /etc/ufw/user.rules
```

### Cleanup

```bash
sed -i 's/# THIS IS A COMMENT//g' /etc/ufw/user.rules
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
