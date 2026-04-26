---
atomic_guid: "44315fb0-f78d-4cef-b10f-cf21c1fe2c75"
title: "Windows - Simulate CPU Load with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1496"
attack_technique_name: "Resource Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1496/T1496.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "44315fb0-f78d-4cef-b10f-cf21c1fe2c75"
  - "Windows - Simulate CPU Load with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Simulate CPU Load with PowerShell

This test simulates high CPU load using PowerShell, commonly seen in resource hijacking.
Spawns background jobs to stress CPU cores for a specified duration.

## Metadata

- Atomic GUID: 44315fb0-f78d-4cef-b10f-cf21c1fe2c75
- Technique: T1496: Resource Hijacking
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1496/T1496.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]

## Input Arguments

### cpu_threads

- description: Number of threads to stress (default 4)
- type: integer
- default: 4

### duration_seconds

- description: Duration in seconds to run the CPU stress test
- type: integer
- default: 30

## Executor

- name: powershell

### Command

```powershell
$end = (Get-Date).AddSeconds(#{duration_seconds})
1..#{cpu_threads} | ForEach-Object { Start-Job { param($t) while((Get-Date) -lt $t) { $i=0; while($i -lt 200000){$i++} } } -ArgumentList $end }
Get-Job | Wait-Job | Remove-Job
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1496/T1496.yaml)
