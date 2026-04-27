---
atomic_guid: "fbff3f1f-b0bf-448e-840f-7e1687affdce"
title: "RemotePC Software Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "fbff3f1f-b0bf-448e-840f-7e1687affdce"
  - "RemotePC Software Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may attempt to trick the user into downloading RemotePC Software for use as a C2 channel. 
Upon successful execution, RemotePC will be executed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219: Remote Access Tools]]

## Input Arguments

### RemotePC_Path

- description: Path of RemotePC executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\RemotePC.exe

## Dependencies

RemotePC must exist on disk at the specified location (#{RemotePC_Path})

### Prerequisite Check

```powershell
if (Test-Path "#{RemotePC_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://static.remotepc.com/downloads/rpc/140422/RemotePC.exe" -OutFile "#{RemotePC_Path}" -UseBasicParsing
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "#{RemotePC_Path}"
```

### Cleanup

```powershell
Unregister-ScheduledTask -TaskName "RemotePC" -Confirm:$False -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName "RPCServiceHealthCheck" -Confirm:$False -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName "ServiceMonitor" -Confirm:$False -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName "StartRPCService" -Confirm:$False -ErrorAction SilentlyContinue      
Stop-Process -Name "RemotePCPerformance" -force -erroraction silentlycontinue
Stop-Process -Name "RPCPerformanceService" -force -erroraction silentlycontinue
Stop-Process -Name "RemotePCUIU" -force -erroraction silentlycontinue
Stop-Process -Name "RPCDownloader" -force -erroraction silentlycontinue
Stop-Process -Name "RemotePCService" -force -erroraction silentlycontinue
Stop-Process -Name "RPCService" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
