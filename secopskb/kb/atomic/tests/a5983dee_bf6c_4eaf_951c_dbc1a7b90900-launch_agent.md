---
atomic_guid: "a5983dee-bf6c-4eaf-951c-dbc1a7b90900"
title: "Launch Agent"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.001"
attack_technique_name: "Create or Modify System Process: Launch Agent"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "a5983dee-bf6c-4eaf-951c-dbc1a7b90900"
  - "Launch Agent"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Launch Agent

Create a plist and execute it

## Metadata

- Atomic GUID: a5983dee-bf6c-4eaf-951c-dbc1a7b90900
- Technique: T1543.001: Create or Modify System Process: Launch Agent
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1543.001/T1543.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.001]]

## Input Arguments

### path_malicious_plist

- description: Name of file to store in cron folder
- type: string
- default: $PathToAtomicsFolder/T1543.001/src/atomicredteam_T1543_001.plist

### plist_filename

- description: filename
- type: string
- default: com.atomicredteam.plist

## Dependencies

The shared library must exist on disk at specified location (#{path_malicious_plist})

### Prerequisite Check

```text
if [ -f #{path_malicious_plist} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
echo "The shared library doesn't exist. Check the path"; exit 1;
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
if [ ! -d ~/Library/LaunchAgents ]; then mkdir ~/Library/LaunchAgents; fi;
sudo cp #{path_malicious_plist} ~/Library/LaunchAgents/#{plist_filename}
sudo launchctl load -w ~/Library/LaunchAgents/#{plist_filename}
```

### Cleanup

```bash
sudo launchctl unload ~/Library/LaunchAgents/#{plist_filename}
sudo rm ~/Library/LaunchAgents/#{plist_filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml)
