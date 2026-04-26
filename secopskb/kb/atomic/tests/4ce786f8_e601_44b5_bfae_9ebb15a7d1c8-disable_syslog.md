---
atomic_guid: "4ce786f8-e601-44b5-bfae-9ebb15a7d1c8"
title: "Disable syslog"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "4ce786f8-e601-44b5-bfae-9ebb15a7d1c8"
  - "Disable syslog"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable syslog

Disables syslog collection

## Metadata

- Atomic GUID: 4ce786f8-e601-44b5-bfae-9ebb15a7d1c8
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### cleanup_command

- description: Command to enable syslog collection. Default newer rsyslog commands. i.e older command = service rsyslog start ; chkconfig rsyslog on
- type: string
- default: systemctl start rsyslog ; systemctl enable rsyslog

### flavor_command

- description: Command to disable syslog collection. Default newer rsyslog commands. i.e older command = service rsyslog stop ; chkconfig off rsyslog
- type: string
- default: systemctl stop rsyslog ; systemctl disable rsyslog

### package_checker

- description: Package checking command for linux.
- type: string
- default: (rpm -q rsyslog 2>&1 >/dev/null) || (dpkg -s rsyslog | grep -q installed)

### package_installer

- description: Package installer command for linux. Default yum
- type: string
- default: (which yum && yum -y install epel-release rsyslog)||(which apt-get && apt-get install -y rsyslog)

## Dependencies

Package with rsyslog must be on system

### Prerequisite Check

```text
if #{package_checker} > /dev/null; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
sudo #{package_installer}
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
#{flavor_command}
```

### Cleanup

```sh
#{cleanup_command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
