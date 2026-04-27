---
atomic_guid: "8b23cae1-66c1-41c5-b79d-e095b6098b5b"
title: "Add and delete Packet Filter rules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "8b23cae1-66c1-41c5-b79d-e095b6098b5b"
  - "Add and delete Packet Filter rules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Add and delete a rule on the Packet Filter (PF) if installed and enabled.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Dependencies

Check if pf is installed on the machine and enabled.

### Prerequisite Check

```bash
if [ ! -x "$(command -v pfctl)" ]; then echo -e "\n***** PF NOT installed *****\n"; exit 1; fi
if [ "$(kldstat -n pf)" = "" ]; then echo -e "\n***** PF inactive *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
echo "anchor pf-rules >> /etc/pf.conf"
pfctl -f /etc/pf.conf
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "block in proto tcp from 1.2.3.4 to any" | pfctl -a pf-rules -f -
pfctl -a pf-rules -s rules
```

### Cleanup

```bash
pfctl -a pf-rules -F rules
sed -i "" '/anchor pf-rules/d'
pfctl -f /etc/pf.conf
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
