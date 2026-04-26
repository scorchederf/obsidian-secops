---
atomic_guid: "694b3cc8-6a78-4d35-9e74-0123d009e94b"
title: "Append to the system shell profile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "694b3cc8-6a78-4d35-9e74-0123d009e94b"
  - "Append to the system shell profile"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Append to the system shell profile

An adversary may wish to establish persistence by executing malicious commands from the systems /etc/profile every time "any" user logs in.

## Metadata

- Atomic GUID: 694b3cc8-6a78-4d35-9e74-0123d009e94b
- Technique: T1546.004: Event Triggered Execution: .bash_profile .bashrc and .shrc
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1546.004/T1546.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.004]]

## Input Arguments

### text_to_append

- description: Text to append to the /etc/profile file
- type: string
- default: # Hello from Atomic Red Team T1546.004

## Executor

- elevation_required: True
- name: sh

### Command

```sh
echo '#{text_to_append}' >> /etc/profile
```

### Cleanup

```sh
sed -i "s/# Atomic Red Team was here! T1546.004//" /etc/profile
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
