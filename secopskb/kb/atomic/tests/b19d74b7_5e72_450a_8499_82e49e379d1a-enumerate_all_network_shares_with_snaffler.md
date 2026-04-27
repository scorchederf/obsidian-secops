---
atomic_guid: "b19d74b7-5e72-450a-8499-82e49e379d1a"
title: "Enumerate All Network Shares with Snaffler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b19d74b7-5e72-450a-8499-82e49e379d1a"
  - "Enumerate All Network Shares with Snaffler"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enumerate All Network Shares with Snaffler

Snaffler is an open-source tool that has been used by various threat groups, including Scattered Spider/Muddled Libra, to enumerate accessible shares and credential-containing files within a domain. 
[Reference](https://unit42.paloaltonetworks.com/muddled-libra/)

## Metadata

- Atomic GUID: b19d74b7-5e72-450a-8499-82e49e379d1a
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
- default: $env:temp\T1135SnafflerOutput.txt

### snaffler_path

- description: Path to the Snaffler executable
- type: String
- default: PathToAtomicsFolder\..\ExternalPayloads\Snaffler.exe

## Dependencies

The Snaffler executable must exist on disk

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\Snaffler.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/SnaffCon/Snaffler/releases/download/1.0.150/Snaffler.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\Snaffler.exe"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
invoke-expression 'cmd /c start powershell -command { cmd /c "#{snaffler_path}" -a -o "#{output_path}" }; start-sleep 90; stop-process -name "snaffler"'
```

### Cleanup

```powershell
remove-item "#{output_path}" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
