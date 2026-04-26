---
atomic_guid: "3448824b-3c35-4a9e-a8f5-f887f68bea21"
title: "Terminal Server Client Connection History Cleared"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "3448824b-3c35-4a9e-a8f5-f887f68bea21"
  - "Terminal Server Client Connection History Cleared"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Terminal Server Client Connection History Cleared

The built-in Windows Remote Desktop Connection (RDP) client (mstsc.exe) saves the remote computer name (or IP address) and the username that is used to login after each successful connection to the remote computer

## Metadata

- Atomic GUID: 3448824b-3c35-4a9e-a8f5-f887f68bea21
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Dependencies

Must have the "MR9" Remote Desktop Connection history Key

### Prerequisite Check

```powershell
if ((Get-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Terminal Server Client\Default\").MR9) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -path "HKCU:\SOFTWARE\Microsoft\" -name "Terminal Server Client"  -ErrorAction Ignore
New-Item -path "HKCU:\SOFTWARE\Microsoft\Terminal Server Client\" -name "Default" -ErrorAction Ignore
New-Itemproperty -path "HKCU:\SOFTWARE\Microsoft\Terminal Server Client\Default" -name "MR9" -value "127.0.0.1"  -PropertyType "String" -ErrorAction Ignore
New-Item -path "HKCU:\SOFTWARE\Microsoft\Terminal Server Client\" -name "Servers" -ErrorAction Ignore
New-Item -path "HKCU:\SOFTWARE\Microsoft\Terminal Server Client\Servers" -name "Redcanary" -ErrorAction Ignore
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" /va /f
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
