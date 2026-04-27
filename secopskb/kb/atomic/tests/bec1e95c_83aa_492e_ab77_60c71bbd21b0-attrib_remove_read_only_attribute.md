---
atomic_guid: "bec1e95c-83aa-492e-ab77-60c71bbd21b0"
title: "attrib - Remove read-only attribute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.001"
attack_technique_name: "File and Directory Permissions Modification: Windows File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "bec1e95c-83aa-492e-ab77-60c71bbd21b0"
  - "attrib - Remove read-only attribute"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Removes the read-only attribute from a file or folder using the attrib.exe command. Upon execution, no output will be displayed.
Open the file in File Explorer > Right Click - Prperties and observe that the Read Only checkbox is empty.

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification#^t1222001-windows-file-and-directory-permissions-modification|T1222.001: Windows File and Directory Permissions Modification]]

## Input Arguments

### file_or_folder

- description: Path of the file or folder remove attribute.
- type: path
- default: %temp%\T1222.001_attrib

## Dependencies

Test requrires a file to modify to be located at (#{file_or_folder})

### Prerequisite Check

```cmd
IF EXIST #{file_or_folder} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```cmd
mkdir #{file_or_folder}
echo T1222.001_attrib1 >> #{file_or_folder}\T1222.001_attrib1.txt
echo T1222.001_attrib2 >> #{file_or_folder}\T1222.001_attrib2.txt
attrib.exe +r #{file_or_folder}\T1222.001_attrib1.txt
attrib.exe +r #{file_or_folder}\T1222.001_attrib2.txt
```

## Executor

- name: command_prompt

### Command

```cmd
attrib.exe -r #{file_or_folder}\*.* /s
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml)
