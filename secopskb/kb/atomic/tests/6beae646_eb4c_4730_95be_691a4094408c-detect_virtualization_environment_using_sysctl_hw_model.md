---
atomic_guid: "6beae646-eb4c-4730-95be-691a4094408c"
title: "Detect Virtualization Environment using sysctl (hw.model)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "6beae646-eb4c-4730-95be-691a4094408c"
  - "Detect Virtualization Environment using sysctl (hw.model)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Detect Virtualization Environment using sysctl (hw.model)

sysctl hw.model will return the model name of the hardware(Macmini8,1, MacBookAir10,1, etc.) in case of native Apple hardware
but will return the hypervisor name (VMware7,0).
Reference: https://evasions.checkpoint.com/src/MacOS/macos.html#hardware-model

## Metadata

- Atomic GUID: 6beae646-eb4c-4730-95be-691a4094408c
- Technique: T1497.001: Virtualization/Sandbox Evasion: System Checks
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1497.001/T1497.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Executor

- name: sh

### Command

```bash
if [ "$(sysctl -n hw.model | grep -v 'Mac')" != "" ]; then echo 'Virtualization Environment detected'; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
