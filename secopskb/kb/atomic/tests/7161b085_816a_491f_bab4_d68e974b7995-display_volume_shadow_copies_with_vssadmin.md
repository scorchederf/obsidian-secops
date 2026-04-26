---
atomic_guid: "7161b085-816a-491f-bab4-d68e974b7995"
title: "Display volume shadow copies with \"vssadmin\""
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "7161b085-816a-491f-bab4-d68e974b7995"
  - "Display volume shadow copies with \"vssadmin\""
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Display volume shadow copies with "vssadmin"

The command shows all available volume shadow copies, along with their creation time and location.

## Metadata

- Atomic GUID: 7161b085-816a-491f-bab4-d68e974b7995
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
vssadmin.exe list shadows
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
