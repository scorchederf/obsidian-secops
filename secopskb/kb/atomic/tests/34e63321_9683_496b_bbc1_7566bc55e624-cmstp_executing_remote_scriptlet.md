---
atomic_guid: "34e63321-9683-496b-bbc1-7566bc55e624"
title: "CMSTP Executing Remote Scriptlet"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.003"
attack_technique_name: "Signed Binary Proxy Execution: CMSTP"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.003/T1218.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "34e63321-9683-496b-bbc1-7566bc55e624"
  - "CMSTP Executing Remote Scriptlet"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CMSTP Executing Remote Scriptlet

Adversaries may supply CMSTP.exe with INF files infected with malicious commands

## Metadata

- Atomic GUID: 34e63321-9683-496b-bbc1-7566bc55e624
- Technique: T1218.003: Signed Binary Proxy Execution: CMSTP
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.003/T1218.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Input Arguments

### inf_file_path

- description: Path to the INF file
- type: path
- default: PathToAtomicsFolder\T1218.003\src\T1218.003.inf

## Dependencies

INF file must exist on disk at specified location (#{inf_file_path})

### Prerequisite Check

```powershell
if (Test-Path "#{inf_file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{inf_file_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.003/src/T1218.003.inf" -OutFile "#{inf_file_path}"
```

## Executor

- name: command_prompt

### Command

```cmd
cmstp.exe /s "#{inf_file_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.003/T1218.003.yaml)
