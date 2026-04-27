---
atomic_guid: "b04284dc-3bd9-4840-8d21-61b8d31c99f2"
title: "Logging sh history to syslog/messages"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "b04284dc-3bd9-4840-8d21-61b8d31c99f2"
  - "Logging sh history to syslog/messages"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Logging sh history to syslog/messages

There are several variables that can be set to control the appearance of the bash command prompt: PS1, PS2, PS3, PS4 and PROMPT_COMMAND. The contents of these variables are executed as if they had been typed on the command line. The PROMPT_COMMAND variable "if set" will be executed before the PS1 variable and can be configured to write the latest "bash history" entries to the syslog.

To gain persistence the command could be added to the users .shrc or .profile

## Metadata

- Atomic GUID: b04284dc-3bd9-4840-8d21-61b8d31c99f2
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Dependencies

This test requires to be run in a bash shell and that logger and tee are installed.

### Prerequisite Check

```bash
if [ "$(echo $SHELL)" != "/bin/sh" ]; then echo -e "\n***** sh not running! *****\n"; exit 1; fi
if [ ! -x "$(command -v logger)" ]; then echo -e "\n***** logger NOT installed *****\n"; exit 1; fi
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
PS2=`logger -t "$USER" -f ~/.sh_history`
$PS2
tail /var/log/messages
```

### Cleanup

```bash
unset PS2
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
