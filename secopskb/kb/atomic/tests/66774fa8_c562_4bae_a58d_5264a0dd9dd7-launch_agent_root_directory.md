---
atomic_guid: "66774fa8-c562-4bae-a58d-5264a0dd9dd7"
title: "Launch Agent - Root Directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.001"
attack_technique_name: "Create or Modify System Process: Launch Agent"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "66774fa8-c562-4bae-a58d-5264a0dd9dd7"
  - "Launch Agent - Root Directory"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Create a plist and execute it

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]

## Input Arguments

### path_malicious_plist

- description: Name of file to store in cron folder
- type: string
- default: $PathToAtomicsFolder/T1543.001/src/atomicredteam_T1543_001.plist

### plist_filename

- description: filename
- type: string
- default: com.atomicredteam.T1543.001.plist

## Dependencies

/Library/LaunchAgents must exist

### Prerequisite Check

```bash
if [ ! -d /Library/LaunchAgents ]; then mkdir /Library/LaunchAgents; exit 0; fi;
```

### Get Prerequisite

```bash
echo "Failed to create /Library/LaunchAgents"; exit 1;
```

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
sudo cp #{path_malicious_plist} /Library/LaunchAgents/#{plist_filename}
launchctl load -w /Library/LaunchAgents/#{plist_filename}
```

### Cleanup

```bash
launchctl unload /Library/LaunchAgents/#{plist_filename}
sudo rm /Library/LaunchAgents/#{plist_filename}
sudo rm /tmp/T1543_001_atomicredteam.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.001/T1543.001.yaml)
