---
atomic_guid: "03ab8df5-3a6b-4417-b6bd-bb7a5cfd74cf"
title: "Launch Daemon"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.004"
attack_technique_name: "Create or Modify System Process: Launch Daemon"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.004/T1543.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "03ab8df5-3a6b-4417-b6bd-bb7a5cfd74cf"
  - "Launch Daemon"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Launch Daemon

Utilize LaunchDaemon to launch `Hello World`

## Metadata

- Atomic GUID: 03ab8df5-3a6b-4417-b6bd-bb7a5cfd74cf
- Technique: T1543.004: Create or Modify System Process: Launch Daemon
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1543.004/T1543.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.004]]

## Input Arguments

### path_malicious_plist

- description: Name of file to store in cron folder
- type: string
- default: $PathToAtomicsFolder/T1543.004/src/atomicredteam_T1543_004.plist

### plist_filename

- description: filename
- type: string
- default: com.atomicredteam.plist

## Dependencies

The shared library must exist on disk at specified location (#{path_malicious_plist})

### Prerequisite Check

```bash
if [ -f #{path_malicious_plist} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
echo "The plist file doesn't exist. Check the path and try again."; exit 1;
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo cp #{path_malicious_plist} /Library/LaunchDaemons/#{plist_filename}
sudo launchctl load -w /Library/LaunchDaemons/#{plist_filename}
```

### Cleanup

```bash
sudo launchctl unload /Library/LaunchDaemons/#{plist_filename}
sudo rm /Library/LaunchDaemons/#{plist_filename}
sudo rm /tmp/T1543_004_atomicredteam.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.004/T1543.004.yaml)
