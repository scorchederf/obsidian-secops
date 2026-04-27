---
atomic_guid: "0d80d088-a84c-4353-af1a-fc8b439f1564"
title: "Enumerate COM Objects in Registry with Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1012"
attack_technique_name: "Query Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0d80d088-a84c-4353-af1a-fc8b439f1564"
  - "Enumerate COM Objects in Registry with Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enumerate COM Objects in Registry with Powershell

This test is designed to enumerate the COM objects listed in HKCR, then output their methods and CLSIDs to a text file.
An adversary could then use this information to identify COM objects that might be vulnerable to abuse, such as using them to spawn arbitrary processes. 
See: https://www.mandiant.com/resources/hunting-com-objects

## Metadata

- Atomic GUID: 0d80d088-a84c-4353-af1a-fc8b439f1564
- Technique: T1012: Query Registry
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1012/T1012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Input Arguments

### output_file

- description: File to output list of COM objects to
- type: string
- default: $env:temp\T1592.002Test1.txt

## Executor

- name: powershell

### Command

```powershell
New-PSDrive -PSProvider registry -Root HKEY_CLASSES_ROOT -Name HKCR
Get-ChildItem -Path HKCR:\CLSID -Name | Select -Skip 1 > $env:temp\clsids.txt
ForEach($CLSID in Get-Content "$env:temp\clsids.txt")
{try{write-output "$($Position)-$($CLSID)"
write-output "------------"| out-file #{output_file} -append
write-output $($CLSID)| out-file #{output_file} -append
$handle=[activator]::CreateInstance([type]::GetTypeFromCLSID($CLSID))
$handle | get-member -erroraction silentlycontinue | out-file #{output_file} -append
$position += 1} catch{}}
```

### Cleanup

```powershell
remove-item #{output_file} -force -erroraction silentlycontinue
remove-item $env:temp\clsids.txt -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml)
