---
atomic_guid: "11979f23-9b9d-482a-9935-6fc9cd022c3e"
title: "Event Monitor Daemon Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.001"
attack_technique_name: "Create or Modify System Process: Launch Agent"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "11979f23-9b9d-482a-9935-6fc9cd022c3e"
  - "Event Monitor Daemon Persistence"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Event Monitor Daemon Persistence

This test adds persistence via a plist to execute via the macOS Event Monitor Daemon.

## Metadata

- Atomic GUID: 11979f23-9b9d-482a-9935-6fc9cd022c3e
- Technique: T1543.001: Create or Modify System Process: Launch Agent
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1543.001/T1543.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.001]]

## Input Arguments

### empty_file

- description: Random name of the empty file used to trigger emond service
- type: string
- default: randomflag

### script_destination

- description: Path where to move the evil plist
- type: path
- default: /etc/emond.d/rules/atomicredteam_T1543_001.plist

### script_location

- description: evil plist location
- type: path
- default: $PathToAtomicsFolder/T1543.001/src/atomicredteam_T1543_001.plist

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo cp #{script_location} #{script_destination}
sudo touch /private/var/db/emondClients/#{empty_file}
```

### Cleanup

```bash
sudo rm #{script_destination}
sudo rm /private/var/db/emondClients/#{empty_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml)
