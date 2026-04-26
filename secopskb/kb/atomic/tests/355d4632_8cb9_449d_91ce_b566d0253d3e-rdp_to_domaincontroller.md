---
atomic_guid: "355d4632-8cb9-449d-91ce-b566d0253d3e"
title: "RDP to DomainController"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.001"
attack_technique_name: "Remote Services: Remote Desktop Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "355d4632-8cb9-449d-91ce-b566d0253d3e"
  - "RDP to DomainController"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP to DomainController

Attempt an RDP session via Remote Desktop Application to a DomainController.

## Metadata

- Atomic GUID: 355d4632-8cb9-449d-91ce-b566d0253d3e
- Technique: T1021.001: Remote Services: Remote Desktop Protocol
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1021.001/T1021.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Input Arguments

### domain

- description: domain argument default %USERDOMAIN%
- type: string
- default: $Env:USERDOMAIN

### logonserver

- description: ComputerName argument default %logonserver%
- type: string
- default: $ENV:logonserver.TrimStart("\")

### password

- description: Password
- type: string
- default: 1password2!

### username

- description: Username argument default %username%
- type: string
- default: $ENV:USERNAME

## Dependencies

Computer must be domain joined

### Prerequisite Check

```untitled
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) { exit 0} else { exit 1}
```

### Get Prerequisite

```untitled
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: powershell

### Command

```powershell
$Server=#{logonserver}
$User = Join-Path #{domain} #{username}
$Password="#{password}"
cmdkey /generic:TERMSRV/$Server /user:$User /pass:$Password
mstsc /v:$Server
echo "RDP connection established"
```

### Cleanup

```powershell
$p=Tasklist /svc /fi "IMAGENAME eq mstsc.exe" /fo csv | convertfrom-csv
if(-not ([string]::IsNullOrEmpty($p.PID))) { Stop-Process -Id $p.PID }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml)
