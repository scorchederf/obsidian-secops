---
atomic_guid: "150c3a08-ee6e-48a6-aeaf-3659d24ceb4e"
title: "Sudo usage"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.003"
attack_technique_name: "Abuse Elevation Control Mechanism: Sudo and Sudo Caching"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "150c3a08-ee6e-48a6-aeaf-3659d24ceb4e"
  - "Sudo usage"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sudo usage

Common Sudo enumeration methods.

## Metadata

- Atomic GUID: 150c3a08-ee6e-48a6-aeaf-3659d24ceb4e
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

```bash
sudo -l      
sudo cat /etc/sudoers
sudo vim /etc/sudoers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.yaml)
