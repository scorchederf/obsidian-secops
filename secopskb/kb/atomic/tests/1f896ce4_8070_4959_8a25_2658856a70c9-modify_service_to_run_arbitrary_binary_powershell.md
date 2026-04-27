---
atomic_guid: "1f896ce4-8070-4959-8a25-2658856a70c9"
title: "Modify Service to Run Arbitrary Binary (Powershell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.003"
attack_technique_name: "Create or Modify System Process: Windows Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "1f896ce4-8070-4959-8a25-2658856a70c9"
  - "Modify Service to Run Arbitrary Binary (Powershell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Service to Run Arbitrary Binary (Powershell)

This test will use PowerShell to temporarily modify a service to run an arbitrary executable by changing its binary path and will then revert the binary path change, restoring the service to its original state.
This technique was previously observed through SnapMC's use of Powerspolit's invoke-serviceabuse function. 
[Reference](https://blog.fox-it.com/2021/10/11/snapmc-skips-ransomware-steals-data/)

## Metadata

- Atomic GUID: 1f896ce4-8070-4959-8a25-2658856a70c9
- Technique: T1543.003: Create or Modify System Process: Windows Service
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1543.003/T1543.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Input Arguments

### new_bin_path

- description: Path of the new service binary
- type: String
- default: $env:windir\system32\notepad.exe

### original_bin_path

- description: Path of the original service binary
- type: String
- default: $env:windir\system32\fxssvc.exe

### service_name

- description: Name of the service to modify
- type: string
- default: fax

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Stop-Service -Name "#{service_name}" -force -erroraction silentlycontinue | Out-Null
set-servicebinarypath -name "#{service_name}" -path "#{new_bin_path}"
start-service -Name "#{service_name}" -erroraction silentlycontinue | out-null
```

### Cleanup

```powershell
Stop-Service -Name "#{service_name}" -force -erroraction silentlycontinue | Out-Null
set-servicebinarypath -name "#{service_name}" -path "#{original_bin_path}" -erroraction silentlycontinue | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml)
