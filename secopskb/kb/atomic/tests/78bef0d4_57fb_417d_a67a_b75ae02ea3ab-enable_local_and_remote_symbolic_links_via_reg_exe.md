---
atomic_guid: "78bef0d4-57fb-417d-a67a-b75ae02ea3ab"
title: "Enable Local and Remote Symbolic Links via reg.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222"
attack_technique_name: "File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "78bef0d4-57fb-417d-a67a-b75ae02ea3ab"
  - "Enable Local and Remote Symbolic Links via reg.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enable Local and Remote Symbolic Links via reg.exe

Use reg.exe to enable both ‘remote to local’ and ‘remote to remote’ symbolic links. This allows access to files from local shortcuts with local or remote paths.
[reference](https://symantec-enterprise-blogs.security.com/threat-intelligence/noberus-blackcat-alphv-rust-ransomware/)

## Metadata

- Atomic GUID: 78bef0d4-57fb-417d-a67a-b75ae02ea3ab
- Technique: T1222: File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1222/T1222.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v SymlinkRemoteToLocalEvaluation /t REG_DWORD /d "1" /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v SymlinkRemoteToRemoteEvaluation /t REG_DWORD /d "1" /f
```

### Cleanup

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v SymlinkRemoteToLocalEvaluation /t REG_DWORD /d "0" /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v SymlinkRemoteToRemoteEvaluation /t REG_DWORD /d "0" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml)
