---
atomic_guid: "a668edb9-334e-48eb-8c2e-5413a40867af"
title: "Auditd keylogger"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "a668edb9-334e-48eb-8c2e-5413a40867af"
  - "Auditd keylogger"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Auditd keylogger

The linux audit tool auditd can be used to capture 32 and 64 bit command execution and place the command in the /var/log/audit/audit.log audit log.

## Metadata

- Atomic GUID: a668edb9-334e-48eb-8c2e-5413a40867af
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Dependencies

This test requires sshd and auditd

### Prerequisite Check

```bash
if [ ! -x "$(command -v auditd)" ]; then echo -e "\n***** auditd NOT installed *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
echo ""
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
auditctl -a always,exit -F arch=b64 -S execve -k CMDS 
auditctl -a always,exit -F arch=b32 -S execve -k CMDS
whoami; ausearch -i --start now
```

### Cleanup

```bash
systemctl restart auditd
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
