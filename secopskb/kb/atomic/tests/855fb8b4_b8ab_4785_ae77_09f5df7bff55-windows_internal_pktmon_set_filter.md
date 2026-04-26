---
atomic_guid: "855fb8b4-b8ab-4785-ae77-09f5df7bff55"
title: "Windows Internal pktmon set filter"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "855fb8b4-b8ab-4785-ae77-09f5df7bff55"
  - "Windows Internal pktmon set filter"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Internal pktmon set filter

Select Desired ports for packet capture 
https://lolbas-project.github.io/lolbas/Binaries/Pktmon/

## Metadata

- Atomic GUID: 855fb8b4-b8ab-4785-ae77-09f5df7bff55
- Technique: T1040: Network Sniffing
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
pktmon.exe filter add -p 445
```

### Cleanup

```commandprompt
pktmon filter remove
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
