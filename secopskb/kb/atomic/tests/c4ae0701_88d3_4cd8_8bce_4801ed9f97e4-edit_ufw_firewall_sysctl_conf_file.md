---
atomic_guid: "c4ae0701-88d3-4cd8-8bce-4801ed9f97e4"
title: "Edit UFW firewall sysctl.conf file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Edit UFW firewall sysctl.conf file

Edit the Uncomplicated Firewall (UFW) configuration file for setting network 
variables /etc/ufw/sysctl.conf.

## Metadata

- Atomic GUID: c4ae0701-88d3-4cd8-8bce-4801ed9f97e4
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

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
