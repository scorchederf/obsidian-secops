---
atomic_guid: "ac7e6118-473d-41ec-9ac0-ef4f1d1ed2f6"
title: "Grant Full Access to folder for Everyone - Ryuk Ransomware Style"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222.001"
attack_technique_name: "File and Directory Permissions Modification: Windows File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ac7e6118-473d-41ec-9ac0-ef4f1d1ed2f6"
  - "Grant Full Access to folder for Everyone - Ryuk Ransomware Style"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Grant Full Access to folder for Everyone - Ryuk Ransomware Style

Invokes the command line similar to that used by Ryuk Ransomware to grant full access to the entire C:\ drive for Everyone.
**icacls "C:\*" /grant Everyone:F /T /C /Q**
However, for this atomic we set the permission on C:\Users\Public so it completes faster and doesn't irreversibly affect the host.
You can set your own path variable to "C:\*" if you prefer.

## Metadata

- Atomic GUID: ac7e6118-473d-41ec-9ac0-ef4f1d1ed2f6
- Technique: T1222.001: File and Directory Permissions Modification: Windows File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: command_prompt
- Source Path: atomics/T1222.001/T1222.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222.001]]

## Input Arguments

### file_path

- description: Path of folder permission back
- type: path
- default: %temp%\T1222.001-folder-perms-backup.txt

### path

- description: Path of folder to recursively set permissions on
- type: path
- default: C:\Users\Public\*

## Dependencies

Backup of original folder permissions should exist (for use in cleanup commands)

### Prerequisite Check

```text
IF EXIST #{file_path} ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```text
icacls #{path} /save #{file_path} /t /q >nul 2>&1
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
icacls "#{path}" /grant Everyone:F /T /C /Q
```

### Cleanup

```commandprompt
icacls '#{path}' /restore #{file_path} /q >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222.001/T1222.001.yaml)
