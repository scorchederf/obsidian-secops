---
atomic_guid: "4df6a0fe-2bdd-4be8-8618-a6a19654a57a"
title: "Disable tty_tickets for sudo caching (freebsd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.003"
attack_technique_name: "Abuse Elevation Control Mechanism: Sudo and Sudo Caching"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "4df6a0fe-2bdd-4be8-8618-a6a19654a57a"
  - "Disable tty_tickets for sudo caching (freebsd)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable tty_tickets for sudo caching (freebsd)

Sets sudo caching tty_tickets value to disabled. This is dangerous to modify without using 'visudo', do not do this on a production system.

## Metadata

- Atomic GUID: 4df6a0fe-2bdd-4be8-8618-a6a19654a57a
- Technique: T1548.003: Abuse Elevation Control Mechanism: Sudo and Sudo Caching
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1548.003/T1548.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.003]]

## Dependencies

Check if sudo is installed.

### Prerequisite Check

```bash
if [ ! -x "$(command -v sudo)" ]; then exit 1; else exit 0; fi;
```

### Get Prerequisite

```bash
(which pkg && pkg install -y sudo)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo sh -c "echo Defaults "'!'"tty_tickets >> /usr/local/etc/sudoers"
sudo visudo -c -f /usr/local/etc/sudoers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml)
