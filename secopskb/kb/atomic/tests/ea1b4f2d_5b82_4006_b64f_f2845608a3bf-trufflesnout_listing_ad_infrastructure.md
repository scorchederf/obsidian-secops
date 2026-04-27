---
atomic_guid: "ea1b4f2d-5b82-4006-b64f-f2845608a3bf"
title: "TruffleSnout - Listing AD Infrastructure"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ea1b4f2d-5b82-4006-b64f-f2845608a3bf"
  - "TruffleSnout - Listing AD Infrastructure"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Iterative AD discovery toolkit for offensive operators. Situational awareness and targeted low noise enumeration. Preference for OpSec.- https://github.com/dsnezhkov/TruffleSnout

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]

## Input Arguments

### domain

- description: Domain name to search on
- type: string
- default: %userdomain%

### trufflesnout_path

- description: Path to the TruffleSnout executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\TruffleSnout.exe

## Dependencies

TruffleSnout.exe must exist on disk at specified location (#{trufflesnout_path})

### Prerequisite Check

```powershell
if (Test-Path "#{trufflesnout_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -ItemType Directory (Split-Path "#{trufflesnout_path}") -Force | Out-Null
Invoke-WebRequest -Uri "https://github.com/dsnezhkov/TruffleSnout/releases/download/0.5/TruffleSnout.exe" -OutFile "#{trufflesnout_path}"
```

## Executor

- name: command_prompt

### Command

```cmd
"#{trufflesnout_path}" forest -n #{domain}
"#{trufflesnout_path}" domain -n #{domain}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
