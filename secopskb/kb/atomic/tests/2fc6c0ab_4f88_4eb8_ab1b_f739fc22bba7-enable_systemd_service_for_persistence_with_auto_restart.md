---
atomic_guid: "2fc6c0ab-4f88-4eb8-ab1b-f739fc22bba7"
title: "Enable systemd Service for Persistence with Auto-Restart"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "2fc6c0ab-4f88-4eb8-ab1b-f739fc22bba7"
  - "Enable systemd Service for Persistence with Auto-Restart"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enable systemd Service for Persistence with Auto-Restart

Creates a payload script and a systemd service unit that executes it, then enables
the service to survive reboots using systemctl enable. The service is configured with
Restart=always to automatically restart on failure, mimicking the persistence mechanism
used by adversaries deploying backdoors or beacons on Linux hosts.

This technique is consistent with observed post-exploitation tradecraft where adversaries
establish a foothold that survives reboots and self-heals after interruption, complicating
incident response and remediation efforts.

## Metadata

- Atomic GUID: 2fc6c0ab-4f88-4eb8-ab1b-f739fc22bba7
- Technique: T1569.003: System Services: Systemctl
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1569.003/T1569.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.003]]

## Input Arguments

### payload_path

- description: Path to the payload script that the service will execute
- type: path
- default: /tmp/atomic_payload.sh

### service_name

- description: Name of the persistence service to create
- type: string
- default: atomic-persist

## Dependencies

systemctl must be available on the system

### Prerequisite Check

```bash
if [ -x "$(command -v systemctl)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo "systemctl is not available. Ensure systemd is running on this system."
```

The test must be run as root or with sudo privileges

### Prerequisite Check

```bash
if [ "$(id -u)" -eq 0 ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo "This test requires root privileges. Run as root or use sudo."
```

/etc/systemd/system/ directory must exist and be writable

### Prerequisite Check

```bash
if [ -d "/etc/systemd/system" ] && [ -w "/etc/systemd/system" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo "/etc/systemd/system/ does not exist or is not writable."
```

Payload script must exist at the specified path

### Prerequisite Check

```bash
if [ -f "#{payload_path}" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo '#!/bin/bash' > #{payload_path}
echo 'echo persistent >> /tmp/atomic_persist_output.txt' >> #{payload_path}
chmod +x #{payload_path}
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "[Unit]" > /etc/systemd/system/#{service_name}.service
echo "Description=Atomic Persistence Service" >> /etc/systemd/system/#{service_name}.service
echo "After=network.target" >> /etc/systemd/system/#{service_name}.service
echo "" >> /etc/systemd/system/#{service_name}.service
echo "[Service]" >> /etc/systemd/system/#{service_name}.service
echo "ExecStart=#{payload_path}" >> /etc/systemd/system/#{service_name}.service
echo "Restart=always" >> /etc/systemd/system/#{service_name}.service
echo "RestartSec=10" >> /etc/systemd/system/#{service_name}.service
echo "" >> /etc/systemd/system/#{service_name}.service
echo "[Install]" >> /etc/systemd/system/#{service_name}.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/#{service_name}.service
systemctl daemon-reload
systemctl enable #{service_name}.service
systemctl start #{service_name}.service
systemctl status #{service_name}.service
```

### Cleanup

```bash
systemctl stop #{service_name}.service 2>/dev/null || true
systemctl disable #{service_name}.service 2>/dev/null || true
rm -f /etc/systemd/system/#{service_name}.service
rm -f /etc/systemd/system/multi-user.target.wants/#{service_name}.service
systemctl daemon-reload
rm -f #{payload_path}
rm -f /tmp/atomic_persist_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
