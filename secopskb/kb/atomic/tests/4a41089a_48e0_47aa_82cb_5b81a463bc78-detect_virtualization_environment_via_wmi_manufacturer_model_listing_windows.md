---
atomic_guid: "4a41089a-48e0-47aa-82cb-5b81a463bc78"
title: "Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1497.001"
attack_technique_name: "Virtualization/Sandbox Evasion: System Checks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "4a41089a-48e0-47aa-82cb-5b81a463bc78"
  - "Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Detect Virtualization Environment via WMI Manufacturer/Model Listing (Windows)

Windows Management Instrumentation(WMI) objects contain system information which helps to detect virtualization. This test will get the model and manufacturer of the machine to determine if it is a virtual machine, such as through VMware or VirtualBox.

## Metadata

- Atomic GUID: 4a41089a-48e0-47aa-82cb-5b81a463bc78
- Technique: T1497.001: Virtualization/Sandbox Evasion: System Checks
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1497.001/T1497.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1497-virtualization_sandbox_evasion|T1497.001]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$Manufacturer = Get-WmiObject -Class Win32_ComputerSystem | select-object -expandproperty "Manufacturer"
$Model = Get-WmiObject -Class Win32_ComputerSystem | select-object -expandproperty "Model"
if((($Manufacturer.ToLower() -eq "microsoft corporation") -and ($Model.ToLower().contains("virtual"))) -or ($Manufacturer.ToLower().contains("vmware")) -or ($Model.ToLower() -eq "virtualbox")) {write-host "Virtualization environment detected!"} else {write-host "No virtualization environment detected!"}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1497.001/T1497.001.yaml)
