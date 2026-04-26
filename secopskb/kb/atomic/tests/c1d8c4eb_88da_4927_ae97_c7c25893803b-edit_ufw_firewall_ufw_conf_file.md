---
atomic_guid: "c1d8c4eb-88da-4927-ae97-c7c25893803b"
title: "Edit UFW firewall ufw.conf file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "c1d8c4eb-88da-4927-ae97-c7c25893803b"
  - "Edit UFW firewall ufw.conf file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Edit UFW firewall ufw.conf file

Edit the Uncomplicated Firewall (UFW) configuration file /etc/ufw/ufw.conf 
which controls if the firewall starts on boot and its logging level.

## Metadata

- Atomic GUID: c1d8c4eb-88da-4927-ae97-c7c25893803b
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if /etc/ufw/ufw.conf exists.

### Prerequisite Check

```bash
if [ ! -f "/etc/ufw/ufw.conf" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
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
echo "# THIS IS A COMMENT" >> /etc/ufw/ufw.conf
grep "# THIS IS A COMMENT" /etc/ufw/ufw.conf
```

### Cleanup

```bash
sed -i 's/# THIS IS A COMMENT//g' /etc/ufw/ufw.conf
cat /etc/ufw/ufw.conf
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
