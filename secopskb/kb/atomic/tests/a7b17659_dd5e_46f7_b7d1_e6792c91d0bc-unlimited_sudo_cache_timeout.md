---
atomic_guid: "a7b17659-dd5e-46f7-b7d1-e6792c91d0bc"
title: "Unlimited sudo cache timeout"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.003"
attack_technique_name: "Abuse Elevation Control Mechanism: Sudo and Sudo Caching"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "a7b17659-dd5e-46f7-b7d1-e6792c91d0bc"
  - "Unlimited sudo cache timeout"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Unlimited sudo cache timeout

Sets sudo caching timestamp_timeout to a value for unlimited. This is dangerous to modify without using 'visudo', do not do this on a production system.

## Metadata

- Atomic GUID: a7b17659-dd5e-46f7-b7d1-e6792c91d0bc
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
sudo sed -i 's/env_reset.*$/env_reset,timestamp_timeout=-1/' /etc/sudoers
sudo visudo -c -f /etc/sudoers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml)
