---
atomic_guid: "1e5be8d4-605a-4acb-8709-2f80b2d8ea95"
title: "Enumerate All systemd Services Using systemctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.003"
attack_technique_name: "System Services: Systemctl"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "1e5be8d4-605a-4acb-8709-2f80b2d8ea95"
  - "Enumerate All systemd Services Using systemctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate All systemd Services Using systemctl

Enumerates all systemd services and their current states using systemctl list-units
and systemctl list-unit-files. Adversaries may enumerate running and enabled services
to identify targets for hijacking, understand the host environment, map installed
security tooling, or identify gaps in monitoring coverage.

Service enumeration is a common reconnaissance step during post-exploitation and may
precede service hijacking or masquerading activity. This test does not require
elevation as service listing is available to unprivileged users on most Linux systems.

## Metadata

- Atomic GUID: 1e5be8d4-605a-4acb-8709-2f80b2d8ea95
- Technique: T1569.003: System Services: Systemctl
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1569.003/T1569.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.003]]

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

## Executor

- elevation_required: False
- name: sh

### Command

```bash
systemctl list-units --type=service --all
systemctl list-unit-files --type=service
```

### Cleanup

```bash
echo "No cleanup required"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.003/T1569.003.yaml)
