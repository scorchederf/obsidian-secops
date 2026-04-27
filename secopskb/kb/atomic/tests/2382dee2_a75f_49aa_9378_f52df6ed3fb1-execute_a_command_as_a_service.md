---
atomic_guid: "2382dee2-a75f-49aa-9378-f52df6ed3fb1"
title: "Execute a Command as a Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "2382dee2-a75f-49aa-9378-f52df6ed3fb1"
  - "Execute a Command as a Service"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a service specifying an arbitrary command and executes it. When executing commands such as PowerShell, the service will report that it did not start correctly even when code executes properly.

Upon successful execution, cmd.exe creates a new service using sc.exe that will start powershell.exe to create a new file `art-marker.txt`

[BlackCat Ransomware (ALPHV)](https://www.varonis.com/blog/blackcat-ransomware)  
[Cybereason vs. BlackCat Ransomware](https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware)

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Input Arguments

### executable_command

- description: Command to execute as a service
- type: string
- default: %COMSPEC% /c powershell.exe -nop -w hidden -command New-Item -ItemType File C:\art-marker.txt

### service_name

- description: Name of service to create
- type: string
- default: ARTService

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc.exe create #{service_name} binPath= "#{executable_command}"
sc.exe start #{service_name}
sc.exe delete #{service_name}
```

### Cleanup

```cmd
del C:\art-marker.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
