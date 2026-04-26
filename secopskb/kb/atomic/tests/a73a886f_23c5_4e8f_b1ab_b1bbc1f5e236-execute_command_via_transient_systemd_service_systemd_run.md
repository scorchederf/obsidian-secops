---
atomic_guid: "a73a886f-23c5-4e8f-b1ab-b1bbc1f5e236"
title: "Execute Command via Transient systemd Service (systemd-run)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "a73a886f-23c5-4e8f-b1ab-b1bbc1f5e236"
  - "Execute Command via Transient systemd Service (systemd-run)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute Command via Transient systemd Service (systemd-run)

Uses systemd-run to execute a command as a transient systemd service without creating
a persistent unit file on disk. Adversaries may use systemd-run to execute arbitrary
commands under the context of systemd while bypassing controls that monitor for new
unit file creation, since transient services exist only in memory for their lifetime.

This is a particularly stealthy technique as it leaves minimal on-disk artefacts and
the service disappears from systemctl list-units once execution completes.

## Metadata

- Atomic GUID: a73a886f-23c5-4e8f-b1ab-b1bbc1f5e236
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

- description: Command to execute as a transient service
- type: string
- default: /bin/bash -c "id > /tmp/atomic_transient_output.txt"

### unit_name

- description: Name of the transient systemd unit to create
- type: string
- default: atomic-transient

## Dependencies

systemd-run must be available on the system

### Prerequisite Check

```text
if [ -x "$(command -v systemd-run)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "systemd-run is not available. Ensure systemd is installed and up to date."
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

## Executor

- elevation_required: True
- name: sh

### Command

```sh
systemd-run --unit=#{unit_name} --wait #{command_to_run}
systemctl status #{unit_name}.service 2>/dev/null || echo "Transient service has already completed and exited."
```

### Cleanup

```sh
systemctl stop #{unit_name}.service 2>/dev/null || true
rm -f /tmp/atomic_transient_output.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
