---
atomic_guid: "dc6fe391-69e6-4506-bd06-ea5eeb4082f8"
title: "Deobfuscate/Decode Files Or Information"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "dc6fe391-69e6-4506-bd06-ea5eeb4082f8"
  - "Deobfuscate/Decode Files Or Information"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Deobfuscate/Decode Files Or Information

Encode/Decode executable
Upon execution a file named T1140_calc_decoded.exe will be placed in the temp folder

## Metadata

- Atomic GUID: dc6fe391-69e6-4506-bd06-ea5eeb4082f8
- Technique: T1140: Deobfuscate/Decode Files or Information
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1140/T1140.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Input Arguments

### executable

- description: name of executable
- type: path
- default: C:\Windows\System32\calc.exe

## Executor

- name: command_prompt

### Command

```commandprompt
certutil -encode #{executable} %temp%\T1140_calc.txt
certutil -decode %temp%\T1140_calc.txt %temp%\T1140_calc_decoded.exe
```

### Cleanup

```commandprompt
del %temp%\T1140_calc.txt >nul 2>&1
del %temp%\T1140_calc_decoded.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
