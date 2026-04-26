---
atomic_guid: "6fec8560-ff64-4bbf-bc79-734fea48f7ca"
title: "Masquerade Malicious Service as Legitimate System Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "6fec8560-ff64-4bbf-bc79-734fea48f7ca"
  - "Masquerade Malicious Service as Legitimate System Service"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerade Malicious Service as Legitimate System Service

Creates a systemd service with a name and description closely resembling a legitimate
system service to blend in with normal service activity. Adversaries may deliberately
choose service names similar to well-known system services such as systemd-networkd,
cron, or ssh to evade detection from analysts reviewing service lists or automated
alerting on service names.

This masquerading technique is particularly effective in environments where detection
relies on service name allowlists or manual review of systemctl list-units output
rather than behavioural analysis of service unit file contents and ExecStart paths.

## Metadata

- Atomic GUID: 6fec8560-ff64-4bbf-bc79-734fea48f7ca
- Technique: T1569.003: System Services: Systemctl
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1569.003/T1569.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.003]]

## Input Arguments

### command_to_run

- description: Command the masquerading service will execute
- type: string
- default: /bin/bash -c "echo masquerade > /tmp/atomic_masquerade_output.txt"

### masquerade_name

- description: Service name designed to closely mimic a legitimate system service
- type: string
- default: systemd-network-helper

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

Chosen masquerade service name must not already exist as a real service

### Prerequisite Check

```bash
if ! systemctl list-unit-files --type=service | grep -q "^#{masquerade_name}.service"; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo "A service named #{masquerade_name} already exists. Change the masquerade_name input argument to avoid conflicts."
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "[Unit]" > /etc/systemd/system/#{masquerade_name}.service
echo "Description=Network connectivity helper service" >> /etc/systemd/system/#{masquerade_name}.service
echo "After=network.target" >> /etc/systemd/system/#{masquerade_name}.service
echo "Before=network-online.target" >> /etc/systemd/system/#{masquerade_name}.service
echo "" >> /etc/systemd/system/#{masquerade_name}.service
echo "[Service]" >> /etc/systemd/system/#{masquerade_name}.service
echo "ExecStart=#{command_to_run}" >> /etc/systemd/system/#{masquerade_name}.service
echo "Restart=on-failure" >> /etc/systemd/system/#{masquerade_name}.service
echo "RestartSec=5" >> /etc/systemd/system/#{masquerade_name}.service
echo "" >> /etc/systemd/system/#{masquerade_name}.service
echo "[Install]" >> /etc/systemd/system/#{masquerade_name}.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/#{masquerade_name}.service
systemctl daemon-reload
systemctl start #{masquerade_name}.service
systemctl status #{masquerade_name}.service
```

### Cleanup

```bash
systemctl stop #{masquerade_name}.service 2>/dev/null || true
systemctl disable #{masquerade_name}.service 2>/dev/null || true
rm -f /etc/systemd/system/#{masquerade_name}.service
systemctl daemon-reload
rm -f /tmp/atomic_masquerade_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
