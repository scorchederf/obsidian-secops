---
atomic_guid: "d9e4f24f-aa67-4c6e-bcbf-85622b697a7c"
title: "Create Systemd Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.002"
attack_technique_name: "Create or Modify System Process: SysV/Systemd Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "d9e4f24f-aa67-4c6e-bcbf-85622b697a7c"
  - "Create Systemd Service"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test creates a Systemd service unit file and enables it as a service.

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]

## Input Arguments

### execreload_action

- description: ExecReload action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execreload-marker

### execstart_action

- description: ExecStart action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execstart-marker

### execstartpost_action

- description: ExecStartPost action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execstartpost-marker

### execstartpre_action

- description: ExecStartPre action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execstartpre-marker

### execstop_action

- description: ExecStop action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execstop-marker

### execstoppost_action

- description: ExecStopPost action for Systemd service
- type: string
- default: /bin/touch /tmp/art-systemd-execstoppost-marker

### systemd_service_file

- description: File name of systemd service unit file
- type: string
- default: art-systemd-service.service

### systemd_service_path

- description: Path to systemd service unit file
- type: path
- default: /etc/systemd/system

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "[Unit]" > #{systemd_service_path}/#{systemd_service_file}
echo "Description=Atomic Red Team Systemd Service" >> #{systemd_service_path}/#{systemd_service_file}
echo "" >> #{systemd_service_path}/#{systemd_service_file}
echo "[Service]" >> #{systemd_service_path}/#{systemd_service_file}
echo "Type=simple"
echo "ExecStart=#{execstart_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "ExecStartPre=#{execstartpre_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "ExecStartPost=#{execstartpost_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "ExecReload=#{execreload_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "ExecStop=#{execstop_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "ExecStopPost=#{execstoppost_action}" >> #{systemd_service_path}/#{systemd_service_file}
echo "" >> #{systemd_service_path}/#{systemd_service_file}
echo "[Install]" >> #{systemd_service_path}/#{systemd_service_file}
echo "WantedBy=default.target" >> #{systemd_service_path}/#{systemd_service_file}
systemctl daemon-reload
systemctl enable #{systemd_service_file}
systemctl start #{systemd_service_file}
```

### Cleanup

```bash
systemctl stop #{systemd_service_file}
systemctl disable #{systemd_service_file}
rm -rf #{systemd_service_path}/#{systemd_service_file}
systemctl daemon-reload
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml)
