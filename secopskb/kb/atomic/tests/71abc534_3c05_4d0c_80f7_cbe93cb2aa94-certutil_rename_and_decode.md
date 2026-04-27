---
atomic_guid: "71abc534-3c05-4d0c-80f7-cbe93cb2aa94"
title: "Certutil Rename and Decode"
framework: "atomic"
generated: "true"
attack_technique_id: "T1140"
attack_technique_name: "Deobfuscate/Decode Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "71abc534-3c05-4d0c-80f7-cbe93cb2aa94"
  - "Certutil Rename and Decode"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Certutil Rename and Decode

Rename certutil and decode a file. This is in reference to latest research by FireEye [here](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)

## Metadata

- Atomic GUID: 71abc534-3c05-4d0c-80f7-cbe93cb2aa94
- Technique: T1140: Deobfuscate/Decode Files or Information
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1140/T1140.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Input Arguments

### executable

- description: name of executable/file to decode
- type: path
- default: C:\Windows\System32\calc.exe

## Executor

- name: command_prompt

### Command

```cmd
copy %windir%\system32\certutil.exe %temp%\tcm.tmp
%temp%\tcm.tmp -encode #{executable} %temp%\T1140_calc2.txt
%temp%\tcm.tmp -decode %temp%\T1140_calc2.txt %temp%\T1140_calc2_decoded.exe
```

### Cleanup

```cmd
del %temp%\tcm.tmp >nul 2>&1
del %temp%\T1140_calc2.txt >nul 2>&1
del %temp%\T1140_calc2_decoded.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1140/T1140.yaml)
