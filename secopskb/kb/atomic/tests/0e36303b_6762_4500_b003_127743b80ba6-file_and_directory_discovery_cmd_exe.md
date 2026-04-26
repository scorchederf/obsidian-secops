---
atomic_guid: "0e36303b-6762-4500-b003-127743b80ba6"
title: "File and Directory Discovery (cmd.exe)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "0e36303b-6762-4500-b003-127743b80ba6"
  - "File and Directory Discovery (cmd.exe)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File and Directory Discovery (cmd.exe)

Find or discover files on the file system.  Upon successful execution, this test will output the results of all the data discovery commands to a specified file.

## Metadata

- Atomic GUID: 0e36303b-6762-4500-b003-127743b80ba6
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### output_file

- description: File to output results to
- type: string
- default: %temp%\T1083Test1.txt

## Executor

- name: command_prompt

### Command

```cmd
dir /s c:\ >> #{output_file}
dir /s "c:\Documents and Settings" >> #{output_file}
dir /s "c:\Program Files\" >> #{output_file}
dir "%systemdrive%\Users\*.*" >> #{output_file}
dir "%userprofile%\AppData\Roaming\Microsoft\Windows\Recent\*.*" >> #{output_file}
dir "%userprofile%\Desktop\*.*" >> #{output_file}
tree /F >> #{output_file}
```

### Cleanup

```cmd
del #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
