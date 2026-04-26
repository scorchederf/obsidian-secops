---
atomic_guid: "d3eda496-1fc0-49e9-aff5-3bec5da9fa22"
title: "Create a system level transient systemd service and timer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.006"
attack_technique_name: "Scheduled Task/Job: Systemd Timers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.006/T1053.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "d3eda496-1fc0-49e9-aff5-3bec5da9fa22"
  - "Create a system level transient systemd service and timer"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a system level transient systemd service and timer

Schedule a system level transient task (will not survive a reboot) without having to create the .timer or .service files by using the systemd-run command.

## Metadata

- Atomic GUID: d3eda496-1fc0-49e9-aff5-3bec5da9fa22
- Technique: T1053.006: Scheduled Task/Job: Systemd Timers
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1053.006/T1053.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.006]]

## Dependencies

Check if systemd-run exists on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v systemd-run)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
echo "Install systemd on the machine."; exit 1;
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
systemd-run --unit=Atomic-Red-Team --on-calendar '*:0/1' /bin/sh -c 'echo "$(date) $(whoami)" >>/tmp/log'
```

### Cleanup

```bash
systemctl stop Atomic-Red-Team.service
systemctl stop Atomic-Red-Team.timer
rm /tmp/log
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.006/T1053.006.yaml)
