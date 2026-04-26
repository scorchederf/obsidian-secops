---
atomic_guid: "161d694c-b543-4434-85c3-c3a433e33792"
title: "Python pty module and spawn function used to spawn sh or bash"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.006"
attack_technique_name: "Command and Scripting Interpreter: Python"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "161d694c-b543-4434-85c3-c3a433e33792"
  - "Python pty module and spawn function used to spawn sh or bash"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python pty module and spawn function used to spawn sh or bash

Uses the Python spawn function to spawn a sh shell followed by a bash shell. Per Volexity, this technique was observed in exploitation of Atlassian Confluence [CVE-2022-26134]. Reference: https://www.volexity.com/blog/2022/06/02/zero-day-exploitation-of-atlassian-confluence

## Metadata

- Atomic GUID: 161d694c-b543-4434-85c3-c3a433e33792
- Technique: T1059.006: Command and Scripting Interpreter: Python
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1059.006/T1059.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.006]]

## Dependencies

Verify if python is in the environment variable path and attempt to import requests library.

### Prerequisite Check

```untitled
which_python=$(which python || which python3 || which python3.9 || which python2); $which_python -V
$which_python -c 'import requests' 2>/dev/null; echo $?
```

### Get Prerequisite

```untitled
pip install requests
```

## Executor

- name: sh

### Command

```bash
which_python=$(which python || which python3 || which python3.9 || which python2)
$which_python -c "import pty;pty.spawn('/bin/sh')"
exit
$which_python -c "import pty;pty.spawn('/bin/bash')"
exit
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml)
