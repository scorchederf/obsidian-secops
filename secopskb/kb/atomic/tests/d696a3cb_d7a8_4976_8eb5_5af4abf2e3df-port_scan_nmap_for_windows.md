---
atomic_guid: "d696a3cb-d7a8-4976-8eb5-5af4abf2e3df"
title: "Port Scan NMap for Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1046"
attack_technique_name: "Network Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "d696a3cb-d7a8-4976-8eb5-5af4abf2e3df"
  - "Port Scan NMap for Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Port Scan NMap for Windows

Scan ports to check for listening ports for the local host 127.0.0.1

## Metadata

- Atomic GUID: d696a3cb-d7a8-4976-8eb5-5af4abf2e3df
- Technique: T1046: Network Service Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1046/T1046.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Input Arguments

### host_to_scan

- description: The host to scan with NMap
- type: string
- default: 127.0.0.1

### nmap_url

- description: NMap installer download URL
- type: url
- default: https://nmap.org/dist/nmap-7.80-setup.exe

## Dependencies

NMap must be installed

### Prerequisite Check

```text
if (cmd /c "nmap 2>nul") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\nmap-7.80-setup.exe" #{nmap_url}
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\nmap-7.80-setup.exe" /S
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
nmap #{host_to_scan}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1046/T1046.yaml)
