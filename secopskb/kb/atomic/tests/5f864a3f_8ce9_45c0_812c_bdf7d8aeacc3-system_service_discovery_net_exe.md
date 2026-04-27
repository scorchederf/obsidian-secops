---
atomic_guid: "5f864a3f-8ce9-45c0-812c-bdf7d8aeacc3"
title: "System Service Discovery - net.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1007"
attack_technique_name: "System Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "5f864a3f-8ce9-45c0-812c-bdf7d8aeacc3"
  - "System Service Discovery - net.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates started system services using net.exe and writes them to a file. This technique has been used by multiple threat actors.

Upon successful execution, net.exe will run from cmd.exe that queries services. Expected output is to a txt file in in the temp directory called service-list.txt.

## ATT&CK Mapping

- [[kb/attack/techniques/T1007-system_service_discovery|T1007: System Service Discovery]]

## Input Arguments

### output_file

- description: Path of file to hold net.exe output
- type: path
- default: %temp%\service-list.txt

## Executor

- name: command_prompt

### Command

```cmd
net.exe start >> #{output_file}
```

### Cleanup

```cmd
del /f /q /s #{output_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1007/T1007.yaml)
