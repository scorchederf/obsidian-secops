---
atomic_guid: "899a7fb5-d197-4951-8614-f19ac4a73ad4"
title: "Modify/delete iptables firewall rules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "899a7fb5-d197-4951-8614-f19ac4a73ad4"
  - "Modify/delete iptables firewall rules"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify/delete iptables firewall rules

Instead of completely "disabling" iptables, adversaries may choose to delete a certain rule, which, for example, blocks data exfiltration via ftp.
By doing so, they may cause less noise to avoid detection.

## Metadata

- Atomic GUID: 899a7fb5-d197-4951-8614-f19ac4a73ad4
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if iptables is installed on the machine.

### Prerequisite Check

```bash
if [ ! -x "$(command -v iptables)" ]; then echo -e "\n***** iptables NOT installed *****\n"; exit 1; fi
if ! echo "$(iptables -L)" | grep -q "DROP .*dpt:ftp"; then echo -e "\n***** this firewall rule is NOT activated *****\n***** activate it by executing \"iptables -A OUTPUT -p tcp --dport 21 -j DROP\" *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
iptables-save > /tmp/iptables.rules
if echo "$(iptables -L)" | grep -q "DROP .*dpt:ftp"; then echo "Rule found"; else echo "Rule not found. Setting it..."; iptables -A OUTPUT -p tcp --dport 21 -j DROP; fi
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
iptables -D OUTPUT -p tcp --dport 21 -j DROP
```

### Cleanup

```bash
iptables-restore < /tmp/iptables.rules
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
