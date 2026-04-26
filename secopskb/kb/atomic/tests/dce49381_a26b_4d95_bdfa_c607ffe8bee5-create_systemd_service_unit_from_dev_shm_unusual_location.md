---
atomic_guid: "dce49381-a26b-4d95-bdfa-c607ffe8bee5"
title: "Create systemd Service Unit from /dev/shm (Unusual Location)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "dce49381-a26b-4d95-bdfa-c607ffe8bee5"
  - "Create systemd Service Unit from /dev/shm (Unusual Location)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create systemd Service Unit from /dev/shm (Unusual Location)

Creates a systemd service unit file in /dev/shm and loads it using systemctl.
/dev/shm is a memory-backed filesystem that is world-writable on most Linux systems
and does not persist across reboots, making it particularly attractive to adversaries
seeking to execute transient payloads while evading file-based forensic detection.

This technique has been observed in post-exploitation scenarios where attackers
deliberately avoid writing to disk-backed locations to limit forensic artefacts.

## Metadata

- Atomic GUID: dce49381-a26b-4d95-bdfa-c607ffe8bee5
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

- description: Command the service will execute
- type: string
- default: /bin/bash -c "whoami > /tmp/atomic_shm_output.txt"

### service_path

- description: Full path to the service file to be written in /dev/shm
- type: path
- default: /dev/shm/atomic_shm.service

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

/dev/shm must exist and be writable

### Prerequisite Check

```bash
if [ -d "/dev/shm" ] && [ -w "/dev/shm" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
echo "/dev/shm does not exist or is not writable on this system."
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

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "[Unit]" > #{service_path}
echo "Description=Atomic SHM Service" >> #{service_path}
echo "" >> #{service_path}
echo "[Service]" >> #{service_path}
echo "ExecStart=#{command_to_run}" >> #{service_path}
echo "" >> #{service_path}
echo "[Install]" >> #{service_path}
echo "WantedBy=multi-user.target" >> #{service_path}
systemctl link #{service_path}
systemctl start $(basename #{service_path})
systemctl status $(basename #{service_path})
```

### Cleanup

```bash
systemctl stop $(basename #{service_path}) 2>/dev/null || true
rm -f #{service_path}
rm -f /tmp/atomic_shm_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
