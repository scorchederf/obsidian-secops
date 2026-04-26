---
atomic_guid: "3d257a03-eb80-41c5-b744-bb37ac7f65c7"
title: "System Discovery - SocGholish whoami"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3d257a03-eb80-41c5-b744-bb37ac7f65c7"
  - "System Discovery - SocGholish whoami"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Discovery - SocGholish whoami

SocGholish performs whoami discovery commands and outputs the results to a tmp file. 
The test will generate a filename similar to the random one generated during execution and write the file to AppData\Temp.

Reference: https://redcanary.com/threat-detection-report/threats/socgholish/

## Metadata

- Atomic GUID: 3d257a03-eb80-41c5-b744-bb37ac7f65c7
- Technique: T1033: System Owner/User Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1033/T1033.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Input Arguments

### output_path

- description: Location of output file
- type: string
- default: $env:temp

## Executor

- name: powershell

### Command

```powershell
$TokenSet = @{
  U = [Char[]]'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  N = [Char[]]'0123456789'
}
$Upper = Get-Random -Count 5 -InputObject $TokenSet.U
$Number = Get-Random -Count 5 -InputObject $TokenSet.N
$StringSet = $Upper + $Number
$rad = (Get-Random -Count 5 -InputObject $StringSet) -join ''
$file = "rad" + $rad + ".tmp"

whoami.exe /all >> #{output_path}\$file
```

### Cleanup

```powershell
Remove-Item -Path #{output_path}\rad*.tmp -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
