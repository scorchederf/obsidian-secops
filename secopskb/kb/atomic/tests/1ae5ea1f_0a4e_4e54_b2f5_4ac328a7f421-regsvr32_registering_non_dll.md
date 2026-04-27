---
atomic_guid: "1ae5ea1f-0a4e-4e54-b2f5-4ac328a7f421"
title: "Regsvr32 Registering Non DLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.010"
attack_technique_name: "Signed Binary Proxy Execution: Regsvr32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "1ae5ea1f-0a4e-4e54-b2f5-4ac328a7f421"
  - "Regsvr32 Registering Non DLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Replicating observed Gozi maldoc behavior registering a dll with an altered extension

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]

## Input Arguments

### dll_file

- description: Path to renamed dll file to be registered
- type: path
- default: %temp%\shell32.jpg

### regsvr32name

- description: Default name of Regsvr32.exe
- type: string
- default: regsvr32.exe

### regsvr32path

- description: Default location of Regsvr32.exe
- type: path
- default: C:\Windows\system32

## Dependencies

Test requires a renamed dll file

### Prerequisite Check

```cmd
if exist #{dll_file} ( exit 0 ) else ( exit 1 )
```

### Get Prerequisite

```cmd
copy "C:\Windows\System32\shell32.dll" "#{dll_file}"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
#{regsvr32path}\#{regsvr32name} /s #{dll_file}
```

### Cleanup

```cmd
#{regsvr32path}\#{regsvr32name} /U /s #{dll_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.010/T1218.010.yaml)
