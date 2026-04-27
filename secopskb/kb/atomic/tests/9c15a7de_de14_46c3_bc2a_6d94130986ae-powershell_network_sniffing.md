---
atomic_guid: "9c15a7de-de14-46c3-bc2a-6d94130986ae"
title: "PowerShell Network Sniffing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "9c15a7de-de14-46c3-bc2a-6d94130986ae"
  - "PowerShell Network Sniffing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PowerShell Built-in Cmdlets to capture network traffic.
https://learn.microsoft.com/en-us/powershell/module/neteventpacketcapture/new-neteventsession?view=windowsserver2022-ps

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040: Network Sniffing]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-NetEventSession -Name Capture007 -LocalFilePath "$ENV:Temp\sniff.etl"
Add-NetEventPacketCaptureProvider -SessionName Capture007 -TruncationLength 100
Start-NetEventSession -Name Capture007
Stop-NetEventSession -Name Capture007
Remove-NetEventSession -Name Capture007
```

### Cleanup

```powershell
del $ENV:Temp\sniff.etl
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
