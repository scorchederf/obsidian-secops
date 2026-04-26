---
atomic_guid: "491a4af6-a521-4b74-b23b-f7b3f1ee9e77"
title: "Service Installation PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.003"
attack_technique_name: "Create or Modify System Process: Windows Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "491a4af6-a521-4b74-b23b-f7b3f1ee9e77"
  - "Service Installation PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Service Installation PowerShell

Installs A Local Service via PowerShell.
Upon successful execution, powershell will download `AtomicService.exe` from github. Powershell will then use `New-Service` and `Start-Service` to start service. Results will be displayed.

## Metadata

- Atomic GUID: 491a4af6-a521-4b74-b23b-f7b3f1ee9e77
- Technique: T1543.003: Create or Modify System Process: Windows Service
- Platforms: windows
- Executor: powershell
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
- default: AtomicTestService_PowerShell

## Dependencies

Service binary must exist on disk at specified location (#{binary_path})

### Prerequisite Check

```text
if (Test-Path "#{binary_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{binary_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1543.003/bin/AtomicService.exe" -OutFile "#{binary_path}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-Service -Name "#{service_name}" -BinaryPathName "#{binary_path}"
Start-Service -Name "#{service_name}"
```

### Cleanup

```powershell
Stop-Service -Name "#{service_name}" 2>&1 | Out-Null
try {(Get-WmiObject Win32_Service -filter "name='#{service_name}'").Delete()}
catch {}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml)
