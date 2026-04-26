---
atomic_guid: "0e59d59d-3265-4d35-bebd-bf5c1ec40db5"
title: "Logging bash history to syslog"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "0e59d59d-3265-4d35-bebd-bf5c1ec40db5"
  - "Logging bash history to syslog"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Logging bash history to syslog

There are several variables that can be set to control the appearance of the bash command prompt: PS1, PS2, PS3, PS4 and PROMPT_COMMAND. The contents of these variables are executed as if they had been typed on the command line. The PROMPT_COMMAND variable "if set" will be executed before the PS1 variable and can be configured to write the latest "bash history" entries to the syslog.

To gain persistence the command could be added to the users .bashrc or .bash_aliases or the systems default .bashrc in /etc/skel/

## Metadata

- Atomic GUID: 0e59d59d-3265-4d35-bebd-bf5c1ec40db5
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

```text
if [ "$(echo $SHELL)" != "/bin/bash" ]; then echo -e "\n***** Bash not running! *****\n"; exit 1; fi
if [ ! -x "$(command -v logger)" ]; then echo -e "\n***** logger NOT installed *****\n"; exit 1; fi
if [ ! -x "$(command -v tee)" ]; then echo -e "\n***** tee NOT installed *****\n"; exit 1; fi
```

### Get Prerequisite

```text
echo ""
```

## Executor

- elevation_required: True
- name: sh

### Command

```sh
PROMPT_COMMAND='history -a >(tee -a ~/.bash_history |logger -t "$USER[$$] $SSH_CONNECTION ")'
echo "\$PROMPT_COMMAND=$PROMPT_COMMAND"
tail /var/log/syslog
```

### Cleanup

```sh
unset PROMPT_COMMAND
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
