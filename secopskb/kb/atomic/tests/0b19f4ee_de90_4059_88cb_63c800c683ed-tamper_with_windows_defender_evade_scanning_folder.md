---
atomic_guid: "0b19f4ee-de90-4059-88cb-63c800c683ed"
title: "Tamper with Windows Defender Evade Scanning -Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "0b19f4ee-de90-4059-88cb-63c800c683ed"
  - "Tamper with Windows Defender Evade Scanning -Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Malware can exclude a specific path from being scanned and evading detection. 
Upon successul execution, the file provided should be on the list of excluded path. 
To check the exclusion list using poweshell (Get-MpPreference).ExclusionPath

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Input Arguments

### excluded_folder

- description: This folder will be excluded from scanning
- type: path
- default: C:\Temp

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$excludedpath= "#{excluded_folder}"
Add-MpPreference -ExclusionPath $excludedpath
```

### Cleanup

```powershell
$excludedpath= "#{excluded_folder}"
Remove-MpPreference -ExclusionPath $excludedpath
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
