---
atomic_guid: "a123ce6a-3916-45d6-ba9c-7d4081315c27"
title: "Tamper with Windows Defender Evade Scanning -Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a123ce6a-3916-45d6-ba9c-7d4081315c27"
  - "Tamper with Windows Defender Evade Scanning -Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender Evade Scanning -Process

Malware can exclude specific processes from being scanned and evading detection.
Upon successful execution, the process(es) should be on the list of excluded processes. 
To check the exclusion list using poweshell  (Get-MpPreference).ExclusionProcess."

## Metadata

- Atomic GUID: a123ce6a-3916-45d6-ba9c-7d4081315c27
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### excluded_process

- description: A list of processes to exclude from scanning
- type: string
- default: outlook.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$excludedProcess = "#{excluded_process}"
Add-MpPreference -ExclusionProcess $excludedProcess
```

### Cleanup

```powershell
$excludedProcess = "#{excluded_process}"
Remove-MpPreference -ExclusionProcess  $excludedProcess
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
