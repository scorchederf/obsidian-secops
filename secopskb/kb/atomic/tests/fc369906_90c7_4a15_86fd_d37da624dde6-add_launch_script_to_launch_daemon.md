---
atomic_guid: "fc369906-90c7-4a15-86fd-d37da624dde6"
title: "Add launch script to launch daemon"
framework: "atomic"
generated: "true"
attack_technique_id: "T1037.005"
attack_technique_name: "Boot or Logon Initialization Scripts: Startup Items"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.005/T1037.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "fc369906-90c7-4a15-86fd-d37da624dde6"
  - "Add launch script to launch daemon"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add launch script to launch daemon

Add launch script to /Library/StartupItems to launch agent
[Example](https://cybersecurity.att.com/blogs/labs-research/diversity-in-recent-mac-malware)

## Metadata

- Atomic GUID: fc369906-90c7-4a15-86fd-d37da624dde6
- Technique: T1037.005: Boot or Logon Initialization Scripts: Startup Items
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Dependency Executor: bash
- Source Path: atomics/T1037.005/T1037.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.005]]

## Input Arguments

### path_malicious_plist

- description: Name of file to store in /tmp
- type: string
- default: $PathToAtomicsFolder/T1037.005/src/T1037_005_daemon.plist

### path_malicious_script

- description: Name of script to store in cron folder
- type: string
- default: $PathToAtomicsFolder/T1037.005/src/T1037.005_daemon.sh

### path_startup_params

- description: Name of plist with startup params
- type: string
- default: $PathToAtomicsFolder/T1037.005/src/StartupParameters.plist

## Dependencies

/Library/StartupItems must exist

### Prerequisite Check

```bash
if [ ! -d /Library/StartupItems ]; then mkdir /Library/StartupItems; exit 0; fi;
```

### Get Prerequisite

```bash
echo "Failed to create /Library/StartupItems"; exit 1;
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

The startup script must exist on disk at specified location (#{path_malicious_script})

### Prerequisite Check

```bash
if [ -f #{path_malicious_script} ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
echo "The startup script doesn't exist. Check the path and try again."; exit 1;
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo cp #{path_startup_params} /Library/StartupItems/StartupParameters.plist
sudo cp #{path_malicious_script} /Library/StartupItems/atomic.sh
sudo cp #{path_malicious_plist} /tmp/T1037_005_daemon.plist
sudo /Library/StartupItems/atomic.sh start
```

### Cleanup

```bash
sudo launchctl unload /tmp/T1037_005_daemon.plist
sudo rm /tmp/T1037_005_daemon.plist
sudo rm /Library/StartupItems/atomic.sh
sudo rm /Library/StartupItems/StartupParameters.plist
sudo rm /tmp/T1037_005_daemon.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.005/T1037.005.yaml)
