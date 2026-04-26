---
atomic_guid: "bc15c13f-d121-4b1f-8c7d-28d95854d086"
title: "Masquerading - non-windows exe running as windows exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "bc15c13f-d121-4b1f-8c7d-28d95854d086"
  - "Masquerading - non-windows exe running as windows exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading - non-windows exe running as windows exe

Copies an exe, renames it as a windows exe, and launches it to masquerade as a real windows exe

Upon successful execution, powershell will execute T1036.003.exe as svchost.exe from on a non-standard path.

## Metadata

- Atomic GUID: bc15c13f-d121-4b1f-8c7d-28d95854d086
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Input Arguments

### inputfile

- description: path of file to copy
- type: path
- default: PathToAtomicsFolder\T1036.003\bin\T1036.003.exe

### outputfile

- description: path of file to execute
- type: path
- default: ($env:TEMP + "\svchost.exe")

## Dependencies

Exe file to copy must exist on disk at specified location (#{inputfile})

### Prerequisite Check

```powershell
if (Test-Path "#{inputfile}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{inputfile}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1036.003/bin/T1036.003.exe" -OutFile "#{inputfile}"
```

## Executor

- name: powershell

### Command

```powershell
copy "#{inputfile}" #{outputfile}
try { $myT1036_003 = (Start-Process -PassThru -FilePath #{outputfile}).Id }
catch { $_; exit $_.Exception.HResult}
Stop-Process -ID $myT1036_003
```

### Cleanup

```powershell
Remove-Item #{outputfile} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
