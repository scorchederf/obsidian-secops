---
atomic_guid: "b7d42afa-9086-4c8a-b7b0-8ea3faa6ebb0"
title: "Cron - Add script to all cron subfolders"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.003"
attack_technique_name: "Scheduled Task/Job: Cron"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "b7d42afa-9086-4c8a-b7b0-8ea3faa6ebb0"
  - "Cron - Add script to all cron subfolders"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cron - Add script to all cron subfolders

This test adds a script to /etc/cron.hourly, /etc/cron.daily, /etc/cron.monthly and /etc/cron.weekly folders configured to execute on a schedule. This technique was used by the threat actor Rocke during the exploitation of Linux web servers.

## Metadata

- Atomic GUID: b7d42afa-9086-4c8a-b7b0-8ea3faa6ebb0
- Technique: T1053.003: Scheduled Task/Job: Cron
- Platforms: macos, linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1053.003/T1053.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Input Arguments

### command

- description: Command to execute
- type: string
- default: echo 'Hello from Atomic Red Team' > /tmp/atomic.log

### cron_script_name

- description: Name of file to store in cron folder
- type: string
- default: persistevil

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "#{command}" > /etc/cron.daily/#{cron_script_name}
echo "#{command}" > /etc/cron.hourly/#{cron_script_name}
echo "#{command}" > /etc/cron.monthly/#{cron_script_name}
echo "#{command}" > /etc/cron.weekly/#{cron_script_name}
```

### Cleanup

```bash
rm /etc/cron.daily/#{cron_script_name} -f
rm /etc/cron.hourly/#{cron_script_name} -f
rm /etc/cron.monthly/#{cron_script_name} -f
rm /etc/cron.weekly/#{cron_script_name} -f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml)
