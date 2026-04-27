---
atomic_guid: "b2563a4e-c4b8-429c-8d47-d5bcb227ba7a"
title: "Add and delete UFW firewall rules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "b2563a4e-c4b8-429c-8d47-d5bcb227ba7a"
  - "Add and delete UFW firewall rules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Add and delete a rule on the Uncomplicated Firewall (UFW) if installed and enabled.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Dependencies

Check if ufw is installed on the machine and enabled.

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
ufw prepend deny from 1.2.3.4
ufw status numbered
```

### Cleanup

```bash
{ echo y; echo response; } | ufw delete 1
ufw status numbered
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
