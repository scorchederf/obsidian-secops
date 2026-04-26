---
atomic_guid: "dfbd1a21-540d-4574-9731-e852bd6fe840"
title: "Detect Virtualization Environment (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "dfbd1a21-540d-4574-9731-e852bd6fe840"
  - "Detect Virtualization Environment (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Detect Virtualization Environment (Linux)

systemd-detect-virt detects execution in a virtualized environment.
At boot, dmesg stores a log if a hypervisor is detected.

## Metadata

- Atomic GUID: dfbd1a21-540d-4574-9731-e852bd6fe840
- Technique: T1497.001: Virtualization/Sandbox Evasion: System Checks
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1497.001/T1497.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
if (systemd-detect-virt) then echo "Virtualization Environment detected"; fi;
if (sudo dmidecode | egrep -i 'manufacturer|product|vendor' | grep -iE 'Oracle|VirtualBox|VMWare|Parallels') then echo "Virtualization Environment detected"; fi;
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
