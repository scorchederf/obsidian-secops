---
atomic_guid: "6ca45b04-9f15-4424-b9d3-84a217285a5c"
title: "Port Scan using python"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "6ca45b04-9f15-4424-b9d3-84a217285a5c"
  - "Port Scan using python"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Port Scan using python

Scan ports to check for listening ports with python

## Metadata

- Atomic GUID: 6ca45b04-9f15-4424-b9d3-84a217285a5c
- Technique: T1046: Network Service Discovery
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Input Arguments

### filename

- description: Location of the project file
- type: path
- default: PathToAtomicsFolder\T1046\src\T1046.py

### host_ip

- description: Host to scan.
- type: string
- default: 127.0.0.1

## Dependencies

Check if python exists on the machine

### Prerequisite Check

```powershell
if (Get-Command py -errorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
invoke-webrequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe" -outfile "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe"
Start-Process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\python_setup.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait
```

## Executor

- name: powershell

### Command

```powershell
python "#{filename}" -i #{host_ip}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
