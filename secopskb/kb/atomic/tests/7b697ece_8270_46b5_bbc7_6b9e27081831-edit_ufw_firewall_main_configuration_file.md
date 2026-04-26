---
atomic_guid: "7b697ece-8270-46b5-bbc7-6b9e27081831"
title: "Edit UFW firewall main configuration file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "7b697ece-8270-46b5-bbc7-6b9e27081831"
  - "Edit UFW firewall main configuration file"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Edit UFW firewall main configuration file

Edit the Uncomplicated Firewall (UFW) main configuration file for setting 
default policies /etc/default/ufw.

## Metadata

- Atomic GUID: 7b697ece-8270-46b5-bbc7-6b9e27081831
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Dependencies

Check if /etc/default/ufw exists.

### Prerequisite Check

```text
if [ ! -f "/etc/default/ufw" ]; then echo -e "\n***** ufw NOT installed *****\n"; exit 1; fi
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
echo "# THIS IS A COMMENT" >> /etc/default/ufw
grep "# THIS IS A COMMENT" /etc/default/ufw
```

### Cleanup

```sh
sed -i 's/# THIS IS A COMMENT//g' /etc/default/ufw
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
