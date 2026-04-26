---
atomic_guid: "7c35779d-42ec-42ab-a283-6255b28e9d68"
title: "Check internet connection using Test-NetConnection in PowerShell (TCP-HTTP)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016.001"
attack_technique_name: "System Network Configuration Discovery: Internet Connection Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7c35779d-42ec-42ab-a283-6255b28e9d68"
  - "Check internet connection using Test-NetConnection in PowerShell (TCP-HTTP)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Check internet connection using Test-NetConnection in PowerShell (TCP-HTTP)

Check internet connection using PowerShell's Test-NetConnection cmdlet and the TCP protocol to check for outbound HTTP (Port 80) access. The default target is www.google.com.

## Metadata

- Atomic GUID: 7c35779d-42ec-42ab-a283-6255b28e9d68
- Technique: T1016.001: System Network Configuration Discovery: Internet Connection Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1016.001/T1016.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016.001]]

## Input Arguments

### target

- description: target of the request
- type: string
- default: www.google.com

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Test-NetConnection -CommonTCPPort HTTP -ComputerName #{target}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016.001/T1016.001.yaml)
