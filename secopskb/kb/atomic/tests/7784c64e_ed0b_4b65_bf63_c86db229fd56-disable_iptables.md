---
atomic_guid: "7784c64e-ed0b-4b65-bf63-c86db229fd56"
title: "Disable iptables"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "7784c64e-ed0b-4b65-bf63-c86db229fd56"
  - "Disable iptables"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Some Linux systems may not activate ufw, but use iptables for firewall rules instead. (ufw works on top of iptables.) 
Attackers cannot directly disable iptables, as it is not implemented as a service like ufw. But they can flush all iptables 
rules, which in fact "disable" iptables.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Dependencies

Check if iptables is installed on the machine.

### Prerequisite Check

```bash
if [ ! -x "$(command -v iptables)" ]; then echo -e "\n***** iptables NOT installed *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
sudo apt-get install iptables
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
iptables-save > /tmp/iptables.rules
iptables -F
```

### Cleanup

```bash
iptables-restore < /tmp/iptables.rules
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
