---
atomic_guid: "8206dd0c-faf6-4d74-ba13-7fbe13dce6ac"
title: "X Windows Capture"
framework: "atomic"
generated: "true"
attack_technique_id: "T1113"
attack_technique_name: "Screen Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "8206dd0c-faf6-4d74-ba13-7fbe13dce6ac"
  - "X Windows Capture"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use xwd command to collect a full desktop screenshot and review file with xwud

## ATT&CK Mapping

- [[kb/attack/techniques/T1113-screen_capture|T1113: Screen Capture]]

## Input Arguments

### output_file

- description: Output file path
- type: path
- default: /tmp/T1113_desktop.xwd

### package_checker

- description: Package checking command for linux. Debian system command- dpkg -s x11-apps
- type: string
- default: rpm -q xorg-x11-apps

### package_installer

- description: Package installer command for linux. Debian system command- apt-get install x11-apps
- type: string
- default: yum install -y xorg-x11-apps

## Dependencies

Package with XWD and XWUD must exist on device

### Prerequisite Check

```bash
if #{package_checker} > /dev/null; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
sudo #{package_installer}
```

## Executor

- name: bash

### Command

```bash
xwd -root -out #{output_file}
xwud -in #{output_file}
```

### Cleanup

```bash
rm #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1113/T1113.yaml)
