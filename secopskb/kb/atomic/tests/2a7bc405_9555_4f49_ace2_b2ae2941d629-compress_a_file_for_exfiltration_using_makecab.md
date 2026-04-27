---
atomic_guid: "2a7bc405-9555-4f49-ace2-b2ae2941d629"
title: "Compress a File for Exfiltration using Makecab"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "2a7bc405-9555-4f49-ace2-b2ae2941d629"
  - "Compress a File for Exfiltration using Makecab"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may compress data using Makecab (in-built Windows binary) that is collected prior to exfiltration.
[reference](https://unit42.paloaltonetworks.com/exchange-server-credential-harvesting/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Input Arguments

### input_file

- description: Path to source file for compression
- type: path
- default: C:\Temp\sam.hiv

### output_file

- description: Path of the CAB file
- type: path
- default: C:\Temp\art.zip

## Dependencies

A sample file for compression must be located at specified location (#{input_file})

### Prerequisite Check

```untitled
if not exist "#{input_file}" (exit /b 1)
```

### Get Prerequisite

```untitled
fsutil file createnew c:\Temp\sam.hiv 10485760
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
makecab.exe #{input_file} #{output_file}
```

### Cleanup

```cmd
del #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
