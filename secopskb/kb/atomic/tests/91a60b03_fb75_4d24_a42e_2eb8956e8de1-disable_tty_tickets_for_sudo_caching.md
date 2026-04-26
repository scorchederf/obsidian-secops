---
atomic_guid: "91a60b03-fb75-4d24-a42e-2eb8956e8de1"
title: "Disable tty_tickets for sudo caching"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.003"
attack_technique_name: "Abuse Elevation Control Mechanism: Sudo and Sudo Caching"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "91a60b03-fb75-4d24-a42e-2eb8956e8de1"
  - "Disable tty_tickets for sudo caching"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable tty_tickets for sudo caching

Sets sudo caching tty_tickets value to disabled. This is dangerous to modify without using 'visudo', do not do this on a production system.

## Metadata

- Atomic GUID: 91a60b03-fb75-4d24-a42e-2eb8956e8de1
- Technique: T1548.003: Abuse Elevation Control Mechanism: Sudo and Sudo Caching
- Platforms: macos, linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1548.003/T1548.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.003]]

## Executor

- elevation_required: True
- name: sh

### Command

```sh
sudo sh -c "echo Defaults "'!'"tty_tickets >> /etc/sudoers"
sudo visudo -c -f /etc/sudoers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml)
