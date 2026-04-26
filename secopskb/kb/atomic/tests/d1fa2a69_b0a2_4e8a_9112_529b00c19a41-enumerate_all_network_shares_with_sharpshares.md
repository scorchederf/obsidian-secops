---
atomic_guid: "d1fa2a69-b0a2-4e8a-9112-529b00c19a41"
title: "Enumerate All Network Shares with SharpShares"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d1fa2a69-b0a2-4e8a-9112-529b00c19a41"
  - "Enumerate All Network Shares with SharpShares"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate All Network Shares with SharpShares

SharpShares is a command line tool that can be integrated with Cobalt Strike's execute-assembly module, allowing for the enumeration of network shares. 
This technique has been utilized by various ransomware groups, including BianLian.
[Reference](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a)

## Metadata

- Atomic GUID: d1fa2a69-b0a2-4e8a-9112-529b00c19a41
- Technique: T1135: Network Share Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Input Arguments

### output_path

- description: File to output enumeration results to
- type: String
- default: $env:temp\T1135SharpSharesOutput.txt

### sharp_path

- description: Path to the SharpShares executable
- type: String
- default: PathToAtomicsFolder\..\ExternalPayloads\SharpShares.exe

## Dependencies

The SharpShares executable must exist on disk

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\SharpShares.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/mitchmoser/SharpShares/releases/download/v2.4/SharpShares.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\SharpShares.exe"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cmd /c '#{sharp_path}' /ldap:all | out-file -filepath "#{output_path}"
```

### Cleanup

```powershell
remove-item "#{output_path}" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
