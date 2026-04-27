---
atomic_guid: "2cb4dbf2-2dca-4597-8678-4d39d207a3a5"
title: "Win32_PnPEntity Hardware Inventory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1120"
attack_technique_name: "Peripheral Device Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "2cb4dbf2-2dca-4597-8678-4d39d207a3a5"
  - "Win32_PnPEntity Hardware Inventory"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Perform peripheral device discovery using Get-WMIObject Win32_PnPEntity

## ATT&CK Mapping

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120: Peripheral Device Discovery]]

## Executor

- name: powershell

### Command

```powershell
Get-WMIObject Win32_PnPEntity | Format-Table Name, Description, Manufacturer > $env:TEMP\T1120_collection.txt
$Space,$Heading,$Break,$Data = Get-Content $env:TEMP\T1120_collection.txt
@($Heading; $Break; $Data |Sort-Object -Unique) | ? {$_.trim() -ne "" } |Set-Content $env:TEMP\T1120_collection.txt
```

### Cleanup

```powershell
Remove-Item $env:TEMP\T1120_collection.txt -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1120/T1120.yaml)
