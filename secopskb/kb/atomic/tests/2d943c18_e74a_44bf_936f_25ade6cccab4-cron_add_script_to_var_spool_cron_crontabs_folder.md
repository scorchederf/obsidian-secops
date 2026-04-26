---
atomic_guid: "2d943c18-e74a-44bf-936f-25ade6cccab4"
title: "Cron - Add script to /var/spool/cron/crontabs/ folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.003"
attack_technique_name: "Scheduled Task/Job: Cron"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "2d943c18-e74a-44bf-936f-25ade6cccab4"
  - "Cron - Add script to /var/spool/cron/crontabs/ folder"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cron - Add script to /var/spool/cron/crontabs/ folder

This test adds a script to a /var/spool/cron/crontabs folder configured to execute on a schedule. This technique was used by the threat actor Rocke during the exploitation of Linux web servers.

## Metadata

- Atomic GUID: 2d943c18-e74a-44bf-936f-25ade6cccab4
- Technique: T1053.003: Scheduled Task/Job: Cron
- Platforms: linux
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

- description: Name of file to store in /var/spool/cron/crontabs folder
- type: string
- default: persistevil

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "#{command}" >> /var/spool/cron/crontabs/#{cron_script_name}
```

### Cleanup

```bash
rm /var/spool/cron/crontabs/#{cron_script_name} -f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml)
