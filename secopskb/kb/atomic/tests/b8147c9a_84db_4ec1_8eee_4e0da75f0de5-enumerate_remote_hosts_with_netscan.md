---
atomic_guid: "b8147c9a-84db-4ec1-8eee-4e0da75f0de5"
title: "Enumerate Remote Hosts with Netscan"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "b8147c9a-84db-4ec1-8eee-4e0da75f0de5"
  - "Enumerate Remote Hosts with Netscan"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Remote Hosts with Netscan

This test uses Netscan to identify remote hosts in a specified network range.

## Metadata

- Atomic GUID: b8147c9a-84db-4ec1-8eee-4e0da75f0de5
- Technique: T1018: Remote System Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1018/T1018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Input Arguments

### netscan_path

- description: NetScan exe location
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\netscan\64-bit\netscan.exe

### range_to_scan

- description: The IP range to scan with Netscan
- type: string
- default: 127.0.0.1-127.0.0.1

## Dependencies

Netscan must be installed

### Prerequisite Check

```text
if (Test-Path "#{netscan_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\netscan.zip" "https://www.softperfect.com/download/files/netscan_portable.zip"
Expand-Archive -LiteralPath "PathToAtomicsFolder\..\ExternalPayloads\netscan.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\netscan"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cmd /c '#{netscan_path}' /hide /auto:"$env:temp\T1018NetscanOutput.txt" /range:'#{range_to_scan}'
```

### Cleanup

```powershell
remove-item "$env:temp\T1018NetscanOutput.txt" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
