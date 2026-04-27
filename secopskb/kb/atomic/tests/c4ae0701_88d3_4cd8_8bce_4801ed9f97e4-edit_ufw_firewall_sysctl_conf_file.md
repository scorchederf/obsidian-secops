---
atomic_guid: "c4ae0701-88d3-4cd8-8bce-4801ed9f97e4"
title: "Edit UFW firewall sysctl.conf file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "c4ae0701-88d3-4cd8-8bce-4801ed9f97e4"
  - "Edit UFW firewall sysctl.conf file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Edit the Uncomplicated Firewall (UFW) configuration file for setting network 
variables /etc/ufw/sysctl.conf.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Dependencies

Check if /etc/ufw/sysctl.conf exists.

### Prerequisite Check

```bash
if [ ! -f "/etc/ufw/sysctl.conf" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
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
echo "# THIS IS A COMMENT" >> /etc/ufw/sysctl.conf
grep "# THIS IS A COMMENT" /etc/ufw/sysctl.conf
```

### Cleanup

```bash
sed -i 's/# THIS IS A COMMENT//g' /etc/ufw/sysctl.conf
cat /etc/ufw/sysctl.conf
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
