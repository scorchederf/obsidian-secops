---
atomic_guid: "51005ac7-52e2-45e0-bdab-d17c6d4916cd"
title: "System File Copied to Unusual Location"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036"
attack_technique_name: "Masquerading"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036/T1036.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "51005ac7-52e2-45e0-bdab-d17c6d4916cd"
  - "System File Copied to Unusual Location"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System File Copied to Unusual Location

It may be suspicious seeing a file copy of an EXE in System32 or SysWOW64 to a non-system directory or executing from a non-system directory.

## Metadata

- Atomic GUID: 51005ac7-52e2-45e0-bdab-d17c6d4916cd
- Technique: T1036: Masquerading
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1036/T1036.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Executor

- name: powershell

### Command

```powershell
copy-item "$env:windir\System32\cmd.exe" -destination "$env:allusersprofile\cmd.exe"
start-process "$env:allusersprofile\cmd.exe"
sleep -s 5 
stop-process -name "cmd" | out-null
```

### Cleanup

```powershell
remove-item "$env:allusersprofile\cmd.exe" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036/T1036.yaml)
