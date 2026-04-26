---
atomic_guid: "bdaebd56-368b-4970-a523-f905ff4a8a51"
title: "Environment variable scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "bdaebd56-368b-4970-a523-f905ff4a8a51"
  - "Environment variable scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Environment variable scripts

An adversary may place scripts in an environment variable because they can't or don't wish to create script files on the host. The following test, in a bash shell, exports the ART variable containing an echo command, then pipes the variable to /bin/bash

## Metadata

- Atomic GUID: bdaebd56-368b-4970-a523-f905ff4a8a51
- Technique: T1059.004: Command and Scripting Interpreter: Bash
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1059.004/T1059.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Executor

- elevation_required: False
- name: sh

### Command

```sh
export ART='echo "Atomic Red Team was here... T1059.004"'
echo $ART |/bin/sh
```

### Cleanup

```sh
unset ART
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
