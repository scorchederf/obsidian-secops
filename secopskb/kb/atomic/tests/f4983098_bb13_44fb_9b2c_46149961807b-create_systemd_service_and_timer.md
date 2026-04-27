---
atomic_guid: "f4983098-bb13-44fb-9b2c-46149961807b"
title: "Create Systemd Service and Timer"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.006"
attack_technique_name: "Scheduled Task/Job: Systemd Timers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.006/T1053.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "f4983098-bb13-44fb-9b2c-46149961807b"
  - "Create Systemd Service and Timer"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Systemd Service and Timer

This test creates Systemd service and timer then starts and enables the Systemd timer

## Metadata

- Atomic GUID: f4983098-bb13-44fb-9b2c-46149961807b
- Technique: T1053.006: Scheduled Task/Job: Systemd Timers
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1053.006/T1053.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.006]]

## Input Arguments

### path_to_systemd_service

- description: Path to systemd service unit file
- type: path
- default: /etc/systemd/system/art-timer.service

### path_to_systemd_timer

- description: Path to service timer file
- type: path
- default: /etc/systemd/system/art-timer.timer

### systemd_service_name

- description: Name of systemd service
- type: string
- default: art-timer.service

### systemd_timer_name

- description: Name of systemd service timer
- type: string
- default: art-timer.timer

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "[Unit]" > #{path_to_systemd_service}
echo "Description=Atomic Red Team Systemd Timer Service" >> #{path_to_systemd_service}
echo "[Service]" >> #{path_to_systemd_service}
echo "Type=simple" >> #{path_to_systemd_service}
echo "ExecStart=/bin/touch /tmp/art-systemd-timer-marker" >> #{path_to_systemd_service}
echo "[Install]" >> #{path_to_systemd_service}
echo "WantedBy=multi-user.target" >> #{path_to_systemd_service}
echo "[Unit]" > #{path_to_systemd_timer}
echo "Description=Executes Atomic Red Team Systemd Timer Service" >> #{path_to_systemd_timer}
echo "Requires=#{systemd_service_name}" >> #{path_to_systemd_timer}
echo "[Timer]" >> #{path_to_systemd_timer}
echo "Unit=#{systemd_service_name}" >> #{path_to_systemd_timer}
echo "OnCalendar=*-*-* *:*:00" >> #{path_to_systemd_timer}
echo "[Install]" >> #{path_to_systemd_timer}
echo "WantedBy=timers.target" >> #{path_to_systemd_timer}
systemctl start #{systemd_timer_name}
systemctl enable #{systemd_timer_name}
systemctl daemon-reload
```

### Cleanup

```bash
systemctl stop #{systemd_timer_name}
systemctl disable #{systemd_timer_name}
rm #{path_to_systemd_service}
rm #{path_to_systemd_timer}
systemctl daemon-reload
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.006/T1053.006.yaml)
