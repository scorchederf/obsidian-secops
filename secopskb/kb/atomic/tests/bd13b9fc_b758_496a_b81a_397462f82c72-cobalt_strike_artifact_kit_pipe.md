---
atomic_guid: "bd13b9fc-b758-496a-b81a-397462f82c72"
title: "Cobalt Strike Artifact Kit pipe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1559"
attack_technique_name: "Inter-Process Communication"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559/T1559.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "bd13b9fc-b758-496a-b81a-397462f82c72"
  - "Cobalt Strike Artifact Kit pipe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cobalt Strike Artifact Kit pipe

Uses the [Named Pipes Micro Emulation](https://github.com/center-for-threat-informed-defense/adversary_emulation_library/tree/master/micro_emulation_plans/src/named_pipes) executable from the Center for Threat Informed Defense to create a named pipe for inter-process communication.

The named pipe executable will pause for 30 seconds to allow the client and server to exchange a message through the pipe.

## Metadata

- Atomic GUID: bd13b9fc-b758-496a-b81a-397462f82c72
- Technique: T1559: Inter-Process Communication
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1559/T1559.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1559-inter-process_communication|T1559]]

## Dependencies

Named pipe executors must exist on disk

### Prerequisite Check

```powershell
if ((Test-Path "PathToAtomicsFolder\..\ExternalPayloads\build\namedpipes_executor.exe") -and (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\build\namedpipes_client.exe") -and (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\build\namedpipes_server.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing)
$zipUrl  = "https://github.com/center-for-threat-informed-defense/adversary_emulation_library/raw/master/micro_emulation_plans/src/named_pipes/named_pipes.zip"
Invoke-FetchFromZip $zipUrl "*.exe" "PathToAtomicsFolder\..\ExternalPayloads"
```

## Executor

- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\build\namedpipes_executor.exe" --pipe 1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1559/T1559.yaml)
