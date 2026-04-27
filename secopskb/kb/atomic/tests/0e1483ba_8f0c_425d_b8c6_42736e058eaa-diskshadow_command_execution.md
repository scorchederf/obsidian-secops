---
atomic_guid: "0e1483ba-8f0c-425d-b8c6-42736e058eaa"
title: "DiskShadow Command Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "0e1483ba-8f0c-425d-b8c6-42736e058eaa"
  - "DiskShadow Command Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Emulates attack with a DiskShadow.exe (LOLBIN installed by default on Windows) being used to execute arbitrary commands Reference: https://bohops.com/2018/03/26/diskshadow-the-return-of-vss-evasion-persistence-and-active-directory-database-extraction/

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### dspath

- description: Default location of DiskShadow.exe
- type: path
- default: C:\Windows\System32\diskshadow.exe

### txt_payload

- description: txt to execute
- type: path
- default: PathToAtomicsFolder\T1218\src\T1218.txt

## Dependencies

txt file must exist on disk at specified location (#{txt_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{txt_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{txt_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/T1218.txt" -OutFile "#{txt_payload}"
```

DiskShadow.exe must exist on disk at specified location (#{dspath})

### Prerequisite Check

```powershell
if (Test-Path #{dspath}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
echo "DiskShadow.exe not found on disk at expected location"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
#{dspath} -S #{txt_payload}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
