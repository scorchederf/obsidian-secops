---
atomic_guid: "7e7ac3ed-f795-4fa5-b711-09d6fbe9b873"
title: "Create and Execute Bash Shell Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.004"
attack_technique_name: "Command and Scripting Interpreter: Bash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "7e7ac3ed-f795-4fa5-b711-09d6fbe9b873"
  - "Create and Execute Bash Shell Script"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates and executes a simple sh script.

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]

## Input Arguments

### host

- description: Host to ping
- type: string
- default: 8.8.8.8

### script_path

- description: Script path
- type: path
- default: /tmp/art.sh

## Executor

- name: sh

### Command

```bash
sh -c "echo 'echo Hello from the Atomic Red Team' > #{script_path}"
sh -c "echo 'ping -c 4 #{host}' >> #{script_path}"
chmod +x #{script_path}
sh #{script_path}
```

### Cleanup

```bash
rm #{script_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.004/T1059.004.yaml)
