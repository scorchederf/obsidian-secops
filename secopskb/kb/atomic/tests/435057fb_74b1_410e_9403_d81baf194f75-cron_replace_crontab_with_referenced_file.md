---
atomic_guid: "435057fb-74b1-410e-9403-d81baf194f75"
title: "Cron - Replace crontab with referenced file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.003"
attack_technique_name: "Scheduled Task/Job: Cron"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "435057fb-74b1-410e-9403-d81baf194f75"
  - "Cron - Replace crontab with referenced file"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cron - Replace crontab with referenced file

This test replaces the current user's crontab file with the contents of the referenced file. This technique was used by numerous IoT automated exploitation attacks.

## Metadata

- Atomic GUID: 435057fb-74b1-410e-9403-d81baf194f75
- Technique: T1053.003: Scheduled Task/Job: Cron
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1053.003/T1053.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Input Arguments

### command

- description: Command to execute
- type: string
- default: /tmp/evil.sh

### tmp_cron

- description: Temporary reference file to hold evil cron schedule
- type: path
- default: /tmp/persistevil

## Executor

- name: sh

### Command

```bash
crontab -l > /tmp/notevil
echo "* * * * * #{command}" > #{tmp_cron} && crontab #{tmp_cron}
```

### Cleanup

```bash
crontab /tmp/notevil
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.003/T1053.003.yaml)
