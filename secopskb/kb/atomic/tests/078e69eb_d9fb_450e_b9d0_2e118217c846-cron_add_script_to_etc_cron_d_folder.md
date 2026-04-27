---
atomic_guid: "078e69eb-d9fb-450e-b9d0-2e118217c846"
title: "Cron - Add script to /etc/cron.d folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.003"
attack_technique_name: "Scheduled Task/Job: Cron"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "078e69eb-d9fb-450e-b9d0-2e118217c846"
  - "Cron - Add script to /etc/cron.d folder"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cron - Add script to /etc/cron.d folder

This test adds a script to /etc/cron.d folder configured to execute on a schedule.

## Metadata

- Atomic GUID: 078e69eb-d9fb-450e-b9d0-2e118217c846
- Technique: T1053.003: Scheduled Task/Job: Cron
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1053.003/T1053.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Input Arguments

### command

- description: Command to execute
- type: string
- default: echo '*/5     *       *       *       *       root    echo "Hello from Atomic Red Team"' > /tmp/atomic.log

### cron_script_name

- description: Name of file to store in cron folder
- type: string
- default: persistevil

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "#{command}" > /etc/cron.d/#{cron_script_name}
```

### Cleanup

```bash
rm /etc/cron.d/#{cron_script_name} -f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml)
